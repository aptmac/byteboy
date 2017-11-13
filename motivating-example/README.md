# Motivating Example

## Description

This folder contains three files:
- One Java file (InfLoop.java)
- Two Byteman Scripts

This example is a simplified version of a potential situation some code may experience. 
```InfLoop.java``` has two methods: 
1. ```doWork()``` // represents the entry point for doing work
2. ```work()``` // represents an operation the object may want to perform

The main method creates an InfLoop object, calls ```doWork()``` and passes the value 0 to commence operations, and then the program gets stuck in an infinite loop.

The two Byteman scripts that are included contain rules to verify the program is still in execution (01-detectloop.btm) and exit the loop (02-stopinfloop.btm).

## Instructions

1. Use the Java compiler to convert the .java file into a .class file</br>
``` javac InfLoop.java ```

2. Run the InfLoop program to see what is (or isn't) going on. Use <ctrl+c> to exit.</br>
``` java InfLoop ```

3. Run the InfLoop program again, this time using the 01-detectloop.btm Byteman Script.</br>
``` java -javaagent:PATH_TO_BYTEMAN_HOME/lib/byteman.jar=script:01-detectloop.btm InfLoop ```

4. Run the InfoLoop program again, this time using the 02-stopinfloop.btm Byteman Script.</br>
``` java -javaagent:PATH_TO_BYTEMAN_HOME/lib/byteman.jar=script:02-stopinfloop.btm InfLoop ```

## Results

Like many bugs in code, running InfLoop won't explicitly tell the user that it's stuck in execution. 
Instead, nothing is printed to the console, and the user is left to figure out what is (or isn't) going on inside the program.
With this in mind, ```01-detectloop.btm``` can be loaded using Byteman, and will verify that the program is still in execution.
The ```01-detectloop.btm``` contains two rules:
1. RULE Traceln when starting work
2. RULE Traceln when stopping work
Both of these rules explicitly target the InfLoop class, and work method. 
When loaded using Byteman, these rules allow the program to output a line of text to the console every time ```work()``` is entered and exited.
Using this rule, the user can now be certain that there is a bug somewhere in the code that is causing ```work()``` to be called infinitely.</br>

Now that the user knows something about the execution state of the program, they can (if the application is open-sourced) dig through the codebase and narrow-down the point of error.
In this example, ```doWork()``` will only continue to loop if it was passed the value of 0. ```02-stopinfloop.btm``` contains a Byteman rule that targets ```doWork()``` and changes the value of the passed value to be 1.
This prevents the loop from starting, and will result in a program that exits safely.

## Tips for Setting Up Byteman

- Download the latest Byteman releases from [http://byteman.jboss.org/downloads.html]()
- Alternatively, Byteman can be downloaded from it's [GitHub repository](https://github.com/bytemanproject/byteman)

- It can be helpful to set-up environment variables for Byteman<br>
``` export BYTEMAN_HOME={PATH_TO_BYTEMAN} ```<br>
``` export PATH=${PATH}:${BYTEMAN_HOME}/bin ```

- The simplest usage of Byteman would be running it as a Java agent, and and attaching the script while running the program:<br> 
``` java -javaagent=${BYTEMAN_HOME}/lib/byteman.jar=script:[BYTEMAN_SCRIPT] <Java Program>```<br>