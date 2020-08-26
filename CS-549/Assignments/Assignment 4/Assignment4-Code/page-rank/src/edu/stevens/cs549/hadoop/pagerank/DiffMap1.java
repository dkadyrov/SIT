package edu.stevens.cs549.hadoop.pagerank;

import java.io.IOException;

import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.*;

public class DiffMap1 extends Mapper<LongWritable, Text, Text, Text> {

	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException,
			IllegalArgumentException {
		String line = value.toString(); // Converts Line to a String
		String[] sections = line.split("\t"); // Splits each line
		if (sections.length > 2) // checks for incorrect data format
		{
			throw new IOException("Incorrect data format");
		}
		/**
		*  TODO: read node-rank pair and emit: key:node, value:rank
		*/

		// Split into Node and Rank
		String[] node_rank = sections[0].split("\\+");

		// Emit Node and Rank
		context.write(new Text(node_rank[0]),  new Text(node_rank[1]));
	}

}
