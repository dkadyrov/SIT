package edu.stevens.cs549.dhts.activity;

public class UriApi {
    public static String INFO = "/info";
    public static String FIND_SUCCESSOR = "/find?id=%s";
    public static String SUCC = "/succ";
    public static String PRED = "/pred";
    public static String GET_KEY_VALUE = "?key=%s";
    public static String SET_KEY_VALUE = "?key=%s&val=%s";
    public static String DELETE_KEY_VALUE = "?key=%s&val=%s";
    public static String NOTIFY = "/notify";
    public static String GET_NODE_BY_FINGER = "/finger?id=%s";
    public static String LISTEN = "/listen?id=%s&key=%s";

}
