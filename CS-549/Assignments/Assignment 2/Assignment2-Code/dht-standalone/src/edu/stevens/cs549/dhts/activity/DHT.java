package edu.stevens.cs549.dhts.activity;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.logging.Logger;

import javax.ws.rs.core.UriInfo;

import edu.stevens.cs549.dhts.main.Main;
import edu.stevens.cs549.dhts.main.WebClient;
import edu.stevens.cs549.dhts.resource.TableRep;
import edu.stevens.cs549.dhts.state.IRouting;
import edu.stevens.cs549.dhts.state.IState;

public class DHT extends DHTBase implements IDHTResource, IDHTNode, IDHTBackground {

	/*
	 * DHT logic.
	 * 
	 * This logic may be invoked from a RESTful Web service or from the command
	 * line, as reflected by the interfaces.
	 */

	/*
	 * Client stub for Web service calls.
	 */
	protected WebClient client = new WebClient();

	public WebClient getClient() {
		return client;
	}

	private boolean debug() {
		return Main.debug();
	}

	private void debug(String msg) {
		if (debug())
			info(msg);
	}

	/*
	 * Logging operations.
	 */

	protected Logger log = Logger.getLogger(DHT.class.getCanonicalName());

	protected void info(String s) {
		log.info(s);
	}

	protected void warning(String s) {
		log.warning(s);
	}

	protected void severe(String s) {
		log.severe(s);
	}

	/*
	 * The URL for this node in the DHT. Although the info is stored in state,
	 * we should be able to cache it locally since it does not change.
	 */
	protected NodeInfo info;

	/*
	 * Remote clients may call this when joining the network and they know only
	 * our URI and need the node identifier (key) as well.
	 */
	// WebMethod
	public NodeInfo getNodeInfo() {
		assert this.info != null;
		return this.info;
	}

	/*
	 * Key-value pairs stored in this node.
	 */
	private IState state;

	/*
	 * Finger tables, and predecessor and successor pointers.
	 */
	private IRouting routing;

	/*
	 * This constructor is called when a DHT object is created for the CLI.
	 */
	public DHT(NodeInfo info, IState s, IRouting r) {
		this.info = info;
		this.state = s;
		this.routing = r;
	}

	/*
	 * This constructor is called when a DHT object is created in a Web service.
	 */
	public DHT(UriInfo uri) {
		this.state = Main.stateServer();
		this.routing = Main.routingServer();
		this.info = state.getNodeInfo();
	}

	/*
	 * Get the successor of a node. Need to perform a Web service call to that
	 * node, and it then retrieves its routing state from its local RMI object.
	 * 
	 * Make a special case for when this is the local node, i.e.,
	 * info.addr.equals(localInfo.addr), otherwise get an infinite loop.
	 */
	private NodeInfo getSucc(NodeInfo info) throws Failed {
		NodeInfo localInfo = this.getNodeInfo();
		if (localInfo.addr.equals(info.addr)) {
			return getSucc();
		} else {
			// TODO: Do the Web service call
			return client.getSucc(info);
		}
	}

	/*
	 * This version gets the local successor from routing tables.
	 */
	// WebMethod
	public NodeInfo getSucc() {
		return routing.getSucc();
	}

	/*
	 * Set the local successor pointer in the routing tables.
	 */
	public void setSucc(NodeInfo succ) {
		routing.setSucc(succ);
	}

	/*
	 * Get the predecessor of a node. Need to perform a Web service call to that
	 * node, and it then retrieves its routing state from its local routing
	 * tables.
	 * 
	 * Make a special case for when this is the local node, i.e.,
	 * info.addr.equals(localInfo.addr), otherwise get an infinite loop.
	 */
	protected NodeInfo getPred(NodeInfo info) throws Failed {
		NodeInfo localInfo = this.getNodeInfo();
		if (localInfo.addr.equals(info.addr)) {
			return getPred();
		} else {
			/*
			 * TODO: Do the Web service call
			 */
			return client.getPred(info);
		}
	}

	/*
	 * This version gets the local predecessor from routing tabes.
	 */
	// WebMethod
	public NodeInfo getPred() {
//		routing.joinCheck();
		return routing.getPred();
	}

	/*
	 * Set the local predecessor pointer in the routing tables.
	 */
	protected void setPred(NodeInfo pred) {
		routing.setPred(pred);
	}

