package edu.stevens.cs549.dhts.resource;

import java.io.Serializable;

//import com.sun.xml.txw2.annotation.XmlElement;
//import javax.xml.bind.annotation.XmlElement;

//@XmlElement
public class TableRow implements Serializable {
	
	/*
	 * Persisting table on disk.
	 */
		
	private static final long serialVersionUID = 1L;

	public String key;
	
	public String[] vals;
	
	public TableRow (String k, String[] vs) {
		this.key = k;
		this.vals = vs;
	}
	
	public TableRow () {
	}
	
}
