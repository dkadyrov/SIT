package edu.stevens.cs549.ftpserver;

import java.net.InetAddress;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

import edu.stevens.cs549.ftpinterface.IServer;
import edu.stevens.cs549.ftpinterface.IServerFactory;

/**
 * @author dduggan
 *
 */
public class ServerFactory extends UnicastRemoteObject implements
		IServerFactory {
	
	private String pathPrefix = "/";
	
	/*
	 * Specify host (IP address) for multi-homed hosts.
	 * Specify port of server for allowing access through a firewall.
	 */
	private InetAddress host;
	private int serverPort;
	
	static final long serialVersionUID = 0L;

	public ServerFactory(InetAddress h, int port, String p) throws RemoteException {
		super(port);
		this.host = h;
		this.serverPort = port;
		this.pathPrefix = p;
	}

	public IServer createServer() throws RemoteException {
		return new Server(host, serverPort, pathPrefix);
	}

}