	/*
	 * Perform a Web service call to get the closest preceding finger in the
	 * finger table of the argument node.
	 */
	protected NodeInfo closestPrecedingFinger(NodeInfo info, int id) throws Failed {
		NodeInfo localInfo = this.getNodeInfo();
		if (localInfo.equals(info)) {
			return closestPrecedingFinger(id);
		} else {
			if (IRouting.USE_FINGER_TABLE) {
				/*
				 * TODO: Do the Web service call to the remote node.
				 */
				return client.closestPrecedingFinger(info, id);
			} else {
				/*
				 * Without finger tables, just use the successor pointer.
				 */
				return getSucc(info);
			}
		}
	}

	/*
	 * For the local version, get from the routing table.
	 */
	// WebMethod
	public NodeInfo closestPrecedingFinger(int id) {
		return routing.closestPrecedingFinger(id);
	}

	/*
	 * Set a finger pointer.
	 */
	protected void setFinger(int ix, NodeInfo node) {
		routing.setFinger(ix, node);
	}

	/*
	 * Find the node that will hold bindings for a key k. Search the circular
	 * list to find the node. Stop when the node's successor stores values
	 * greater than k.
	 */
	protected NodeInfo findPredecessor(int id) throws Failed {
		NodeInfo info = getNodeInfo();
		NodeInfo succ = getSucc(info);
		if (info.id != succ.id) {
			while (!inInterval(id, info.id, succ.id)) {
				info = closestPrecedingFinger(info, id);
				succ = getSucc(info);
				/*
				 * Break out of infinite loop (e.g. our successor may be
				 * a single-node network that still points to itself).
				 */
				if (getNodeInfo().equals(info)) {
					break;
				}
			}
		}
		return info;
	}

	/*
	 * Find the successor of k, starting at the current node. Called internally
	 * and (server-side) in join protocol.
	 */
	// WebMethod
	public NodeInfo findSuccessor(int id) throws Failed {
		NodeInfo predInfo = findPredecessor(id);
		return getSucc(predInfo);
	}

	/*
	 * Find the successor of k, given the URI for a node. Used as client part of
	 * the join protocol.
	 */
	protected NodeInfo findSuccessor(URI addr, int id) throws Failed {
		return client.findSuccessor(addr, id);
	}

	/*
	 * Stabilization logic.
	 * 
	 * Called by background thread & in join protocol by joining node (as new
	 * predecessor).
	 */
	public boolean stabilize() throws Failed {
		debug("Starting stabilize()");
		NodeInfo info = getNodeInfo();
		NodeInfo succ = getSucc();
		if (info.equals(succ)) {
			debug("Ending stabilize() 1");
			return true;
		}

		// Possible synchronization point (see join() below).
		NodeInfo predOfSucc = getPred(succ);
		if (predOfSucc == null) {
			/*
			 * Successor's predecessor is not set, so we will become pred.
			 * Notify succ that we believe we are its predecessor. Provide our
			 * bindings, that will be backed up by our successor. Expect
			 * transfer of bindings from succ as ack.
			 * 
			 * Note: We pass in our bindings to the successor for backing up.
			 * We don't use this now, but might in a future assignment.
			 * 
			 * Do the Web service call.
			 */
			debug("Joining succ with null pred.");
			TableRep db = client.notify(succ, state.extractBindings());
			debug("Ending stabilize() 2");
			return notifyContinue(db);
		} else if (inInterval(predOfSucc.id, info.id, succ.id, false)) {
			setSucc(predOfSucc);
			/*
			 * Successor's predecessor should be our predecessor. Notify pred of
			 * succ that we believe we are its predecessor. Expect transfer of
			 * bindings from succ as ack.
			 * 
			 * Do the Web service call.
			 */
			debug("Joining succ as new, closer pred.");
			/*
			 * Note: We notify predOfSucc in this case, since we have
			 * set that as our successor.
			 */
			TableRep db = client.notify(predOfSucc, state.extractBindings());
			debug("Ending stabilize() 3");
			// The bindings we got back will be merged with our current bindings.
			return notifyContinue(db);
		} else if (inInterval(info.id, predOfSucc.id, succ.id, false)) {
			/*
			 * Has some node inserted itself between us and the successor? This
			 * could happen due to a race condition between setting our
			 * successor pointer and notifying the successor.
			 */
			debug("Notifying succ that we are its pred.");
			TableRep db = client.notify(succ, state.extractBindings());
			debug("Ending stabilize() 4");
			return notifyContinue(db);
		} else {
			/*
			 * We come here if we are already the predecessor, so no change.
			 */
			debug("Ending stabilize() 5");
			return false;
		}
	}

