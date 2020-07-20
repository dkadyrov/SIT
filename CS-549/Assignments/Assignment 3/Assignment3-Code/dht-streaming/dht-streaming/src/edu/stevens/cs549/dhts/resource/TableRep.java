package edu.stevens.cs549.dhts.resource;

import java.io.Serializable;
import java.util.Iterator;
import java.util.List;
import java.util.logging.Logger;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

import edu.stevens.cs549.dhts.activity.NodeInfo;

@XmlRootElement(name = "table")
// @XmlAccessorType(XmlAccessType)
public class TableRep implements Serializable {

	private static final long serialVersionUID = 1L;

	Logger log = Logger.getLogger(TableRep.class.getCanonicalName());

	@XmlElement
	public TableRow[] entry;

	/*
	 * Node id needed for transferring bindings to predecessor.
	 */
	@XmlElement
	public NodeInfo info;

	/*
	 * Successor (transmitted to pred for backup).
	 */
	@XmlElement
	public NodeInfo succ;

	public TableRep() {
		/*
		 * JAXB unmarshals empty entries as null.
		 */
		entry = new TableRow[0];
	}

	public TableRep(NodeInfo info, NodeInfo succ, List<TableRow> rows) {
		this(info, succ, rows.size());
		Iterator<TableRow> iter = rows.iterator();
		for (int i = 0; iter.hasNext(); i++) {
			entry[i] = iter.next();
		}
	}

	public TableRep(NodeInfo info, NodeInfo succ, int nrecs) {
		entry = new TableRow[nrecs];
		this.info = info;
		this.succ = succ;
	}

	public NodeInfo getInfo() {
		return info;
	}

	public NodeInfo getSucc() {
		return succ;
	}

}
