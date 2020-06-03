package edu.stevens.cs549.ftpinterface;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IServer extends Remote {

	public void get(String f) throws IOException, FileNotFoundException,
			RemoteException;

	public void put(String f) throws IOException, FileNotFoundException,
			RemoteException;

	public String pwd() throws RemoteException;

	public void cd(String d) throws IOException, RemoteException;

	public String[] dir() throws RemoteException;

	public void port(InetSocketAddress s) throws RemoteException;

	public InetSocketAddress pasv() throws IOException, RemoteException;

}
