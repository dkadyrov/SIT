package edu.stevens.cs549.dhts.main;

import org.glassfish.jersey.server.ResourceConfig;

public class Application extends ResourceConfig {
    public Application() {
        packages("edu.stevens.cs549.dhts.resource");
    }
}
