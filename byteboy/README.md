# Byteboy

A Python application for analyzing Java code, and creating/generating Byteman scripts

## Usage

Run Byteboy on the command-line using:

``python byteboy.py <path/to/java_program>``

If the user decides not to supply a Java program, that is completely okay. They just won't be able to use the functionality that involves analysis; they'll be able to use the guided rule creation functionality only.

The specified Java program can be in either a .java format (and Byteboy will run javac), or a .class format.

## Functionality

Byteboy currently offers the following functionality:

- Program analysis of the provided Java application
- Manual Rule creation
- Semi-automatic rule creation using results of the analysis
- Automatic rule generation
  - Rules will focus on tracing application behaviour 
- Fuzz test rule generation using the results of the analysis
  - Rules will focus on altering function parameters in an attempt to find holes in current test implementations

## Output

Byteboy creates a folder called ``/output`` inside of this folder, which will house the created rules.

Rules created as a result of the manual and semi-automatic generators will allow the user to name the .btm files.

Rules created as a result of the fuzz test generator will be assigned a file name based on the behaviour of the rule.
