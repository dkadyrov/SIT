package edu.stevens.cs549.dhts.resource;

import java.util.logging.Logger;

import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;

import org.glassfish.jersey.media.sse.EventOutput;
import org.glassfish.jersey.media.sse.SseFeature;

import edu.stevens.cs549.dhts.activity.DHTBase.Invalid;

@Path("/dht")
public class NodeResource {

	/*
	 * Web service API.
	 * 
	 * TODO: Fill in the missing operations.
	 */

	Logger log = Logger.getLogger(NodeResource.class.getCanonicalName());

	@Context
	UriInfo uriInfo;

	@Context
	HttpHeaders headers;

	@GET
	@Path("info")
	@Produces("application/xml")
	public Response getNodeInfoXML() {
		return new NodeService(headers, uriInfo).getNodeInfo();
	}

	@GET
	@Path("info")
	@Produces("application/json")
	public Response getNodeInfoJSON() {
		return new NodeService(headers, uriInfo).getNodeInfo();
	}

	@GET
	@Path("pred")
	@Produces("application/xml")
	public Response getPred() {
		return new NodeService(headers, uriInfo).getPred();
	}

	@PUT
	@Path("notify")
	@Consumes("application/xml")
	@Produces("application/xml")
	/*
	 * Actually returns a TableRep (annotated with @XmlRootElement)
	 */
	public Response putNotify(TableRep predDb) {
		/*
		 * See the comment for WebClient::notify (the client side of this logic).
		 */
		return new NodeService(headers, uriInfo).notify(predDb);
	}

	@GET
	@Path("find")
	@Produces("application/xml")
	public Response findSuccessor(@QueryParam("id") String index) {
		int id = Integer.parseInt(index);
		return new NodeService(headers, uriInfo).findSuccessor(id);
	}

	@GET
	@Path("succ")
	@Produces("application/xml")
	public Response getSucc() {
		return new NodeService(headers, uriInfo).getSucc();
	}

	@GET
	@Path("findClosestPrecedingFinger")
	@Produces("application/xml")
	public Response findClosestPrecedingFinger(@QueryParam("id") String index) {
		int id = Integer.parseInt(index);
		return new NodeService(headers, uriInfo).findClosestPrecedingFinger(id);
	}

	@GET
	@Path("getValue")
	@Produces("application/xml")
	public Response getValue(@QueryParam("key") String key) throws Invalid {
		return new NodeService(headers, uriInfo).getValue(key);
	}

	@PUT
	@Path("add")
	@Consumes("application/xml")
	public Response add(TableRep tablerep) throws Invalid {
		return new NodeService(headers, uriInfo).add(tablerep.entry[0].key, tablerep.entry[0].vals[0]);
	}

	@DELETE
	@Path("delete")
	@Consumes("application/xml")
	public Response delete(@QueryParam("key") String key, @QueryParam("value") String value) throws Invalid {
		return new NodeService(headers, uriInfo).delete(key, value);
	}

	@GET
	@Path("listen")
	@Produces(SseFeature.SERVER_SENT_EVENTS)
	public EventOutput listenOn(@QueryParam("id") int id, @QueryParam("key") String key) {
		return new NodeService(headers, uriInfo).listen(id, key);
	}

	@DELETE
	@Path("listen")
	public Response listenOff(@QueryParam("id") int id, @QueryParam("key") String key) {
		return new NodeService(headers, uriInfo).stopListening(id, key);
	}

}