	// WebMethod
	public TableRep notify(TableRep predDb) {
		/*
		 * Node cand ("candidate") believes it is our predecessor.
		 */
		NodeInfo cand = predDb.getInfo();
		NodeInfo pred = getPred();
		NodeInfo info = getNodeInfo();
		if (pred == null || inInterval(cand.id, pred.id, info.id, false)) {
			setPred(cand);
			/*
			 * If this is currently a single-node network, close the loop by
			 * setting our successor to our pred. Thereafter the network should
			 * update automatically as new predecessors are detected by old
			 * predecessors.
			 */
			if (getSucc().equals(info)) {
				setSucc(cand);
				// We must also set pred of succ (i.e. cand) to point back
				// to us. This will be done by stabilize().
			}
			/*
			 * Transfer our bindings up to cand.id to our new pred (the
			 * transferred bindings will be in the response). We will back up
			 * their bindings (this was sent as an argument in notify()).
			 */
			TableRep db = transferBindings(cand.id);
			// Back up predecessor bindings. Might be used in future assignment.
			state.backupBindings(predDb);
			debug("Transferring bindings to node id=" + cand.id);
			return db;
		} else {
			/*
			 * Null indicates that we did not accept new pred. This may be
			 * because cand==pred.
			 */
			return null;
		}
	}

	/*
	 * Process the result of a notify to a potential successor node.
	 */
	protected boolean notifyContinue(TableRep db) {
		if (db == null) {
			/*
			 * We are out.
			 */
			return false;
		} else {
			/*
			 * Set pred pointer for the case where our successor is also our
			 * predecessor?
			 */
			if (getNodeInfo().equals(db.succ)) {
				setPred(db.info);
			}
			/*
			 * db is bindings we take from the successor.
			 */
			debug("Installing bindings from successor.");
			state.installBindings(db);
			return true;
		}
	}

	/*
	 * Transfer our bindings up to predId to a new predecessor.
	 */
	protected TableRep transferBindings(int predId) {
		TableRep db = state.extractBindings(predId);
		state.dropBindings(predId);
		return db;
	}

	private int next = 0;

	/*
	 * Periodic refresh of finger table based on changed successor.
	 */
	protected void fixFinger() {
		int localNext;
		synchronized(state) {
			next = (next + 1) % IRouting.NFINGERS;
			localNext = next;
		}
		/*
		 * Compute offset = 2^next
		 */
		int offset = 1;
		for (int i = 0; i < localNext; i++)
			offset = offset * 2;
		/*
		 * finger[next] = findSuccessor (n + 2^next)
		 */
		int nextId = (getNodeInfo().id + offset) % IRouting.NKEYS;
		try {
			setFinger(localNext, findSuccessor(nextId));
		} catch (Failed e) {
			warning("FixFinger: findSuccessor(" + nextId + ") failed.");
		}
	}

	/*
	 * Speed up the finger table refresh.
	 */
	// Called by background thread.
	public void fixFingers(int ntimes) throws Error {
		for (int i = 0; i < ntimes; i++) {
			fixFinger();
		}
	}

	/*
	 * Check if the predecessor has failed.
	 */
	// Called by background thread.
	public void checkPredecessor() {
		/*
		 * Ping the predecessor node by asking for its successor.
		 */
		NodeInfo pred = getPred();
		if (pred != null) {
			try {
				getSucc(pred);
			} catch (Failed e) {
				info("CheckPredecessor: Predecessor has failed (id=" + pred.id + ")");
				setPred(null);
			}
		}
	}

	/*
	 * Get the values under a key at the specified node. If the node is the
	 * current one, go to the local state.
	 */
	protected String[] get(NodeInfo n, String k) throws Failed {
		if (n.addr.equals(info.addr)) {
			try {
				return this.get(k);
			} catch (Invalid e) {
				severe("Get: invalid internal inputs: " + e);
				throw new IllegalArgumentException(e);
			}
		} else {
			/*
			 * Retrieve the bindings at the specified node.
			 * 
			 * TODO: Do the Web service call.
			 */
			return client.get(n, k);
		}
	}

	/*
	 * Retrieve values under the key at the current node.
	 */
	// WebMethod
	public String[] get(String k) throws Invalid {
		return state.get(k);
	}

