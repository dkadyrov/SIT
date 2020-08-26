package edu.stevens.cs549.hadoop.pagerank;

import java.io.File;
import java.io.IOException;
import java.net.URI;

import org.apache.commons.io.FileUtils;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class JoinMapper extends Mapper < LongWritable, Text, Text, Text > {
	@Override
	protected void setup(Context context) throws IOException, InterruptedException {
		if (context.getCacheFiles() != null && context.getCacheFiles().length > 0) {
			URI mappingFileUri = context.getCacheFiles()[0];

			if (mappingFileUri != null) {
				System.out.println("Mapping File: " + FileUtils.readFileToString(new File("./cache")));
			} else {
				System.out.println("no mapping file");
			}
		} else {
			System.out.println("no cache file");
		}
	}

	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException, IllegalArgumentException {
		String line = value.toString();
		String[] sections;

		if (line.contains(":")) {
			int index = line.indexOf(":");
			sections = new String[2];
			sections[0] = line.substring(0, index);
			sections[1] = line.substring(index + 1, line.length());
		} else {
			sections = line.split("\t");
		}

		if (sections.length > 2) {
			throw new IOException("Incorrect data format");
		}

		String[] node_rank = sections[0].split("\\+");
		if (node_rank.length == 1) {
			context.write(new Text(node_rank[0]), new Text("name:" + sections[1].trim()));
		}
		if (node_rank.length == 2) {
			context.write(new Text(node_rank[0]), new Text("rank:" + node_rank[1]));
		}
	}
}