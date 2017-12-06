#!/usr/bin/python

# main.py
# CMPT 479 - Final Project
# Contributors: itpun, aptmac

import os
import sys

from analysis import run_analysis

def main(java_file):
    
    run_analysis(java_file)

if __name__ == "__main__":
    try:
        java_file = sys.argv[1]
        main(java_file)
    except IndexError:
        print("Invalid number of arguments supplied")
