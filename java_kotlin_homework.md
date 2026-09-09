# Java / Kotlin Homework Exercises

> **Instructions**: Complete the exercises below. For each exercise, create a standalone CLI application. When you are ready, share your code and I will review it.
>
> **Note**: These exercises assume you are proficient in systems programming but new to (or rusty on) Java and Kotlin. Each section includes brief explanations of modern JVM concepts.

---

## Introduction: JVM Basics for Power Systems

**Java 17+ (LTS)**: Power utilities are conservative technology adopters. Java 17 is the current Long-Term Support (LTS) release widely used in enterprise integration buses, SCADA middleware, and CIM data exchange platforms. It adds records, sealed classes, pattern matching for switch, and improved NIO.

**Kotlin**: A modern JVM language that interoperates fully with Java. Increasingly adopted for new components in power system integration stacks. Kotlin emphasizes null safety, coroutines for async I/O, and concise data class definitions — all useful when modeling SCADA data streams and equipment configurations.

**Maven vs Gradle**: Maven uses XML-based `pom.xml` and is the traditional build tool in conservative enterprise environments (many power system Java libraries publish to Maven Central). Gradle uses a Groovy/Kotlin DSL and is the standard build tool for Kotlin projects.

**Build a Java project with Maven:**
```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=exercise -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd exercise
mvn compile exec:java -Dexec.mainClass="com.example.App"
```

**Build a Kotlin project with Gradle:**
```bash
gradle init --type kotlin-application --dsl kotlin --project-name exercise
cd exercise
gradle run
```

---

## 1. Java

Use **Maven** for all Java exercises. Target **Java 17+**. Each exercise should be a runnable `main` class.

### Exercise 1.1: Hello Power System
Create a Maven project that prints `"System online: Grid Monitor v1.0"` to stdout. Include a `pom.xml` with Java 17 as the compiler target. Run it with `mvn compile exec:java`.

*Note: This is just to verify your Maven toolchain works before we introduce libraries.*

**Your Answer**:
```java
package com.livewire;

public class App {
    public static void main(String[] args) {
        System.out.println("System online: Grid Monitor v1.0");
    }
}
// Output:
// System online: Grid Monitor v1.0
// [INFO] ------------------------------------------------------------------------
// [INFO] BUILD SUCCESS
// [INFO] ------------------------------------------------------------------------
// [INFO] Total time:  1.452 s
// [INFO] Finished at: 2026-09-07T15:26:04-04:00
// [INFO] ------------------------------------------------------------------------
```

---

### Exercise 1.2: Parse Equipment JSON
Read a JSON file `equipment.json` containing an array of substation equipment objects with fields `id`, `type`, `voltage_kv`, and `status`. Print each object's `id` and `voltage_kv` to stdout, one per line. Use **Jackson** (`com.fasterxml.jackson.core:jackson-databind`) as the JSON parser.

*Note: JSON is the modern lingua franca for configuration exchange. CIM/CGMES data and IEC 61850 SCL configurations are increasingly serialized as JSON in integration layers.*

Sample `equipment.json`:
```json
[
  {"id": "T1", "type": "Transformer", "voltage_kv": 138.0, "status": "active"},
  {"id": "B1", "type": "Bus", "voltage_kv": 13.8, "status": "active"}
]
```

**Your Answer**:
```java
// Equipment.java
package com.livewire;

public class Equipment {
    public String id;
    public String type;
    public double voltage_kv;
    public String status;
}

// App.java
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
// Output:
// T1 138.0
// B1 13.8
// [INFO] BUILD SUCCESS
// [INFO] Total time: 0.316 s

```

---

### Exercise 1.3: SCADA CSV ETL
Read a CSV file `scada.csv` with headers `timestamp,voltage,power,frequency`. Filter out rows where `voltage` is outside the range 0.95–1.05 (per-unit). Write the filtered rows to `scada_clean.csv` with the same header. Use only the **Java standard library** (`java.nio.file`, `BufferedReader`, `BufferedWriter`, `String.split`). No external CSV libraries.

*Note: SCADA systems stream millions of measurements per day. Simple ETL pipelines — filter, validate, and write — are the first step before data reaches the analytics engine.*

Sample `scada.csv`:
```csv
timestamp,voltage,power,frequency
2024-01-01T00:00,0.98,120.5,60.01
2024-01-01T00:01,0.92,115.0,60.02
```

