package edu.stevens.cs549.hadoop.pagerank;

import java.io.*;
import java.util.Iterator;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.*;

public class InitReducer extends Reducer<Text, Text, Text, Text> {

	public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
		/* 
		 * TODO: Output key: node+rank, value: adjacency list
		 */
		// Default Rank is 1
		int default_rank = 1;
		Iterator<Text> iterator = values.iterator();
		
		while(iterator.hasNext()) {
			// Emit Node and Rank, Value
			context.write(new Text(key + "+" + default_rank), iterator.next());
		}
	}
}
