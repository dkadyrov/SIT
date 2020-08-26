package edu.stevens.cs549.hadoop.pagerank;

import java.io.IOException;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.*;

public class FinMapper extends Mapper < LongWritable, Text, DoubleWritable, Text > {
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException,IllegalArgumentException {
		String line = value.toString(); // Converts Line to a String
		/*
		 * TODO output key:-rank, value: node
		 * See IterMapper for hints on parsing the output of IterReducer.
		 */
		String[] sections = line.split("\t"); // nodeId+nodeName | rank

		// Check Format of Data
		if (sections.length > 2) {
			throw new IOException("Incorrect data format");
		}
		if (sections.length != 2) {
			return;
		}

		// 0-Rank will Reverse Shuffle the Reducer
		context.write(new DoubleWritable(0 - Double.valueOf(sections[1])), new Text(sections[0]));
	}
}