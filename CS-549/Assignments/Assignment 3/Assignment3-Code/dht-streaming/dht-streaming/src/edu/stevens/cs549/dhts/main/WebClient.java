package edu.stevens.cs549.dhts.main;

import java.net.URI;
import java.util.logging.Logger;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.GenericType;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriBuilder;
import javax.xml.bind.JAXBElement;

import org.glassfish.jersey.media.sse.EventSource;
import org.glassfish.jersey.media.sse.SseFeature;

import edu.stevens.cs549.dhts.activity.DHTBase;
import edu.stevens.cs549.dhts.activity.NodeInfo;
import edu.stevens.cs549.dhts.activity.UriApi;
import edu.stevens.cs549.dhts.resource.TableRep;
import edu.stevens.cs549.dhts.resource.TableRow;

public class WebClient {

	private Logger log = Logger.getLogger(WebClient.class.getCanonicalName());

	private void error(String msg) {
		log.severe(msg);
	}

	/*
	 * Encapsulate Web client operations here.
	 * 
	 * TODO: Fill in missing operations.
	 */

	/*
	 * Creation of client instances is expensive, so just create one.
	 */
	protected Client client;

	protected Client listenClient;

	public WebClient() {
		client = ClientBuilder.newClient();
		listenClient = ClientBuilder.newBuilder().register(SseFeature.class).build();
	}

	private void info(String mesg) {
		Log.info(mesg);
	}

	private Response getRequest(URI uri) {
		try {
			Response cr = client.target(uri).request(MediaType.APPLICATION_XML_TYPE)
					.header(Time.TIME_STAMP, Time.advanceTime()).get();
			processResponseTimestamp(cr);
			return cr;
		} catch (Exception e) {
			error("Exception during GET request: " + e);
			return null;
		}
	}

	private Response putRequest(URI uri, Entity<?> entity) {
		try {
			Response cr = client.target(uri).request(MediaType.APPLICATION_XML_TYPE)
					.header(Time.TIME_STAMP, Time.advanceTime()).put(entity);
			processResponseTimestamp(cr);
			return cr;
		} catch (Exception e) {
			error("Exception during PUT request: " + e);
			return null;
		}
	}

	private Response delRequest(URI deletePath) {
		try {
			Response cr = client.target(deletePath).request(MediaType.APPLICATION_XML_TYPE)
					.header(Time.TIME_STAMP, Time.advanceTime()).delete();
			processResponseTimestamp(cr);
			return cr;
		} catch (Exception e) {
			error("Exception during DELETE request: " + e);
			return null;
		}
	}

	private Response putRequest(URI uri) {
		return putRequest(uri, Entity.text(""));
	}

	private void processResponseTimestamp(Response cr) {
		Time.advanceTime(Long.parseLong(cr.getHeaders().getFirst(Time.TIME_STAMP).toString()));
	}

	/*
	 * Jersey way of dealing with JAXB client-side: wrap with run-time type
	 * information.
	 */
	private GenericType<JAXBElement<NodeInfo>> nodeInfoType = new GenericType<JAXBElement<NodeInfo>>() {
	};

	private GenericType<JAXBElement<TableRow>> tableRowType = new GenericType<JAXBElement<TableRow>>() {
	};

	/*
	 * Ping a remote site to see if it is still available.
	 */
	public boolean isFailed(URI base) {
		URI uri = UriBuilder.fromUri(base).path("info").build();
		Response c = getRequest(uri);
		return c.getStatus() >= 300;
	}

	/*
	 * Get the predecessor pointer at a node.
	 */
	public NodeInfo getPred(NodeInfo node) throws DHTBase.Failed {
		URI predPath = UriBuilder.fromUri(node.addr).path("pred").build();
		info("client getPred(" + predPath + ")");
		Response response = getRequest(predPath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("GET /pred");
		} else {
			NodeInfo pred = response.readEntity(nodeInfoType).getValue();
			return pred;
		}
	}

	public NodeInfo getSucc(NodeInfo node) throws DHTBase.Failed {
		URI succPath = UriBuilder.fromUri(node.addr).path("succ").build();
		info("client getSucc(" + succPath + ")");
		Response response = getRequest(succPath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("GET /succ");
		} else {
			NodeInfo succ = response.readEntity(nodeInfoType).getValue();
			return succ;
		}
	}

