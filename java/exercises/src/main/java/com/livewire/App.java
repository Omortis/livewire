package com.livewire;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class App {
    public static void main(String[] args) {
        // Use command-line arg if provided, otherwise default to logs directory
        String dirPath = args.length > 0 ? args[0] : "src/main/resources/logs";
        
        int totalAlarms = 0;
        
        // Files.walk() returns a Stream<Path> that must be closed (try-with-resources)
        try (Stream<Path> paths = Files.walk(Paths.get(dirPath))) {
            
            totalAlarms = paths
                .filter(Files::isRegularFile)           // Only files, not directories
                .filter(p -> p.toString().endsWith(".log"))  // Only .log files
                .mapToInt(App::countAlarmsInFile)       // Count ALARM lines per file
                .sum();                                 // Sum across all files
                
        } catch (IOException e) {
            System.err.println("ERROR: " + e.getClass().getSimpleName() + " - " + e.getMessage());
            System.exit(1);
        }
        
        System.out.println("Total ALARM count: " + totalAlarms);
    }
    
    /**
     * Counts lines containing the word "ALARM" in a single file.
     * Uses try-with-resources to ensure the file stream is closed.
     */
    private static int countAlarmsInFile(Path filePath) {
        try (Stream<String> lines = Files.lines(filePath)) {
            return (int) lines.filter(line -> line.contains("ALARM")).count();
        } catch (IOException e) {
            System.err.println("ERROR reading " + filePath + ": " + e.getMessage());
            return 0;
        }
    }
}
