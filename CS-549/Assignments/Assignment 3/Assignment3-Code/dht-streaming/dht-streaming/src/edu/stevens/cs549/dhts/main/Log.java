package edu.stevens.cs549.dhts.main;

import java.util.logging.Logger;

public class Log {
	
	private static Logger logger = Logger.getLogger(Log.class.getCanonicalName());
	
	private static boolean logging = false;
	
	public static void setLogging(boolean l) {
		logging = l;
	}
	
	public static void setLogging() {
		logging = !logging;
	}
	
	public static synchronized void info(String mesg) {
		if (logging) {
			logger.info("[LT = " + Time.getTime() + "] " + mesg);
		}
	}
	
}
