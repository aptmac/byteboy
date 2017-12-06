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
    script += "RULE "
    script += rule_name
    script += "\n"
    return script

# Appends the Class name to the script
def add_class(script, class_name):
    script += "CLASS "
    script += class_name
    script += "\n"
    return script

# Appends the Method name to the script
def add_method(script, method_name):
    script += "METHOD "
    script += method_name
    script += "\n"
    return script

# Appends the entry point to the script
def add_entry(script, entry_point):
    script += "AT "
    script += entry_point
    script += "\nIF TRUE\n"
    return script

# Appends the Rule Logic to the script
def add_body(script, body):
    script += body
    return script

def write_to_file(script):
    filename = raw_input ("What would you like to call your file?: ")
    if filename.find(".btm") == -1:
        filename += ".btm"
    if not os.path.exists("output"):
        os.makedirs("output")
    file = open("output/" + filename, "w")
    file.write(script)
    file.close()

# Appends the ENDRULE keyword to the script 
def add_endrule(script):
    script += "ENDRULE"
    return script


def manual_creation():
    print("GUIDED MANUAL RULE CREATION")
    script = ""
    # Create a generic rule based completely on user input
    script = add_rule(script, raw_input("What would you like to name your Rule: "))
    script = add_class(script, raw_input("What is the target Class name: "))
    script = add_method(script, raw_input("What is the target Method name: "))
    script = add_entry(script, raw_input("When would you like to trigger activity? (ENTRY or EXIT): "))
    print("What is the body of the script?: (input an empty line when finished)")
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
