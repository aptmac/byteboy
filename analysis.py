#!/usr/bin/python3

# analysis.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys
import subprocess

def run_analysis(java_file_path):
    #HPROF ranking indexes

    TOTAL_RANKINGS = 5
    RANK   = 0
    SELF   = 1
    ACCUM  = 2
    COUNT  = 3
    TRACE  = 4
    METHOD = 5

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
        rankings = list()
        trace_search_list = list()

        for line in results:                
            if "rank " in line:
                #for entry in results:
                for index, entry in enumerate(results):
                    if (index < TOTAL_RANKINGS):
                        temp_list = entry.split()
                        trace_search_list.append("TRACE " + temp_list[TRACE] + ":") 
                        del temp_list[SELF]
                        rankings.append(temp_list)
                    else: break
        search_index = 0 
        results = open("./java.hprof.txt", "r")
        for line in results:
            print "searching for " + trace_search_list[search_index]
            if trace_search_list[search_index] in line:
                print "found at " + trace_search_list[search_index]
                for method in results:
                    if ("TRACE " not in method):
                        rankings[search_index].append(method)
                    else:
                        search_index += 1
                        print "increase search index"
                        break
        #print rankings
    else:
        print ("Java file does not exist.")