**Your Answer**:
```java
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

// Output:
// Rejected 1 rows
// [INFO] ------------------------------------------------------------------------
// [INFO] BUILD SUCCESS
// [INFO] ------------------------------------------------------------------------
// --> ./src/main/resources
// ❯ cat scada_clean.csv
// timestamp,voltage,power,frequency
// 2024-01-01T00:00,0.98,120.5,60.01
```

---

### Exercise 1.4: Interface-Based Solver
Define a Java interface `PowerFlowSolver` with a single method `solve(double[] injections)` that returns `double[]`. Create two implementations: `DcSolver` (returns the input array unchanged as a trivial DC approximation) and `AcSolver` (returns the input multiplied by 0.95 to simulate AC losses). In `main`, create a `List<PowerFlowSolver>`, add both solvers, iterate over them, and print the result of each solver for the input `[1.0, -0.5, -0.5]`.

*Note: Interface-driven design is the standard pattern in power system Java middleware. CIM adapters, IEC 61850 clients, and market interfaces all use this polymorphism pattern.*

**Your Answer**:
```java
package com.livewire;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

interface PowerFlowSolver {
    double[] solve(double[] injections);
}

class DcSolver implements PowerFlowSolver {
    public double[] solve(double[] injections) {
        return injections; // trivial pass-through
    }
}

class AcSolver implements PowerFlowSolver {
    public double[] solve(double[] injections) {
        double[] result = new double[injections.length];
        for (int i = 0; i < injections.length; i++) {
            result[i] = injections[i] * 0.95;
        }
        return result;
    }
}

public class App {
    public static void main(String[] args) {
        List<PowerFlowSolver> solvers = new ArrayList<>();
        solvers.add(new DcSolver());
        solvers.add(new AcSolver());
        
        double[] input = {1.0, -0.5, -0.5};
        
        for (PowerFlowSolver solver : solvers) {
            System.out.println(
                solver.getClass().getSimpleName() + ": " + 
                Arrays.toString(solver.solve(input))
            );
        }
    }
}

// Output:
// [INFO] --- exec:3.6.3:java (default-cli) @ exercises ---
// DcSolver: [1.0, -0.5, -0.5]
// AcSolver: [0.95, -0.475, -0.475]
// [INFO] ------------------------------------------------------------------------
// [INFO] BUILD SUCCESS
// [INFO] ------------------------------------------------------------------------
```

---

### Exercise 1.5: Generics and Equipment Registry
Create a generic class `EquipmentRegistry<T>` that stores items in a `List<T>` and provides methods `add(T item)` and `List<T> findBy(Predicate<T> filter)`. In `main`, instantiate `EquipmentRegistry<Equipment>` (where `Equipment` is a simple class with `id`, `type`, `voltage_kv`), add 5 items, and print all equipment with `voltage_kv > 50` using `findBy`.

*Note: Generic collections and lambda filters are the bread and butter of CIM object registries and substation asset databases in Java integration layers.*

**Your Answer**:
```java
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

// Output:
// [INFO] --- exec:3.6.3:java (default-cli) @ exercises ---
// id = eq1, type = thermal, voltage_kv = 55.0
// id = eq2, type = coal, voltage_kv = 60.0
// id = eq4, type = nuclear, voltage_kv = 70.0
// [INFO] ------------------------------------------------------------------------
// [INFO] BUILD SUCCESS
// [INFO] ------------------------------------------------------------------------
```

---

### Exercise 1.6: NIO File Walker and Log Analyzer
Use `java.nio.file.Files.walk()` to recursively find all `.log` files in a given directory. For each file, count lines containing the word `"ALARM"`. Print the total alarm count across all files. Accept the directory path as a command-line argument.

*Note: SCADA and substation automation systems generate massive log volumes. NIO.2 (Java 7+) is the modern standard for high-performance file traversal.*

**Your Answer**:
```java
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
                .filter(p -> p.toString().endsWith(".log"))
                .mapToInt(App::countAlarmsInFile)
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

// Output:
// [INFO] --- exec:3.6.3:java (default-cli) @ exercises ---
// Total ALARM count: 8
// [INFO] BUILD SUCCESS
```

---

## 2. Kotlin

Use **Gradle with Kotlin DSL** for all Kotlin exercises. Target **Java 17+ runtime**. Each exercise should be a runnable `main` function.

