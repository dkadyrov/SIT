package edu.stevens.cs549.dhts.main;

public class Time {

	/*
	 * Logical time.
	 */
	private static long time = 0;
	
	public static synchronized long getTime() {
		return time;
	}
	
	/*
	 * Advance time on a send:
	 */
	public static synchronized long advanceTime() {
		return ++time;
	}
	
	/*
	 * Advance time on a receive:
	 */
	public static synchronized long advanceTime(long timestamp) {
		time = Math.max(timestamp, time) + 1;
		return time;
	}

	public static final String TIME_STAMP = "timestamp";

}
