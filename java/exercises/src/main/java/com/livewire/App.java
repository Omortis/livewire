package com.livewire;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class App {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java App <directory>");
            return;
        }
        
        // TODO: Files.walk() with try-with-resources
        // TODO: Filter for .log files
        // TODO: For each file, Files.lines() and count "ALARM"
        // TODO: Sum across all files and print total
    }
}