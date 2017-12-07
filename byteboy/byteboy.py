#!/usr/bin/python3

# main.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys

from analysis import run_analysis
from interactive import interactive
from interactive import manual_creation

def main(java_file):
    os.system("clear")
    print("Thanks for choosing")
    # Cool ascii art courtesy of: http://www.patorjk.com/software/taag
    print("______       _       _")         
    print("| ___ \     | |     | |")                
    print("| |_/ /_   _| |_ ___| |__   ___  _   _") 
    print("| ___ \ | | | __/ _ \ '_ \ / _ \| | | |")
    print("| |_/ / |_| | ||  __/ |_) | (_) | |_| |")
    print("\____/ \__, |\__\___|_.__/ \___/ \__, |")
    print("        __/ |                     __/ |")
    print("       |___/                     |___/")
    print("A Companion Application for Byteman.")
    print("---------------------------------------")
    if java_file != False:
        print("- Running program analysis")
        print("- - If you think the program is stuck looping, use <ctrl+c> to continue")
        rankings, methods  = run_analysis(java_file)
        interactive(rankings, methods)
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