#!/usr/bin/python

# interactive.py
# CMPT 479 - Final Project
# Contributors: aptmac

# This file allows for the user to interact with the data received during analysis.
# It allows for a guided creation of a Byteman script based on the analysis.
# Or for more advanced users, allows for the freedom to write a rule of their choice.
# If Byteman is configured on the host's machine, should allow for syntax checking as well.

import os
import sys

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

# Writes the created rule to a file in the output folder, and creates
# the output folder if it doesn't exist.
def write_to_file(script):
    filename = raw_input ("What would you like to call your file?: ")
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
    print("GUIDED MANUAL RULE CREATION")
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
    return

# Semiautomatic Creation()
# - Using the results from the analysis, functions similar to the manual creation
# - - but suggests what Classes/Methods/etc. the user may be interested in
# - - based on the execution of their program.
def semiautomatic_creation():
    # TODO
    return

def automatic_generator():
    # TODO
    return

def fuzztest_generator():
    # TODO
    return

####
# Main
####
def main():
    os.system('clear')
    print("-----------------------------------------------------")
    print("Welcome to the interactive Byteman script generator.")
    print("-----------------------------------------------------")
    print("1. Manual Rule Creation")
    print("2. Semi-Automatic Rule Creation")
    print("3. Automatic Rule Generation (for tracing purposes)")
    print("4. Fuzz Test Generator")
    print("5. Exit")
    result = int(input("Please select your choice: "))
    if result == 1:
        os.system("clear")
        manual_creation()
    elif result == 2:
        os.system("clear")
        semiautomatic_creation()
    elif result == 3:
        os.system("clear")
        automatic_generator()
    elif result == 4:
        os.system("clear")
        fuzztest_generator()
    print("Goodbye.")


if __name__ == "__main__":
    main()
