#!/usr/bin/python3

# analysis.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys
import subprocess

def run_analysis(java_file_path):
    """returns a .txt file with analysis details for interactive"""
    # Runs the profiler on the provided java class
    # ranked methods by time (5 to 10)
    # Need its method name, CPU usage,  arguments, argmuent types, whats calling it (stack trace),
    # TODO: figure out argument/agrument types
    if os.path.exists(java_file_path):        
        # check to see if it is a relative path or if there is something there already
        fullpath =  os.path.realpath(java_file_path)  
        print "Analyzing..."
        flags = " -agentlib:hprof=cpu=times -classpath " + os.path.dirname(fullpath) + " " + os.path.basename(fullpath)
        # look into subprocesses for refactoring!
        os.system("java -agentlib:hprof=cpu=times -classpath " + os.path.dirname(fullpath) + " " + os.path.basename(fullpath))
        # Reads in the results, dumps some of it to the console
        results = open("./java.hprof.txt", "r")
        for line in results:
            if "rank " in line:
                for entry in results:
                    entrysplit =entry.split()
                    print "test"
                    print entrysplit

    else:
        print ("Java file does not exist.")
