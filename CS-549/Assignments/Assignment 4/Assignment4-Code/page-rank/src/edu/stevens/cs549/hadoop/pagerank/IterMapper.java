package edu.stevens.cs549.hadoop.pagerank;

import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.*;

public class IterMapper extends Mapper < LongWritable, Text, Text, Text > {

	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException, IllegalArgumentException {
		String line = value.toString(); // Converts Line to a String
		String[] sections = line.split("\t"); // Splits it into two parts. Part 1: node+rank | Part 2: adj list

		if (sections.length > 2) // Checks if the data is in the incorrect format
		{
			throw new IOException("Incorrect data format");
		}
		if (sections.length != 2) {
			return;
		}

		/* 
		 * TODO: emit key: adj vertex, value: computed weight.
		 * 
		 * Remember to also emit the input adjacency list for this node!
		 * Put a marker on the string value to indicate it is an adjacency list.
		 */
		// Split Line to Node and Rank
		String[] node_rank = sections[0].split("\\+");
		String node = String.valueOf(node_rank[0]);
		double rank = Double.valueOf(node_rank[1]);

		// Store Adjacent List
		String adjacent_list = sections[1].toString().trim();
		String[] adjacent_nodes = adjacent_list.split(" ");

		// Track Number of Nodes
		int n = adjacent_nodes.length;

		// Page Weight is 1/n * rank
		double page_weight = (double) 1 / n * rank;

		for (String adjacent_node: adjacent_nodes) {
			context.write(new Text(adjacent_node), new Text(String.valueOf(page_weight)));
		}

		context.write(new Text(node), new Text("adj:" + sections[1]));
	}
}