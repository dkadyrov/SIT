/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package edu.stevens.cs549.dhts.main;

import java.io.BufferedReader;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.logging.Logger;

import edu.stevens.cs549.dhts.activity.DHT;
import edu.stevens.cs549.dhts.activity.IDHTBackground;
import edu.stevens.cs549.dhts.activity.IDHTNode;
import edu.stevens.cs549.dhts.activity.NodeInfo;
import edu.stevens.cs549.dhts.state.IRouting;
import edu.stevens.cs549.dhts.state.IState;
import edu.stevens.cs549.dhts.state.Persist;

/*
 * CLI for a DHT node.
 */

public class CliClient {

	public static Logger log = Logger
			.getLogger("edu.stevens.cs549.dht.main.Client");
	

	protected IDHTNode node;
	
	protected WebClient client;
	
	protected Main main;
	
	protected long key;
	
	public CliClient(NodeInfo info, IState s, IRouting r, Main m) {
		node = new DHT(info, s, r);
		client = new WebClient();
		main = m;
		key = info.id;
	}

	protected void msg(String m) {
		System.out.print(m);;
	}

	protected void msgln(String m) {
		System.out.println(m);
		System.out.flush();
	}

	protected void err(Exception e) {
		main.severe("Error : " + e);
		e.printStackTrace();
	}
	
	public IDHTBackground getDHT() {
		return (IDHTBackground)node;
	}

	public void cli() {

		// Main command-line interface loop

		Dispatch d = new Dispatch(client, node);
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		try {
			while (true) {
				msg("dht<" + key + "> ");
				String line = in.readLine();
				String[] inputs = line.split("\\s+");
				if (inputs.length > 0) {
					String cmd = inputs[0];
					if (cmd.length() == 0)
						;
//					else if ("lget".equals(cmd))
//						d.localGet(inputs);
//					else if ("ladd".equals(cmd))
//						d.localAdd(inputs);
//					else if ("ldel".equals(cmd))
//						d.localDelete(inputs);
					else if ("get".equals(cmd))
						d.get(inputs);
					else if ("add".equals(cmd))
						d.add(inputs);
					else if ("del".equals(cmd))
						d.delete(inputs);
					else if ("bindings".equals(cmd))
						d.bindings(inputs);
					else if ("join".equals(cmd))
						d.join(inputs);
					else if ("routes".equals(cmd))
						d.routes(inputs);
					else if ("ping".equals(cmd))
						d.ping(inputs);
					else if ("silent".equals(cmd))
						d.background(inputs);
					else if ("debug".equals(cmd))
						d.debug(inputs);
					else if ("weblog".equals(cmd))
						d.weblog(inputs);
//					else if ("listenOn".equals(cmd))
//						d.listenOn(inputs);
//					else if ("listenOff".equals(cmd))
//						d.listenOff(inputs);
//					else if ("listeners".equals(cmd))
//						d.listeners(inputs);
					else if ("help".equals(cmd))
						d.help(inputs);
					else if ("quit".equals(cmd))
						return;
					else
						msgln("Bad input.  Type \"help\" for more information.");
				}
			}
		} catch (EOFException e) {
		} catch (IOException e) {
			err(e);
			System.exit(-1);
		}

	}
	
	protected class Dispatch {

		protected WebClient client;
		protected IDHTNode node;
		
		protected 

		Dispatch(WebClient c, IDHTNode n) {
			client = c;
			node = n;
		}

		public void help(String[] inputs) {
			if (inputs.length == 1) {
				msgln("Commands are:");
//				// Local commands
//				msgln("  lget key: (local) get values under a key");
//				msgln("  ladd key value: (local) add a value under a key");
//				msgln("  ldel key value: (local) delete a value under a key");
				// Network-wide commands
				msgln("  get key: get values under a key");
				msgln("  add key value: add a value under a key");
				msgln("  del key value: delete a value under a key");
				// Network protocol
				msgln("  join uri: join a DHT as a new node");
				msgln("  bindings: display all key-value bindings");
				msgln("  routes: display routing information");
				msgln("  ping uri: check if a remote node is active");
				// Logging commands.
				msgln("  background: toggle on and off logging of background processing");
				msgln("  weblog: toggle on and off web service logging");
				msgln("  debug: toggle on and off debug logging");
//				// Listening commands.
//				msgln("  listenOn key: request notification of a change in binding for this key");
//				msgln("  listenOff key: disable any further notifications for this key");
//				msgln("  listeners: keys for which listeners are defined");
				
				msgln("  quit: exit the client");
			}
		}

//		public void localGet(String[] inputs) {
//			if (inputs.length == 2)
//				try {
//					String[] vs = node.get(inputs[1]);
//					if (vs != null)
//						msgln(Persist.displayVals(vs));
//				} catch (Exception e) {
//					err(e);
//				}
//			else
//				msgln("Usage: lget <key>");
//		}
//
//		public void localAdd(String[] inputs) {
//			if (inputs.length == 3)
//				try {
//					node.add(inputs[1], inputs[2]);
//				} catch (Exception e) {
//					err(e);
//				}
//			else
//				msgln("Usage: ladd <key> <value>");
//		}
//
//		public void localDelete(String[] inputs) {
//			if (inputs.length == 3)
//				try {
//					node.delete(inputs[1], inputs[2]);
//				} catch (Exception e) {
//					err(e);
//				}
//			else
//				msgln("Usage: ldel <key> <value>");
//		}

		public void get(String[] inputs) {
			if (inputs.length == 2)
				try {
					String[] vs = node.getNet(inputs[1]);
					if (vs != null)
						msgln(Persist.displayVals(vs));
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: get <key>");
		}

		public void add(String[] inputs) {
			if (inputs.length == 3)
				try {
					node.addNet(inputs[1], inputs[2]);
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: add <key> <value>");
		}

		public void delete(String[] inputs) {
			if (inputs.length == 3)
				try {
					node.deleteNet(inputs[1], inputs[2]);
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: del <key> <value>");
		}

		public void bindings(String[] inputs) {
			if (inputs.length == 1)
				try {
					node.display();
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: display");
		}

		public void routes(String[] inputs) {
			if (inputs.length == 1)
				try {
					node.routes();
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: routes");
		}

		public void background(String[] inputs) {
			if (inputs.length == 1)
				try {
					main.toggleBackground();
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: background");
		}

		public void debug(String[] inputs) {
			if (inputs.length == 1)
				try {
					Main.toggleDebug();
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: debug");
		}

		public void weblog(String[] inputs) {
			if (inputs.length == 1)
				try {
//					client.toggleLogging();
					Log.setLogging();
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: silent");
		}

		public void ping(String[] inputs) {
			if (inputs.length == 2)
				try {
					if (client.isFailed(new URI(inputs[1]))) {
						msgln("Server down.");
					} else {
						msgln("Server up.");
					}
				} catch (URISyntaxException e) {
					msgln("Badly formed URI: "+inputs[1]);
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: ping <uri>");
		}

		public void join(String[] inputs) {
			if (inputs.length == 2)
				try {
					node.join(inputs[1]);
				} catch (Exception e) {
					err(e);
				}
			else
				msgln("Usage: insert <uri>");
		}

	}

}
