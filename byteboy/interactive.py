#!/usr/bin/python

# interactive.py
# CMPT 479 - Final Project
# Contributors: aptmac

# This file allows for the user to interact with the data received during analysis.
# It allows for a guided creation of a Byteman script based on the analysis.
# Or for more advanced users, allows for the freedom to write a rule of their choice.
# If Byteman is configured on the host's machine, should allow for syntax checking as well.

import os
import random
import uuid
import sys

from analysis import parse_variables
from analysis import get_method_name

###
# Helper Functions for adding content to Byteman Scripts
###

# Appends the Rule name to the script
def add_rule(script, rule_name):
    script += "RULE " + rule_name + "\n"
    return script

# Appends the Class name to the script
def add_class(script, class_name):
    script += "CLASS " + class_name + "\n"
    return script

# Appends the Method name to the script
def add_method(script, method_name):
    script += "METHOD " + method_name + "\n"
    return script

# Appends the entry point to the script
def add_entry(script, entry_point):
    script += "AT " + entry_point + "\n"
    return script

def add_conditional(script, condition):
    script += "IF " + condition + "\n"
    return script

# Appends the Rule Logic to the script
def add_body(script, body):
    script += body
    return script

# Appends the ENDRULE keyword to the script 
def add_endrule(script):
    script += "ENDRULE"
    return script

####
# Helper functions to fuzz random values
####
def fuzz_int():
    max_int = 2147483647
    return random.randint(-max_int, max_int)

def fuzz_long():
    max_long = 9223372036854775807
    return random.randint(-max_long, max_long)

def fuzz_float():
    modifier = random.uniform(0, 1)
    return modifier*fuzz_long()

def fuzz_double():
    return fuzz_float()

def fuzz_string():
    # Idea to use uuid borrowed from StackOverflow discussion found at:
    # https://stackoverflow.com/questions/37675280/how-to-generate-a-random-string
    return "\"{}\"".format(uuid.uuid4().hex)

def fuzz_boolean():
    if random.randint(0, 10) > 5:
        return "true"
    else:
        return "false"

def fuzz_action(script, pos, value):
    script += "DO\n"
    action = "${} = {}\n".format(pos, value)
    script += action
    return script

# Writes the created rule to a file in the output folder, and creates
# the output folder if it doesn't exist.
def write_to_file(script, filename = False):
    if filename == False:
        filename = raw_input ("What would you like to call your rule file? (e.g., <name>.btm): ")
    if filename.find(".btm") == -1:
        filename += ".btm"
    if not os.path.exists("output"):
        os.makedirs("output")
    file = open("output/" + filename, "w")
    file.write(script)
    file.close()

# Manual Creation()
# - Guides the user through writing the necessary components of a Byteman rule
# - Inspired by the Yeoman code generator, which offers similar functionality for
# - - scaffolding JavaScript applications and VS Code extensions
def manual_creation():
    print("---------------------------")
    print("GUIDED MANUAL RULE CREATION")
    print("---------------------------")
    script = ""
    # Create a generic rule based completely on user input
    script = add_rule(script, raw_input("What would you like to name your Rule: "))
    script = add_class(script, raw_input("What is the target Class name: "))
    script = add_method(script, raw_input("What is the target Method name: "))
    script = add_entry(script, raw_input("When would you like to trigger activity? (ENTRY or EXIT): "))
    script = add_conditional(script, raw_input("Under what conditions should the rule execute? (if not sure, write TRUE): "))
    print("What is the body of the script? (input an empty line when finished):\n- For Example: traceln(\"<text>\") could be used to write to the console.")
    body = ""
    while True:
        line = raw_input()
        if not line: break
        body += line
        body += "\n"
    script = add_body(script, body)
    script = add_endrule(script)
    write_to_file(script)
    print("Manual Creation has completed.")
    return

# Semiautomatic Creation()
# - Using the results from the analysis, functions similar to the manual creation
# - - but suggests what Classes/Methods/etc. the user may be interested in
# - - based on the execution of their program.
def semiautomatic_creation(methods, classname):
    print("----------------------------------")
    print("GUIDED SEMIAUTOMATIC RULE CREATION")
    print("----------------------------------")
    print("INSTRUCTIONS")
    print("- Based on the analysis results, Byteboy will list potential options you may be interested in.")
    print("- Feel free to use the highest ranking option, or if you type nothing then Byteboy will automatically use the first entry.")
    print("- Let's begin!\n")
    script = ""
    print("The identified CLASS name is: " + classname)
    method = raw_input("The identified METHODS are:\n" + str(methods) + "\nWhich METHOD do you wish to target? (only enter the name): ")
    if method == "":
        method = get_method_name(methods[0])
    entry = raw_input("When would you like to trigger activity? (ENTRY/EXIT, default is ENTRY): ")
    if entry == "":
        entry = "ENTRY"
    condition = raw_input("Under what conditions should the rule execute? (default is IF TRUE): ")
    if condition == "":
        condition = "TRUE"
    print("What is the body of the script? (input an empty line when finished):\n- For Example: traceln(\"<text>\") could be used to write text to the console.")
    body = "DO\n"
    while True:
        line = raw_input()
        if not line: break
        body += line
        body += "\n"
    rulename = raw_input("What would you like to name your rule?: ")

    # Compile the rule & write to file
    script = add_rule(script, rulename)
    script = add_class(script, classname)
    script = add_method(script, method)
    script = add_entry(script, entry)
    script = add_conditional(script, condition)
    script = add_body(script, body)
    script = add_endrule(script)
    write_to_file(script)
    print("Semi-automatic Creation has completed.")
    return

