# Java / Kotlin Homework Course

## Opencode / Sonnet Research Text

### My Question / Prompt

```
It would seem that Java and kotlin are used heavily in power generation system data exchange and maybe to interface with SCADA systems? Can you find any information to back this up?
```

### Your Answer

```
Yes, you're correct. Java is heavily used in power system data exchange and SCADA interfaces, particularly for:

IEC 61850 (Substation Automation)
- SmartGridware provides a Java SDK for implementing IEC 61850 compliant servers — the protocol used for SCADA/substation communication
- Java is used for MMS (Manufacturing Message Specification) stack implementation, which is the core transport for IEC 61850 data

CIM (Common Information Model) Data Exchange
- The CIM-61850 harmonization effort uses Java frameworks:
- JAXB for XML binding (CIM uses XML-based data exchange)
- RDF4J for querying CIM configuration files (RDF/XML format)
- MapStruct for mapping between CIM classes and IEC 61850 classes
- Kalkitech provides CIM-based integration platforms for SCADA, DMS, EMS, GIS systems using Java

Enterprise Integration
- Java web services (SOAP/XML) are commonly used for utility-to-utility data exchange (ICCP/TASE.2)
- Java frameworks handle message translation between CIM/XML, JSON, and IEC 61850 formats

Kotlin specifically: I didn't find explicit Kotlin references in power systems literature, but it's increasingly common in modern JVM-based enterprise applications. Many organizations that already use Java for IEC 61850/CIM are adopting Kotlin for newer components.
```

## Problem Statement

We need to create some homework exercises covering the following topics:

- Java system/API programming w/ light ETL
- Kotlin system/API programming w/ light ETL

## Guidelines

- These exercises should target a veteran system programmer (in Golang, Python, C#, etc) who has very little Java or Kotlin experience, or whose experience in both is quite dated (10+ years).
- Problems should be drawn from the SCADA/IEC61850 discussion above if and only if public libraries and SDKs are available for use.
- Difficulty should ramp up progressively within each topic. Exercises should be practical and reflect day-to-day analysis tasks at a power engineering firm.
- A mix of general programming/syntax exercises and power systems specific problems is encouraged.
- The exercises should be able to be completed in less than one day — nothing too terribly complex.
- Including sample data sets relevant to IEC61850 (or referencing same online) would be helpful to make the exercises realistic.
- Target MacOS or FreeBSD if OS-specific decisions are encountered.
- **Java target: Java 17+ (LTS)**. Power utilities are conservative adopters; Java 17 is the current enterprise sweet spot.
- **Build tools:** Maven for Java exercises, Gradle for Kotlin exercises.
- **Output format:** CLI applications that can be tested and run directly from the terminal.

## Document Format

The output should be a Markdown file generated in the local directory. Follow format and layout of the extant `python_homework.md` file in this repo.

## Exercise Solutions

There is no need to generate a set of solutions, but let's setup the Markdown such that I can ask you to review my answers and code.
