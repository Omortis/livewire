package com.livewire;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

class Equipment {
    public String id;
    public String type;
    public Double voltage_kv;

    public Equipment(String id, String type, Double voltage) {
        this.id = id;
        this.type = type;
        this.voltage_kv = voltage;
    }

    public String toString() {
        return "id = " + id + ", type = " + type + ", voltage_kv = " + voltage_kv;
    }
}

class EquipmentRegistry<T> {
    List<T> registry = new ArrayList<>();

    public void add(T item) {
        registry.add(item);
    }
    
    public List<T> findBy(Predicate<T> filter) {
        List<T> result = new ArrayList<>();
        for (T item : registry) {
            if (filter.test(item)) {
                result.add(item);
            }
        }
        return result;
    }
}

public class App {
    public static void main(String[] args) {
        EquipmentRegistry<Equipment> registry = new EquipmentRegistry<>();

        registry.add(new Equipment("eq1", "thermal", 55.0));
        registry.add(new Equipment("eq2", "coal", 60.0));
        registry.add(new Equipment("eq3", "solar", 40.0));
        registry.add(new Equipment("eq4", "nuclear", 70.0));
        registry.add(new Equipment("eq5", "wind", 30.0));

        List<Equipment> highVoltage = registry.findBy(e -> e.voltage_kv > 50);

        for (Equipment equipment : highVoltage) {
            System.out.println(equipment);
        }
    }
}