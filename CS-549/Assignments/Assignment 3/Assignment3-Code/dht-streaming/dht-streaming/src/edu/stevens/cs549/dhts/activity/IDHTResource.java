package edu.stevens.cs549.dhts.activity;

import org.glassfish.jersey.media.sse.EventOutput;

import edu.stevens.cs549.dhts.activity.DHTBase.Failed;
import edu.stevens.cs549.dhts.activity.DHTBase.Invalid;
import edu.stevens.cs549.dhts.resource.TableRep;


/*
 * The part of the DHT business logic that is used in the NodeActivity
 * class (the business logic for a node resource).
 */

public interface IDHTResource {
	
	public NodeInfo getNodeInfo();
	
	public NodeInfo getSucc();
	
	public NodeInfo getPred();
	
	/*
	 * Called externally during the join protocol.
	 */
	public NodeInfo findSuccessor(int id) throws Failed;
	
	/*
	 * Exposing the finger table in the node API.
	 * Alternatively search for predecessor tail-recursively,
	 * but be sure to redirect HTTP to the next node.
	 */
	public NodeInfo closestPrecedingFinger (int id);
	
	/*
	 * Called by a node to notify another node that it believes it is the latter
	 * node's new predecessor.  If acknowledged by the successor, then a range of
	 * key-value pairs is transferred from the successor  (all bindings 
	 * at the successor up to and including the key of the new predecessor).
	 * The predecessor supplies its own bindings, to be backed up
	 * at the successor.
	 */
	public TableRep notify (TableRep predDb);
	
	/*
	 * The operations for actually accessing the underlying hash table for a node.
	 */
	public String[] get(String k) throws Invalid;
	
	public void add(String k, String v) throws Invalid;
	
	public void delete(String k, String v) throws Invalid;
	
	/*
	 * Listen for bindings added for a key.
	 */
	public EventOutput listenForBindings(int id, String key);
	
	public void stopListening(int id, String key);
	
}