### Exercise 2.1: Hello Kotlin Grid
Create a Gradle Kotlin project that prints `"System online: Kotlin Grid Monitor v1.0"`. Use the Gradle Kotlin DSL (`build.gradle.kts`). Run it with `gradle run`.

*Note: This verifies your Gradle/Kotlin toolchain before adding dependencies.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

### Exercise 2.2: Data Classes and Null Safety
Define a Kotlin data class `Breaker(val id: String, val status: String, val currentAmps: Double?)`. Create a list of 5 breakers where one has `currentAmps = null`. Use the Elvis operator (`?:`) to print `"No reading"` for null values, otherwise print the current rounded to one decimal. Use Kotlin's `List.filterNotNull()` extension to count how many breakers have a valid current reading.

*Note: Null safety is Kotlin's killer feature. SCADA data often has missing measurements (nulls), and Kotlin's type system forces explicit handling — eliminating an entire class of NPE bugs common in Java SCADA middleware.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

### Exercise 2.3: Collection DSL for Load Profiles
Given a list of hourly load readings `List<Double>` (24 values), use Kotlin collection functions (`filter`, `map`, `average`, `max`) to compute: (1) average load, (2) peak load, (3) number of hours above 500 MW, and (4) a new list of loads normalized to per-unit using a 1000 MVA base. Print all four results.

*Note: Kotlin's collection DSL is far more concise than Java streams. Power analytics pipelines — load profiling, generation forecasting — benefit from this expressiveness.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

### Exercise 2.4: Coroutines for Async SCADA Polling
Simulate polling three different SCADA data sources concurrently. Use Kotlin coroutines (`kotlinx.coroutines`) to launch three async tasks, each waiting 100ms and then returning a random `Double` (0.95–1.05) representing a voltage reading. Use `async`/`await` to collect all three results, then print the average. Run with `Dispatchers.Default`.

*Note: Coroutines are Kotlin's answer to async I/O. In real SCADA integration, a Kotlin service might concurrently poll hundreds of IEC 61850 or DNP3 devices. This exercise simulates the concurrency pattern without requiring network access.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

### Exercise 2.5: Sealed Classes for Message Types
Define a sealed class `ScadaMessage` with subclasses `AnalogValue(val value: Double)`, `DigitalStatus(val state: Boolean)`, and `Alarm(val severity: Int)`. Write a function `handleMessage(msg: ScadaMessage): String` that uses a `when` expression (Kotlin's pattern matching) to return: `"Analog: $value"` for analogs, `"Status: $state"` for digital, and `"Alarm level $severity"` for alarms. Create one of each message type in `main` and print the handler result.

*Note: Sealed classes (Kotlin 1.5+) are the modern replacement for visitor patterns in Java. They are ideal for protocol state machines — e.g., IEC 61850 message types or DNP3 function codes — where exhaustiveness is critical.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

### Exercise 2.6: Extension Functions and ETL Pipeline
Create an extension function `List<Double>.normalize(base: Double): List<Double>` that divides each element by the base. Create another extension function `List<Double>.movingAverage(window: Int): List<Double>` that computes a simple moving average. In `main`, generate a list of 24 hourly load values, normalize to per-unit (base 1000), compute a 3-hour moving average, and print both results.

*Note: Extension functions let you add domain-specific operations to standard collections without inheritance. This is heavily used in Kotlin analytics libraries for power system time-series processing.*

**Your Answer**:
```kotlin
// Paste your Kotlin code here
```

---

## Submission Notes

- Each exercise should be a standalone, runnable project (Maven for Java, Gradle for Kotlin).
- Include sample data files (JSON, CSV) where the exercise requires reading from disk.
- When you are ready for review, copy the code for the exercises you want me to check and paste it into the chat, or point me to the project directory.
- I will review your solutions for correctness, idiomatic style, and adherence to Java 17+ / Kotlin best practices.

## Additional Resources

- **IEC 61850 Java Stack**: [IEC61850bean / OpenIEC61850](https://www.beanit.com/iec-61850/) — open-source Java MMS client/server (Maven: `com.beanit:iec61850bean`)
- **CIM/CGMES Java Tools**: [RDF4J](https://rdf4j.org/) for CIM RDF/XML processing, [JAXB](https://javaee.github.io/jaxb-v2/) for CIM XML binding
- **Kotlin Coroutines**: [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) — the standard async library
- **Jackson JSON**: [jackson-databind](https://github.com/FasterXML/jackson-databind) — the de facto JSON library for JVM