	public NodeInfo closestPrecedingFinger(NodeInfo node, int id) throws DHTBase.Failed {
		UriBuilder ub = UriBuilder.fromUri(node.addr).path("findClosestPrecedingFinger");
		URI getPath = ub.queryParam("id", id).build();
		info("client findClosestPrecedingFinger(" + getPath + ")");
		Response response = getRequest(getPath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("GET /findClosestPrecedingFinger?id=ID");
		} else {
			return response.readEntity(nodeInfoType).getValue();
		}
	}

	public NodeInfo findSuccessor(URI addr, int id) throws DHTBase.Failed {
		UriBuilder ub = UriBuilder.fromUri(addr).path("find");
		URI findPath = ub.queryParam("id", id).build();
		info("client findSuccessor(" + findPath + ")");
		Response response = getRequest(findPath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("GET /find?id=ID");
		} else {
			return response.readEntity(nodeInfoType).getValue();
		}
	}

	public String[] get(NodeInfo n, String k) throws DHTBase.Failed {
		UriBuilder ub = UriBuilder.fromUri(n.addr).path("getValue");
		URI getPath = ub.queryParam("key", k).build();
		info("client getValue(" + getPath + ")");
		Response response = getRequest(getPath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("GET /getValue?id=ID");
		} else {
			return response.readEntity(tableRowType).getValue().vals;
		}
	}

	public void add(NodeInfo n, String k, String v) throws DHTBase.Failed {
		UriBuilder ub = UriBuilder.fromUri(n.addr).path("add");
		URI addPath = ub.queryParam("key", k).queryParam("value", v).build();
		TableRep tablerep = new TableRep(null, null, 1);
		tablerep.entry[0] = new TableRow(k, new String[] { v });
		info("client add(" + addPath + ")");
		Response response = putRequest(addPath, Entity.xml(tablerep));
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("PUT /add?id=ID");
		}

	}

	public void delete(NodeInfo n, String k, String v) throws DHTBase.Failed {
		UriBuilder ub = UriBuilder.fromUri(n.addr).path("delete");
		URI deletePath = ub.queryParam("key", k).queryParam("value", v).build();
		info("client delete(" + deletePath + ")");
		Response response = delRequest(deletePath);
		if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("DELETE /delete?id=ID");
		}
	}

	/*
	 * Notify node that we (think we) are its predecessor.
	 */
	public TableRep notify(NodeInfo node, TableRep predDb) throws DHTBase.Failed {
		/*
		 * The protocol here is more complex than for other operations. We notify a new
		 * successor that we are its predecessor, and expect its bindings as a result.
		 * But if it fails to accept us as its predecessor (someone else has become
		 * intermediate predecessor since we found out this node is our successor i.e.
		 * race condition that we don't try to avoid because to do so is infeasible), it
		 * notifies us by returning null. This is represented in HTTP by RC=304 (Not
		 * Modified).
		 */
		NodeInfo thisNode = predDb.getInfo();
		UriBuilder ub = UriBuilder.fromUri(node.addr).path("notify");
		URI notifyPath = ub.queryParam("id", thisNode.id).build();
		info("client notify(" + notifyPath + ")");
		Response response = putRequest(notifyPath, Entity.xml(predDb));
		if (response != null && response.getStatusInfo() == Response.Status.NOT_MODIFIED) {
			/*
			 * Do nothing, the successor did not accept us as its predecessor.
			 */
			return null;
		} else if (response == null || response.getStatus() >= 300) {
			throw new DHTBase.Failed("PUT /notify?id=ID");
		} else {
			TableRep bindings = response.readEntity(TableRep.class);
			return bindings;
		}
	}

	public EventSource listenForBindings(NodeInfo node, int id, String skey) throws DHTBase.Failed {
		// TODO listen for SSE subscription requests on http://.../dht/listen?key=<key>
		// On the service side, don't expect LT request or response headers for this
		// request.
		// Note: "id" is client's id, to enable us to stop event generation at the
		// server.
		String uri = String.format(node.addr + UriApi.LISTEN, id, skey);
		WebTarget target = listenClient.target(uri);
		EventSource eventSource = new EventSource(target, false);
		return eventSource;

	}

	public void listenOff(NodeInfo node, int id, String skey) throws DHTBase.Failed {
		// TODO listen for SSE subscription requests on http://.../dht/listen?key=<key>
		// On the service side, don't expect LT request or response headers for this
		// request.

		String uri = String.format(node.addr + UriApi.LISTEN, id, skey);
		try {
			delRequest(new URI(uri));
		} catch (Exception e) {
			throw new DHTBase.Failed("listen Off error. message: " + e);
		}
	}

}
