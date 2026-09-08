package com.livewire;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        try (BufferedReader reader = Files.newBufferedReader(Paths.get("src/main/resources/scada.csv"));
                BufferedWriter writer = Files.newBufferedWriter(Paths.get("src/main/resources/scada_clean.csv"))) {

            String header = reader.readLine(); // Read header
            writer.write(header); // Write header to output
            writer.newLine();

            String line;
            int imputedCount = 0;
            while ((line = reader.readLine()) != null) {
                String[] values = line.split(",");
                float voltage = Float.parseFloat(values[1]); // values[1] = voltage column

                if (voltage >= 0.95 && voltage <= 1.05) {
                    writer.write(line);
                    writer.newLine();
                } else {
                    imputedCount++;
                }
            }
            System.out.println("Rejected " + imputedCount + " rows");
        } catch (IOException e) {
            System.err.println("ERROR: " + e.getClass().getSimpleName() + " - " + e.getMessage());
        }
    }
}