package edu.stevens.cs549.hadoop.pagerank;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.URI;
import java.util.HashMap;
import java.util.Map;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class PageRankDriver {
	
	public static final double DECAY = 0.85;
		
	public static void main(String[] args) throws Exception {
		long startTime = System.currentTimeMillis();
		String job = "";
		if (args.length != 0) // Checks if there is no input
			job = args[0];
		if (args.length == 4) // If the number of input arguments is 4
		{

			if (job.equals("init")) // Checks the first arguments for a match
									// with each of the function names
			{
				init(args[1], args[2], Integer.parseInt(args[3])); 
				// Sends data to the functions
			} else if (job.equals("iter")) {
				iter(args[1], args[2], Integer.parseInt(args[3]));
			} else if (job.equals("finish")) {
				finish(args[1], args[2], Integer.parseInt(args[3]));
			} else // In case the function name doesn't match up
			{
				System.err
						.println("Please check the name of the function you wish to call and try again");
			}
		} else if (args.length == 5) // If number of input arguments is 5
		{
			if (job.equals("diff")) // And the first argument == "diff"
			{
				diff(args[1], args[2], args[3], Integer.parseInt(args[4])); 
				// Parses data to diff
			} else // In case the function name doesn't match up
			{
				System.err
						.println("Please check the name of the function you wish to call and try again");
			}
		} else if (args.length == 7) // If number of input arguments is 7 and
										// first input is == "composite"; parses
										// data to composite
		{
			if (job.equals("composite")) {
				composite(args[1], args[2], args[3], args[4], args[5],
						Integer.parseInt(args[6]));
			} else // In case the function name doesn't match up
			{
				System.err
						.println("Please check the name of the function you wish to call and try again");
			}
		} else {
			System.err
					.println("Incorrect Usage \n Correct format: <function name><input><output><#reducers> \n Or \n <function name><input><output><diff><#reducers>"
							+ "\n Or \n <function name><input><output><interim1><interim2><diff><#reducers>");
		}

		long endTime = System.currentTimeMillis();
		System.out.println("Time consuming:"+ (endTime-startTime)/1000+ "s");
	}

	static void init(String input, String output, int reducers)
			throws IOException, ClassNotFoundException, InterruptedException {
		System.out.println("Init Job Started");
		Job job = Job.getInstance(); // Creates a new Job
		job.setJarByClass(PageRankDriver.class); // Sets the Driver class
		job.setNumReduceTasks(reducers); // Sets the number of reducers

		// Adds input and output paths
		FileInputFormat.addInputPath(job, new Path(input)); 
		FileOutputFormat.setOutputPath(job, new Path(output));

		// Initializes the Mapper and Reducer Classes
		job.setMapperClass(InitMapper.class); 
		job.setReducerClass(InitReducer.class);

		// Sets the input output types for the Mapper and Reducer
		job.setMapOutputKeyClass(Text.class); 
		job.setMapOutputValueClass(Text.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		// Prints message on successful completion or in case of an error
		System.out.println(job.waitForCompletion(true) ? "Init Job Completed" : "Init Job Error");
	}

	static void iter(String input, String output, int reducers)
			throws IOException, ClassNotFoundException, InterruptedException {
		System.out.println("Iter Job Started");
		Job job = Job.getInstance(); // Creates a new Job
		job.setJarByClass(PageRankDriver.class); // Sets the Driver class
		job.setNumReduceTasks(reducers); // Sets the number of reducers

		// Adds input and output paths
		FileInputFormat.addInputPath(job, new Path(input)); 
		FileOutputFormat.setOutputPath(job, new Path(output));

		// Sets the Mapper and Reducer classes
		job.setMapperClass(IterMapper.class); 
		job.setReducerClass(IterReducer.class);

		// Sets the Mapper and Reducer output types
		job.setMapOutputKeyClass(Text.class); 
		job.setMapOutputValueClass(Text.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		// Prints message on successful completion or in case of an error
		System.out.println(job.waitForCompletion(true) ? "Iter Job Completed" : "Iter Job Error");

	}

	static void diff(String input1, String input2, String output, int reducers)
			throws Exception {
		System.out.println("Diff Job Part 1 Started");
		
		Job job = Job.getInstance(); // Creates a new job
		job.setJarByClass(PageRankDriver.class); // Sets Driver Class
		job.setNumReduceTasks(reducers); // Sets number of reducers

		FileInputFormat.addInputPath(job, new Path(input1)); // Adds input from one interim output
		FileInputFormat.addInputPath(job, new Path(input2)); // Adds input from another interim output
		FileOutputFormat.setOutputPath(job, new Path("tempdiff")); // Adds a temporary output folder "tempdiff"

		job.setMapperClass(DiffMap1.class); // Sets Mapper and Reducer class for first job
		job.setReducerClass(DiffRed1.class);

		job.setMapOutputKeyClass(Text.class); // Sets output classes for Mapper and Reducers for Job 1
		job.setMapOutputValueClass(Text.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		if (job.waitForCompletion(true)) // Once the first job completes
		{
			System.out.println("Diff Part 1 Complete, Part 2 Started");
			Job job1 = Job.getInstance(); // Creates a new second job
			job1.setJarByClass(PageRankDriver.class); // Sets driver class and number of reducers
			job1.setNumReduceTasks(reducers);

			FileInputFormat.addInputPath(job1, new Path("tempdiff")); 
			// Adds the temporary directory "tempdiff" as input
			FileOutputFormat.setOutputPath(job1, new Path(output)); // Sets output

			job1.setMapperClass(DiffMap2.class); // Sets Mapper and Reducer classes for second job
			job1.setReducerClass(DiffRed2.class);

			job1.setMapOutputKeyClass(Text.class); // Sets output class for second job
			job1.setMapOutputValueClass(Text.class);

			job1.setOutputKeyClass(Text.class);
			job1.setOutputValueClass(Text.class);

			// If Job is completed, prints message, else prints an error
			System.out
					.println(job1.waitForCompletion(true) ? "Diff Job Completed"
							: "Diff Job Error");
			deleteDirectory("tempdiff"); // Deletes the temporary directory "tempdiff"
		}

	}
	
	static void finish(String input, String output, int reducers) throws Exception {
		finishJoin(input, output, reducers);
		
		// Exits once job finishes.
		deleteDirectory(input); // Deletes the input directory
	}
	
	static void finishJoin(String input, String output, int reducers)
			throws Exception {
		String tempJoinFolder = "tempJoin";
		System.out.println("Finish Join Job Started");
		Job job = Job.getInstance(); // Creates a new Job
		job.setJarByClass(PageRankDriver.class); // Sets the Driver class
		job.setNumReduceTasks(reducers); // Sets the number of reducers

		FileInputFormat.addInputPath(job, new Path(input)); // Adds input and output paths
		FileOutputFormat.setOutputPath(job, new Path(tempJoinFolder));
		
		job.setMapperClass(JoinMapper.class); // Sets Mapper and Reducer Classes
		job.setReducerClass(JoinReducer.class);

		job.setMapOutputKeyClass(Text.class); // Sets Mapper and Reducer output types
		job.setMapOutputValueClass(Text.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		// Prints message on successful completion or error.
		if(job.waitForCompletion(true)) {
			finishCombine(tempJoinFolder, output, reducers);
		}
	}


	static void finishCombine(String input, String output, int reducers)
			throws Exception {
		System.out.println("Finish Join Job end, and Finish Job Started");
		Job job = Job.getInstance(); // Creates a new Job
		job.setJarByClass(PageRankDriver.class); // Sets the Driver class
		job.setNumReduceTasks(reducers); // Sets the number of reducers

		FileInputFormat.addInputPath(job, new Path(input)); // Adds input and output paths
		FileOutputFormat.setOutputPath(job, new Path(output));

		job.setMapperClass(FinMapper.class); // Sets Mapper and Reducer Classes
		job.setReducerClass(FinReducer.class);

		job.setMapOutputKeyClass(DoubleWritable.class); // Sets Mapper and Reducer output types
		job.setMapOutputValueClass(Text.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		// Prints message on successful completion or error.
		System.out.println(job.waitForCompletion(true) ? "Finish Job Completed" : "Finish Job Error");
		// Exits once job finishes.
//		deleteDirectory(CURRENT_PATH + "/tempJoin"); // Deletes the input directory
		deleteDirectory("tempJoin"); // Deletes the input directory

	}

	public static void composite(String input, String output, String interim1,
			String interim2, String diff, int reducers) throws Exception {
		/*
		 * TODO 
		 */
		System.out.println("Daniel Kadyrov (10455680)");
		
		int counter = 0;
		init(input, interim1, reducers); // Initializes data
		counter++;
		double difference = 100000000; // sets ridiculously large default difference
		int i = 0; // counter variables
		while (difference >= 400) // continues operation till difference is of specified value
		{
			if (i % 2 == 0) {
				iter(interim1, interim2, reducers); 
				/*
				 * or every even iteration, interim1 is the input and interim2 the output
				 */
			} else {
				iter(interim2, interim1, reducers); 
				// For odd iterations it is swapped
			}
			if (i % 3 == 0) // for every 3 iterations calculates the difference
			{
				counter++;
				diff(interim1, interim2, "diffout", reducers); 
				/*
				 * as difference is an absolute value, order of input1, input2 directories doesn't matter
				 */
				difference = readDiffResult("diffout"); // Reads difference from "diffout"
				System.out.println("Difference updates to:" + difference);
				deleteDirectory("diffout"); // deletes diffout
			}

			if (i % 2 == 0) // on even iterations, delete input directory interim1
			{
				deleteDirectory(interim1);
			}
			if (i % 2 == 1) // on odd, delete interim2
			{
				deleteDirectory(interim2);
			}
			counter++;
			i++; // increment i
		}

		if (i % 2 == 1) // As i increments at the last step, for odd i, interim2
						// is the input directory
		{
			deleteDirectory(interim1); // deletes other directory
			counter++;
			finish(interim2, output, reducers);
			summarizeResult(output);
		} else // for even i, interim1 is the input directory
		{
			deleteDirectory(interim2); // Deletes other directory
			counter++;
			finish(interim1, output, reducers);
			summarizeResult(output);
		}
		System.out.println();
		System.out.println(counter);

	}

	/*
	 * Given an output folder, takes the first 10 (if available) lines from each
	 * output file from finish and sorts them in rank descending order.
	 */
	static void summarizeResult(String path) throws Exception {
		Path finpath = new Path(path); // Creates new Path
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(URI.create(path), conf);
		HashMap<Long, Double> values = new HashMap<Long, Double>(); 
		Map<Long, String> node_names = new HashMap<Long, String>();
		// HashMap to store Node, Rank Pairs
		int size = 0;

		if (fs.exists(finpath)) {
			FileStatus[] ls = fs.listStatus(finpath);
			for (FileStatus file : ls) {
				if (file.getPath().getName().startsWith("part-r-00")) {
					FSDataInputStream diffin = fs.open(file.getPath());
					BufferedReader d = new BufferedReader(new InputStreamReader(diffin));
					int i = 0;
					String diffcontent = "x"; // Initializes string to random value
					while (i <= 10 && diffcontent != null) // Adds only 10 values max. per file
					{
						diffcontent = d.readLine();
						if (diffcontent != null) // Adds new value as long as value exists
						{
							String[] parts = diffcontent.split("\t");
							String[] sections = parts[0].split("\\+");
							long node = Long.parseLong(sections[0]);
							String node_name = "0";
							if(sections.length > 1) {
								node_name = sections[1];
							}
							
							double rank = Double.parseDouble(parts[1]);
							values.put(node, rank);
							node_names.put(node, node_name);
							i++;
							size++; // Counter to calculate size of HashMap
						}
					}
					d.close();
				}
			}
			Long[] nodes = new Long[size];
			Double[] ranks = new Double[size];
			int j = 0;
			for (Map.Entry<Long, Double> entry : values.entrySet())
				/*
				 *  Iterates over set and stores values in arrays
				 */
			{
				nodes[j] = entry.getKey();
				ranks[j] = entry.getValue();
				j++;
			}

			for (int i = 0; i < j - 1; i++) // Simple linear sort to order the
											// nodes in reducing rank order
			{
				for (int k = i + 1; k < j; k++) {
					if (ranks[i] < ranks[k]) {
						double temp = ranks[i]; // swaps
						ranks[i] = ranks[k];
						ranks[k] = temp;

						Long temps = nodes[i]; // swaps
						nodes[i] = nodes[k];
						nodes[k] = temps;
					}
				}
			}

			try {
				OutputStream os = fs.create(new Path(path + "/output.txt")); 
				/*
				 * Creates new file output.txt
				 */
				for (int i = 0; i < nodes.length && i < 50; i++) {
					String out = nodes[i] + ":" + node_names.get(nodes[i]) + "\t" + ranks[i] + "\n"; 
					/*
					 *  Print out node rank pairs
					 */
					for (int k = 0; k < out.length(); k++) {
						// Writes characters one by one to the output stream
						char c = out.charAt(k);
						os.write(c); 
					}
				}
				os.close(); // Closes the writer
				Job job = Job.getInstance();
				job.addCacheFile(new Path(path).toUri());
			} catch (IOException e) {
				System.out.println("Any Errors:");
				e.printStackTrace();
			}
		}
		System.out.println();
		System.out.println("Results Summarized");

		fs.close();
	}

	/*
	 * Given an output folder, returns the first double from the first part-r-00000 file
	 */
	static double readDiffResult(String path) throws Exception {
		double diffnum = 0.0;
		Path diffpath = new Path(path);
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(URI.create(path), conf);

		if (fs.exists(diffpath)) {
			FileStatus[] ls = fs.listStatus(diffpath);
			for (FileStatus file : ls) { // Modified file to support multiple reducer output files.
				if (file.getPath().getName().startsWith("part-r-00")) {
					FSDataInputStream diffin = fs.open(file.getPath());
					BufferedReader d = new BufferedReader(
							new InputStreamReader(diffin));
					String diffcontent = d.readLine();
					if (diffcontent != null) {
						double diff_temp = Double.parseDouble(diffcontent);
						if (diffnum < diff_temp) {
							diffnum = diff_temp;
						}
					}
					diffin.close();
					d.close();
				}
			}
		}

		fs.close();
		return diffnum;
	}

	static void deleteDirectory(String path) throws Exception {
		Path todelete = new Path(path);
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(URI.create(path), conf);

		if (fs.exists(todelete))
			fs.delete(todelete, true);

		fs.close();
	}
}