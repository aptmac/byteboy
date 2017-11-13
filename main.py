#!/usr/bin/python3

# main.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys

def main(java_file):
    
    # Runs the profiler on the provided java class
    os.system("java -agentlib:hprof=cpu=times " + java_file)
    
    # Reads in the results, dumps some of it to the console
    results = open("./java.hprof.txt", "r").read()
    print(results[results.find("CPU TIME (ms)"):])

    # print command line arguments
    print("testing")
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    try:
        java_file = sys.argv[1]
        main(java_file)
    except IndexError:
        print("Invalid number of arguments supplied")
