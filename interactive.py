#!/usr/bin/python3

# interactive.py
# CMPT 479 - Final Project
# Contributors: aptmac

# This file allows for the user to interact with the data received during analysis.
# It allows for a guided creation of a Byteman script based on the analysis.
# Or for more advanced users, allows for the freedom to write a rule of their choice.
# If Byteman is configured on the host's machine, should allow for syntax checking as well.

import os
import sys

#######################################################
# TODO
# ----
# Idea: Create an array/list for the rule attributes
#       So it can be easily edited if a mistake occurs

###
# Helper Functions for adding content to Byteman Scripts
###

def add_rule(script, rule_name):
    script += "RULE "
    script += rule_name
    script += "\n"
    return script

def add_class(script, class_name):
    script += "CLASS "
    script += class_name
    script += "\n"
    return script

def add_method(script, method_name):
    script += "METHOD "
    script += method_name
    script += "\n"
    return script

def add_body(script, body):
    script += body
    return script

def add_endrule(script):
    script += "ENDRULE"
    return script

###
# Helper Functions for Guided and User-Controlled Script Writing
###
def create_guided_rule():
    return

def create_advanced_rule():
    script = ""
    # Create a generic rule based completely on user input
    script = add_rule(script, input("What is the rule name: "))
    script = add_class(script, input("What is the target Class name: "))
    script = add_method(script, input("What is the target Method name: "))
    # TODO: Add script logic
    print("What is the body of the script?: ")
    body = ''
    while True:
        line = input()
        if not line: break
        body += line
        body += "\n"
    script = add_body(script, body)
    script = add_endrule(script)

    # TODO: when using a list, this should just grab the name of the rule
    # and write that as the file name, but ask the user if they want
    # to have the filename be different than the rule name first
    filename = input ("What would you like to call your file?: ")

    # TODO: This should be done dynamically, if no extension was added we should add one
    filename += ".btm"
    file = open(filename, "w")
    file.write(script)
    file.close()
    return

def main():
    os.system('clear')
    print("-----------------------------------------------------")
    print("Welcome to the interactive Byteman script generator.")
    print("-----------------------------------------------------")
    print("1. Guided Script-Template with results from anaylsis")
    print("2. Advanced Template with user-directed script writing")
    print("3. Exit")
    result = int(input("Please select your choice: "))
    print(result)
    if result == 1:
        os.system('clear')
        create_guided_rule()
    elif result == 2:
        os.system('clear')
        create_advanced_rule()
    print ("Goodbye.")

if __name__ == "__main__":
    main()
