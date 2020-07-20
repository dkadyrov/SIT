package edu.stevens.cs549.dhts.activity;

import edu.stevens.cs549.dhts.activity.DHTBase.Failed;
import edu.stevens.cs549.dhts.activity.DHTBase.Invalid;

/*
 * The part of the DHT business logic that is used in the CLI
 * (the business logic for a command line interface).
 */

public interface IDHTNode {
	
	/*
	 * Adding and deleting content at the local node.
	 */
	public String[] get(String k) throws Invalid;
	
	public void add(String k, String v) throws Invalid;
	
	public void delete(String k, String v) throws Invalid;
	
	/*
	 * Adding and deleting content in the network.
	 */
	public String[] getNet(String k) throws Failed;
	
	public void addNet(String k, String v) throws Failed;
	
	public void deleteNet(String k, String v) throws Failed;
	
	/*
	 * Insert this node into a DHT identified by a node's URI.
	 */
	public void join(String uri) throws Failed, Invalid;
	
	/*
	 * Display internal state at the CLI.
	 */
	public void display();
	
	public void routes();
	
}
