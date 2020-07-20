package edu.stevens.cs549.dhts.state;

import java.io.IOException;

import edu.stevens.cs549.dhts.activity.NodeInfo;
import edu.stevens.cs549.dhts.resource.TableRep;

/*
 * The interface for a state server that maintains the
 * local (key,value)-pair bindings for a DHT node.
 * This should ONLY be accessed locally by the DHT Web service.
 * Think of it as a database server for a DHT node.
 */
public interface IState {

	/*
	 * The key for a node.
	 */
	public NodeInfo getNodeInfo();

	/*
	 * Get all values stored under a key.
	 */
	public String[] get(String k);

	/*
	 * Add a binding under a key (always cumulative).
	 */
	public void add(String k, String v);

	/*
	 * Delete a binding under a key.
	 */
	public void delete(String k, String v);

	/*
	 * Clear all bindings (necessary if a node joins a network with pre-existing
	 * bindings).
	 */
	public void clear();

	/*
	 * These operations support the protocol for data transfers between pred &
	 * succ.
	 */

	/*
	 * The successor uses this operation to create a table of some of its
	 * bindings, for transmission to its predecessor. TableRep also contains
	 * succ pointer, so predecessor can alert successor to take over if this
	 * node fails.
	 */
	public TableRep extractBindings(int predId);

	public TableRep extractBindings();

	/*
	 * The successor uses this to remove bindings it has transferred to the
	 * predecessor.
	 */
	public void dropBindings(int id);

	/*
	 * The predecessor uses this operation to install all bindings into its
	 * internal hash table, as part of its own initialization.
	 */
	public void installBindings(TableRep bindings);

	/*
	 * The successor uses this operation to install the predecessor's bindings
	 * into backup storage. Each node is also a hot standby for its predecessor.
	 */
	public void backupBindings(TableRep bindings);

	/*
	 * Each node backs up the successor pointer of its successor, and notifies
	 * the succ of the succ when it should take over from succ.
	 */
	public void backupSucc(TableRep bindings);

	/*
	 * Back up the bindings in the table to a file.
	 */
	public void backup(String filename) throws IOException;

	/*
	 * Reload the bindings from a file.
	 */
	public void reload(String filename) throws IOException;

	/*
	 * Display the contents of the local hash table.
	 */
	public void display();
	
}
