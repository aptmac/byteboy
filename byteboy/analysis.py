#!/usr/bin/python

# analysis.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys
import subprocess
import re

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
    # ranked methods by time (5)
    # Need its method name, CPU usage,  arguments, argmuent types, and whats calling it (stack trace)
    if os.path.exists(java_file_path):        
        # check to see if it is a relative path or if there is something there already
        fullpath =  os.path.realpath(java_file_path)  
        classpath = ''
        if ".java" in os.path.basename(fullpath):
            os.system('javac ' + str(fullpath))
            classpath = (os.path.basename(fullpath)).replace('.java', '')
        elif ".class" in os.path.basename(fullpath):
            classpath = (os.path.basename(fullpath)).replace('.class', '')
        javap_result = subprocess.check_output("javap -p -classpath " + os.path.dirname(fullpath) + " " + classpath, shell=True)
        methods_with_arugments = re.findall(r"(\w+\(.*\))", javap_result)
        os.system("java -agentlib:hprof=cpu=times -classpath " + os.path.dirname(fullpath) + " " + classpath)
        # Reads in the results, dumps some of it to the console
        results = open("./java.hprof.txt", "r")
        rankings = list()
        trace_search_list = list()

        for line in results:                
            if "rank " in line:
                for index, entry in enumerate(results):
                    if (index < TOTAL_RANKINGS):
                        temp_list = entry.split()
                        # Do not include items that are internal java calls
                        if ("java." in entry):
                            break
                        temp_list = entry.split()
                        trace_search_list.append("TRACE " + temp_list[TRACE] + ":") 
                        # ignore method name as it will appear in stack trace and accum as they are not useful for diagnostic anymore
                        del temp_list[METHOD]
                        del temp_list[ACCUM]
                        rankings.append(temp_list)
                    else: break
        search_index = 0 
        for search_query in trace_search_list:
            results = open("./java.hprof.txt", "r")
            for line in results:
                if search_query in line:
                    for method in results:
                        if ("TRACE " not in method):
                            method = re.sub(r'\t', '', method)
                            method = re.sub(r'\n', '', method)
                            method_name = re.findall(r"(\w+)\(.*\)", method)
                            for entry in methods_with_arugments:
                                if method_name[0] in entry:
                                    argument_type = re.findall(r"(\(.*\))", entry)
                                    method = re.sub(r"\(.*\)", argument_type[0], method)
                            rankings[search_index].append(method)
                        else:
                            search_index += 1
                            break
        print("Analysis complete.\n")
        print("REPORT")
        for entry in rankings:
            print ("Method "+entry[4]+" was called "+entry[2]+" times using "+entry[1]+" CPU.")
        print("\n")
        return rankings, methods_with_arugments, classpath
    else:
        print("Java file does not exist.")

# Function to regex to get the variables out of the method declaration as a string
def parse_variables(fn):
    vars_re = re.compile(".*\((.*?)\)")
    m = vars_re.match(fn)
    vars_string = m.group(1).replace(" ", "")
    vars_list = vars_string.split(",")
    return vars_list

# Given a function declaration, return the function name
def get_method_name(method):
    method_re = re.compile("^(.*)\(")
    m = method_re.match(method)
    return m.group(1)
