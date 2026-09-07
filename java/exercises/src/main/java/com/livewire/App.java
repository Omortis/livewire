package com.livewire;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;

public class App {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        Equipment[] equipment = mapper.readValue(
            new File("src/main/resources/equipment.json"), 
            Equipment[].class
        );
        
        for (Equipment e : equipment) {
            System.out.println(e.id + " " + e.voltage_kv);
        }
    }
}