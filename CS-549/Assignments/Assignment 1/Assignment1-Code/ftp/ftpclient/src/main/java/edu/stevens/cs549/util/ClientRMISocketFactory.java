package edu.stevens.cs549.util;

/*
 * Copyright (c) 2005-2007 Augur Systems, Inc.  All Rights Reserved.
 *
 * Augur Systems, Inc. ("ASI") grants you ("Licensee") 
 * a non-exclusive, royalty free, license to use,
 * modify and redistribute this software in source and binary code form,
 * provided that i) this copyright notice and license appear on all copies of
 * the software; and ii) Licensee does not utilize the software in a manner
 * which is disparaging to ASI.
 *
 * This software is provided "AS IS," without a warranty of any kind. ALL
 * EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY
 * IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR
 * NON-INFRINGEMENT, ARE HEREBY EXCLUDED. ASI AND ITS LICENSORS SHALL NOT BE
 * LIABLE FOR ANY DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
 * OR DISTRIBUTING THE SOFTWARE OR ITS DERIVATIVES. IN NO EVENT WILL ASI OR ITS
 * LICENSORS BE LIABLE FOR ANY LOST REVENUE, PROFIT OR DATA, OR FOR DIRECT,
 * INDIRECT, SPECIAL, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER
 * CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF THE USE OF
 * OR INABILITY TO USE SOFTWARE, EVEN IF ASI HAS BEEN ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGES.
 *
 * This software is not designed or intended for use in on-line control of
 * aircraft, air traffic, aircraft navigation or aircraft communications; or in
 * the design, construction, operation or maintenance of any nuclear
 * facility. Licensee represents and warrants that it will not use or
 * redistribute the Software for such purposes.
 */

import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketAddress;
import java.rmi.server.RMISocketFactory;
import java.util.Map;

/**
 * This is meant to override the default RMISocketFactory. The default factory
 * provides sockets with very long timeouts, resulting in approx. 5-minute hang
 * delays when connections are attempted to IP addresses that are currently
 * inaccessible (offline or non-existent on subnet). This new implementation
 * provides shorter timeouts, approx 30-seconds.
 * <p>
 * Not 100% sure of resulting delay... it may be multiplied by 3 in the end,
 * since RMI may try three ways: 1) socket 2) html 3) cgi (per Sun javadoc)
 * <p>
 * To use, just instantiate once within your JVM, prerably before any RMI code.
 * (Additional attempts will throw exceptions.)
 * <p>
 * A map of proxy redirects, and/or a single default proxy is supported. See
 * setProxies() and setProxy() for more info.
 * 
 * @author Chris.Janicki@AugurSystems.com
 */
public class ClientRMISocketFactory extends RMISocketFactory {
	private static final boolean debug = true;
	private static int timeoutMillis;
	private static InetAddress server;
	private static Map proxies;
	private static String proxy;

	/**
	 * Creates a new instance of ClientRMISocketFactory with a default 10-sec
	 * timeout, and installs itself as the new default; can only happen once,
	 * else an exception is thrown.
	 */
	public ClientRMISocketFactory() throws IOException {
		this(null, 10000);
	}

	/**
	 * Creates a new instance of ClientRMISocketFactory, and installs itself as
	 * the new default; can only happen once, else an exception is thrown.
	 * 
	 * @param server
	 *            The InetAddress of the network interface on which to bind
	 *            server sockets; if null, will bind to all interfaces.
	 */
	public ClientRMISocketFactory(InetAddress server, int timeoutMillis)
			throws IOException {
		this.timeoutMillis = timeoutMillis;
		this.server = server;
		RMISocketFactory.setSocketFactory(this);
	}

	/**
	 * Implements RMISocketFactory by just creating a normal ServerSocket; same
	 * as default impl?
	 */
	public ServerSocket createServerSocket(int port) throws IOException {
		ServerSocket ss = new ServerSocket(port, 50, server);
		return ss;
	}

	/**
	 * Implements RMISocketFactory by creating a Socket, but connecting with a
	 * short timeout; 5-sec(may act like 15-sec... see class javadoc) or as
	 * defined in the constructor.
	 * <p>
	 * May replace the given host with a proxy if configured; first the proxies
	 * map is checked; if no match there then the default proxy is used if
	 * configured; otherwise no host replacement is made.
	 */
	public Socket createSocket(String host, int port) throws IOException {
		// Replace host with proxy, if defined via lookup map or default
		// proxy...
		if (proxies != null) {
			String p = proxies.get(host).toString();
			if (p != null) {
				host = p;
			} else if (proxy != null)
				host = proxy;
		} else if (proxy != null) {
			host = proxy;
		}

		Socket s = new Socket();
		SocketAddress sa = new InetSocketAddress(host, port);
		try {
			s.connect(sa, timeoutMillis);
		} catch (IOException ioe) // timeout
		{
			throw ioe;
		}
		return s;
	}

	/**
	 * Set an optional lookup map for defining hosts that should be routed
	 * through a proxy. For example, when a server is protected behind a NAT
	 * router, an external client may be able to connect to the server's RMI
	 * registry through the router, but any stub addresses returned by the RMI
	 * registry will reference the server's real address (not reachable directly
	 * by the client). So a proxy map can replace the server's address with the
	 * NAT address.
	 * <p>
	 * Note that traditionally, the java.rmi.server.hostname property could be
	 * set to advertise the NAT address instead of the protected address on the
	 * server's RMI Registry JVM, but if that same Registry is used by other
	 * servers on the same protected network, then their stub connections would
	 * be routed through the external NAT address, which is not efficient or
	 * secure. Note that this is only an issue in a client-server system where
	 * there are multiple networked servers. A stand-alone system is fine just
	 * using the java.rmi.server.hostname property.
	 * <p>
	 * This method may be called anytime after construction; subsequent calls
	 * overwrite any previous setting. Note that this RMISocketFactory is
	 * essentially static in the JVM, so any proxy changes affect all users.
	 * 
	 * @param proxies
	 *            A Map, possibly null, whose keys are the String IP addresses
	 *            of the protected servers; the values are the associated public
	 *            NAT addresses. The proxy map will be used whenever the
	 *            createSocket() method is called. The proxies do not affect the
	 *            createServerSocket() method.
	 */
	public void setProxies(Map proxies) {
		this.proxies = proxies;
	}

	/**
	 * Optional: Set a default proxy for all calls to createSocket(), replacing
	 * any host passed to that call; may be overridden if a proxies Map contains
	 * a proxy for the given host. See the javadoc for setProxies() for more
	 * background info.
	 * <p>
	 * This method may be called anytime after construction; subsequent calls
	 * overwrite any previous setting. Note that this RMISocketFactory is
	 * essentially static in the JVM, so any proxy changes affect all users.
	 */
	public void setProxy(String proxy) {
		this.proxy = proxy;
	}

}