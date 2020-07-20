package edu.stevens.cs549.dhts.main;

import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.List;
import java.util.Properties;
import java.util.Random;
import java.util.logging.Logger;

import javax.ws.rs.core.UriBuilder;

import org.glassfish.grizzly.http.server.HttpServer;
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;

import edu.stevens.cs549.dhts.activity.Background;
import edu.stevens.cs549.dhts.activity.NodeInfo;
import edu.stevens.cs549.dhts.state.IRouting;
import edu.stevens.cs549.dhts.state.State;
//import com.sun.jersey.api.container.grizzly2.GrizzlyServerFactory;
//import com.sun.jersey.api.core.PackagesResourceConfig;
//import com.sun.jersey.api.core.ResourceConfig;

public class Main {

	public static final String serverPropsFile = "/server.properties";
	public static final String loggerPropsFile = "/log4j.properties";

	private static Logger log = Logger.getLogger(Main.class.getCanonicalName());

	private static boolean debug = false;
	
	public static boolean debug() {
		return debug;
	}
	
	public static void toggleDebug() {
		debug = !debug;
	}

	public void severe(String s) {
		log.severe(s);
	}

	public void warning(String s) {
		log.info(s);
	}

	public void info(String s) {
		log.info(s);
	}

	/*
	 * Allow logging of background processing to be turned on and off.
	 */
	protected boolean background = true;

	public void toggleBackground() {
		background = !background;
	}

	public void bgSevere(String s) {
		if (!background)
			severe(s);
	}

	public void bgWarning(String s) {
		if (!background)
			info(s);
	}

	public void bgInfo(String s) {
		if (!background)
			info(s);
	}

	/*
	 * Hostname and port for HTTP server URL.
	 */
	private static String host;
	private static int httpPort;

	private static URI getBaseURI() {
		return UriBuilder.fromUri("http://" + host).port(httpPort).build();
	}

	public static URI getURI(URI base) {
		return UriBuilder.fromUri(base).path("dht").build();
	}

	private static State stateServer;

	public static State stateServer() {
		return stateServer;
	}

	private static IRouting routingServer;

	public static IRouting routingServer() {
		return routingServer;
	}

	public final static String DHT_STATE = "DHT_STATE";

	/*
	 * The key for our place in the Chord ring. We will set it to a random id,
	 * and then set if a value was specified on the command line.
	 */
	private static int nodeId;

	protected static URI BASE_URI;

	protected static NodeInfo INFO;

	protected State stub;

	protected Registry registry;

	private Main(String[] args) {

		try {
			/*
			 * Load server properties.
			 */
			Properties props = new Properties();
			InputStream in = getClass().getResourceAsStream(serverPropsFile);
			props.load(in);
			in.close();

			httpPort = Integer.parseInt((String) props.getProperty("server.port.http", "8080"));
			host = (String) props.getProperty("server.host", "localhost");

			nodeId = new Random().nextInt(IRouting.NKEYS);

			/*
			 * Properties may be overridden by command line options.
			 */

			processArgs(args);

			BASE_URI = getBaseURI();

			INFO = new NodeInfo(nodeId, getURI(BASE_URI));

		} catch (java.io.FileNotFoundException e) {
			severe("Server error: " + serverPropsFile + " file not found.");
		} catch (java.io.IOException e) {
			severe("Server error: IO exception.");
		} catch (Exception e) {
			severe("Server exception:" + e);
		}
	}

	protected List<String> processArgs(String[] args) {
		List<String> commandLineArgs = new ArrayList<String>();
		int ix = 0;
		Hashtable<String, String> opts = new Hashtable<String, String>();

		while (ix < args.length) {
			if (args[ix].startsWith("--")) {
				String option = args[ix++].substring(2);
				if (ix == args.length || args[ix].startsWith("--"))
					severe("Missing argument for --" + option + " option.");
				else if (opts.containsKey(option))
					severe("Option \"" + option + "\" already set.");
				else
					opts.put(option, args[ix++]);
			} else {
				commandLineArgs.add(args[ix++]);
			}
		}
		/*
		 * Overrides of values from configuration file.
		 */
		Enumeration<String> keys = opts.keys();
		while (keys.hasMoreElements()) {
			String k = keys.nextElement();
			if ("host".equals(k))
				host = opts.get("host");
			else if ("http".equals(k))
				httpPort = Integer.parseInt(opts.get("http"));
			else if ("id".equals(k))
				nodeId = Integer.parseInt(opts.get("id"));
			else
				severe("Unrecognized option: --" + k);
		}

		return commandLineArgs;
	}

	protected State startStateServer() throws IOException {
		info("Starting state server...");
		State stub = new State(INFO);
		stateServer = stub;
		routingServer = stub;
		info("State server bound.");
		return stub;
	}

	protected HttpServer startHttpServer() throws IOException {
		info("Starting HTTP server.");
		return GrizzlyHttpServerFactory.createHttpServer(BASE_URI, new Application());
	}

	protected boolean terminated = false;

	public void setTerminated() {
		terminated = true;
	}

	public boolean isTerminated() {
		return terminated;
	}

	public static void main(String[] args) throws IOException {
		Main main = new Main(args);

		/*
		 * Start the state server for this node.
		 */
		main.startStateServer();
		/*
		 * Start the HTTP server (for Web services) and background thread for
		 * stabilize.
		 */
		CliClient client = new CliClient(INFO, stateServer(), routingServer(), main);
		HttpServer httpServer = main.startHttpServer();
		Thread t = new Thread(new Background(5000, 8, main, client.getDHT()));
		t.start();
		/*
		 * Start the command-line loop.
		 */
		main.info(String.format("DHT Web service started with WADL available at "
				+ "%s/application.wadl\nTry out %s\nEntering command-line interface...", BASE_URI, INFO.addr.toString()));
		client.cli();

		/*
		 * Execute when the CLI terminates.
		 */
		main.info("Terminating background processing...");
		main.setTerminated();
		main.info("Shutting down Web server...");
		httpServer.stop();

	}
}