	/*
	 * Add a value under a key.
	 */
	public void add(NodeInfo n, String k, String v) throws Failed {
		if (n.addr.equals(info.addr)) {
			try {
				add(k, v);
			} catch (Invalid e) {
				severe("Add: invalid internal inputs: " + e);
				throw new IllegalArgumentException(e);
			}
		} else {
			/*
			 * TODO: Do the Web service call.
			 */
			client.add(n, k, v);
		}
	}

	/*
	 * Store a value under a key at the local node.
	 */
	// WebMethod
	public void add(String k, String v) throws Invalid {
		/*
		 * Validate that this binding can be stored here.
		 */
		int kid = DHTBase.NodeKey(k);
		NodeInfo info = getNodeInfo();
		NodeInfo pred = getPred();

		if (pred != null && inInterval(kid, pred.id, info.id, true)) {
			/*
			 * This node covers the interval in which k should be stored.
			 */
			state.add(k, v);
		} else if (pred == null && info.equals(getSucc())) {
			/*
			 * Single-node network.
			 */
			state.add(k, v);
		} else if (info.id == kid) {
			/*
			 * ???
			 */
			state.add(k, v);			
		} else if (pred == null && info.equals(getSucc())) {
			severe("Add: predecessor is null but not a single-node network.");
		} else {
			throw new Invalid("Invalid key: " + k + " (id=" + kid + ")");
		}
	}

	/*
	 * Delete value under a key.
	 */
	public void delete(NodeInfo n, String k, String v) throws Failed {
		if (n.addr.equals(info.addr)) {
			try {
				delete(k, v);
			} catch (Invalid e) {
				severe("Delete: invalid internal inputs: " + e);
				throw new IllegalArgumentException(e);
			}
		} else {
			/*
			 * TODO: Do the Web service call.
			 */
			client.delete(n, k, v);

		}
	}

	/*
	 * Delete value under a key at the local node.
	 */
	// WebMethod
	public void delete(String k, String v) throws Invalid {
		state.delete(k, v);
	}

	/*
	 * These operations perform the CRUD logic at the network level.
	 */

	/*
	 * Store a value under a key in the network.
	 */
	public void addNet(String skey, String v) throws Failed {
		int id = NodeKey(skey);
		//if the key's id is equal to the nodes id then add it locally
		if (info.id == id)
			add(info, skey, v);
		else {
			NodeInfo succ = this.findSuccessor(id);
			add(succ, skey, v);
		}
	}

	/*
	 * Get the values under a key in the network.
	 */
	public String[] getNet(String skey) throws Failed {
		int id = NodeKey(skey);
		// if the key's id is equal to the nodes id then get it locally
		if (info.id == id)
			return get(info, skey);
		else {
			NodeInfo succ = this.findSuccessor(id);
			return get(succ, skey);
		}
	}

	/*
	 * Delete a value under a key in the network.
	 */
	public void deleteNet(String skey, String v) throws Failed {
		int id = NodeKey(skey);
		//if the key's id is equal to the nodes id then delete it locally
		if (info.id == id)
			delete(info, skey, v);
		else {
			NodeInfo succ = this.findSuccessor(id);
			delete(succ, skey, v);
		}
	}

	/*
	 * Join logic.
	 */

	/*
	 * Insert this node into the DHT identified by uri.
	 */
	public void join(String uri) throws Failed, Invalid {
		setPred(null);
		NodeInfo info = getNodeInfo();
		NodeInfo succ;
		/*
		 * TODO: Do a web service call to the node identified by "uri" and find
		 * the successor of info.id, then setSucc(succ). Make sure to clear any
		 * local bindings first of all, to maintain consistency of the ring. We
		 * start afresh with the bindings that are transferred from the new
		 * successor.
		 * 
		 * Do a stabilize() here. Stabilize() will set the succ node's pred
		 * pointing back to us. In the case of inserting into a single-node
		 * network, there is a potential race condition: notify() will also set
		 * succ in the singleton to point back to us (a special case in
		 * notify()). If the singleton does stabilize(), it will find our pred
		 * null and perform notify() to get bindings from us. It is important
		 * that it keeps its own bindings, to which it adds those it transfers
		 * from us.
		 */
		try {
			succ = findSuccessor(new URI(uri), info.id);
			setSucc(succ);
		} catch (URISyntaxException e) {
			e.printStackTrace();
		}
		stabilize();

	}

	/*
	 * State display operations for CLI.
	 */

	public void display() {
		state.display();
	}

	public void routes() {
		routing.routes();
	}
	
}
