package edu.stevens.cs549.hadoop.pagerank;

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class JoinReducer extends Reducer < Text, Text, Text, Text > {
	public void reduce(Text key, Iterable < Text > values, Context context) throws IOException, InterruptedException,IllegalArgumentException {
		Iterator <Text> iterator = values.iterator();
		String node_name = "";
		String rank = "";

		while (iterator.hasNext()) {
			String tmp = iterator.next().toString();
			if (tmp.startsWith("name:")) {
				node_name = tmp.replaceAll("name:", "");
			}
			if (tmp.startsWith("rank:")) {
				rank = tmp.replaceAll("rank:", "");
			}
		}

		context.write(new Text(key + "+" + node_name), new Text(rank));
	}
}