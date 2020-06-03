package edu.stevens.cs549.ftpserver;

import java.io.InputStream;
import java.net.InetAddress;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.List;
import java.util.Properties;
import java.util.logging.Logger;

import org.apache.log4j.PropertyConfigurator;

/**
 *
 * @author dduggan
 */
public class ServerMain {
	
	protected String serverIp;
	
	protected int serverPort;
	
	private static String serverPropsFile = "/server.properties";
	private static String loggerPropsFile = "/log4j.properties";

	private static Logger log = Logger.getLogger(ServerMain.class.getCanonicalName());

	public void severe(String s) {
		log.severe(s);
	}

	public void warning(String s) {
		log.info(s);
	}

	public void info(String s) {
		log.info(s);
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
			if ("serverIp".equals(k))
				serverIp = opts.get("host");
			else if ("serverPort".equals(k))
				serverPort = Integer.parseInt(opts.get("http"));
			else
				severe("Unrecognized option: --" + k);
		}

		return commandLineArgs;
	}
	
	
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    	
/*        PropertyConfigurator.configure(ServerMain.class.getClassLoader()
                .getResource(loggerPropsFile));
*/
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }
        new ServerMain(args);
    }
    
	public ServerMain (String[] args) {
    	try {
            PropertyConfigurator.configure(getClass().getResource(loggerPropsFile));
    		/*
    		 * Load server properties.
    		 */
    		Properties props = new Properties();
    		InputStream in = getClass().getResourceAsStream(serverPropsFile);
    		props.load(in);
    		in.close();
        	String rootDir = (String)props.get("server.path");
        	String serverName = (String)props.get("server.name");
        	serverIp = (String)props.get("server.ip");
        	serverPort = Integer.parseInt((String)props.get("server.port"));
        	/*
        	 * Process overrides from command line
        	 */
        	processArgs(args);
        	/*
        	 * Register factory object in registry.
        	 */
            ServerFactory stub = new ServerFactory (InetAddress.getByName(serverIp), serverPort, rootDir);
            Registry registry = LocateRegistry.createRegistry(serverPort);
            registry.rebind(serverName, stub);
            Server.log.info("Server bound [port="+serverPort+"]");
    	
    	} catch (java.io.FileNotFoundException e) {
    		System.err.println ("Server error: "+serverPropsFile+" file not found.");
    	} catch (java.io.IOException e) {
    		System.err.println ("Server error: IO exception.");
    	} catch (Exception e) {
    		Server.log.severe ("Server exception:");
    		e.printStackTrace();
    	}
    	
    }

}