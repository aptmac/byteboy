#!/usr/bin/python3

# main.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys

from analysis import run_analysis
from interactive import interactive
from interactive import manual_creation
from interactive import print_ascii_art

def main(java_file):
    os.system("clear")
    print("Thanks for choosing")
    print_ascii_art()
    print("A Companion Application for Byteman.")
    print("---------------------------------------")
    if java_file != False:
        print("- Running program analysis")
        print("- - If you think the program is stuck looping, use <ctrl+c> to continue")
        rankings, methods, classname  = run_analysis(java_file)
        interactive(rankings, methods, classname)
    else:
        print("You have not supplied a Java application to Byteboy.")
        print("The functionality available to you is Manual Rule Creation.")
        result = raw_input("Do you wish to continue? (y/n): ")
        if result == "y":
            manual_creation()
    print("Goodbye.")

if __name__ == "__main__":
    try:
        java_file = sys.argv[1]
        main(java_file)
    except IndexError:
        main(False)