# Automatic Generator()
# - Using the results from the analysis, automatically generates rules that can be used
# - - to trace application behaviour and progress
def automatic_generator(methods, classname):
    print("---------------------------------")
    print("AUTOMATIC RULE CREATION - Tracing")
    print("---------------------------------")
    # Automatically generate rules (or try to) that are found from our analysis
    files = []
    for method in methods:
        method = get_method_name(method)
        if method != classname:  # don't want to write a rule for the class declaration
            script = ''
            # Generate the Entry Rule
            script = add_rule(script, "Traceln when Entering {}.{}".format(classname, method))
            script = add_class(script, classname)
            script = add_method(script, method)
            script = add_entry(script, "ENTRY")
            script = add_conditional(script, "TRUE")
            script += "DO\ntraceln(\"- Entering {} in class {}\")\n".format(method, classname)
            script = add_endrule(script)
            script += "\n\n"

            # Generate the Exit Rule
            script = add_rule(script, "Traceln when Exiting {}.{}".format(classname, method))
            script = add_class(script, classname)
            script = add_method(script, method)
            script = add_entry(script, "EXIT")
            script = add_conditional(script, "TRUE")
            script += "DO\ntraceln(\"- Exiting {} in class {}\")\n".format(method, classname)
            script = add_endrule(script)

            # Write to file
            filename = "trace_{}-{}".format(classname, method)
            files.append(filename)
            write_to_file(script, filename)
    print("The following set of files have been created: " + str(files))
    print("Automatic Generation has completed.")
    return

# Fuzztest Generation()
# - Using the results of the analysis, figures out the data types of the arguments used
# - - in the method's arguments, and replace the variable contents with different values
# - - of the same type (or null)
def fuzztest_generator(methods, classname):
    print("------------------------")
    print("Fuzz Test Rule Generator")
    print("------------------------")
    # Has support for fuzzing the following types:
    # Numeric: int, long, float, double
    # String (java.lang.String)
    # Boolean
    files = []
    for method in methods:
        variables = parse_variables(method)
        method = get_method_name(method)
        if len(variables) >= 1:
            i = 1
            for var in variables:
                value = ""
                if var == "int":
                    value = fuzz_int()
                elif var == "long":
                    value = fuzz_long()
                elif var == "float":
                    value = fuzz_float()
                elif var == "double":
                    value = fuzz_double()
                elif var == "boolean":
                    value = fuzz_boolean()
                elif var == "java.lang.String":
                    value = fuzz_string()
                else: continue
                # Generate the rule
                script = ''
                script = add_rule(script, "Fuzz {}.{}() parameter #{} of type {}".format(classname, method, i, var))
                script = add_class(script, classname)
                script = add_method(script, method)
                script = add_entry(script, "ENTRY")
                script = add_conditional(script, "TRUE")
                script = fuzz_action(script, i, value)
                script = add_endrule(script)
                filename = "fuzz_{}-{}_arg{}-{}".format(classname, method, i, var)
                files.append(filename)
                write_to_file(script, filename)
                i = i + 1
    print("The following set of files have been created: " + str(files))
    print("Fuzz Test Generation has completed.")
    return

def print_ascii_art():
    # Cool ascii art courtesy of: http://www.patorjk.com/software/taag
    print("______       _       _")         
    print("| ___ \     | |     | |")                
    print("| |_/ /_   _| |_ ___| |__   ___  _   _") 
    print("| ___ \ | | | __/ _ \ '_ \ / _ \| | | |")
    print("| |_/ / |_| | ||  __/ |_) | (_) | |_| |")
    print("\____/ \__, |\__\___|_.__/ \___/ \__, |")
    print("        __/ |                     __/ |")
    print("       |___/                     |___/")

####
# Main function of interactive.py
####
def interactive(rankings, methods, classname):
    cont = 0
    while(cont == 0):
        print("-----------------------------------------------------")
        print("Welcome to the interactive Byteman script generator.")
        print("-----------------------------------------------------")
        print("1. Manual Rule Creation")
        print("2. Semi-Automatic Rule Creation")
        print("3. Automatic Rule Generation (for tracing purposes)")
        print("4. Fuzz Test Generator")
        print("5. Exit")
        result = raw_input("Please select your choice: ")
        try:
            result = int(result)
            if result == 1:
                os.system("clear")
                manual_creation()
            elif result == 2:
                os.system("clear")
                semiautomatic_creation(methods, classname)
            elif result == 3:
                automatic_generator(methods, classname)
            elif result == 4:
                fuzztest_generator(methods, classname)
            elif result == 5:
                print("You have chosen to exit the program.")
                break
            result = raw_input("Would you like to perform another Byteboy action? (y/n): ")
            if result == "n":
                cont = 1
            else:
                os.system("clear")
                print_ascii_art()
        except ValueError:
            print("Invalid input.")
            print("You must supply the number of the corresponding action you wish to perform.")
            break
