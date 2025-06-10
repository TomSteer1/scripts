#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 3:
    print("Usage: ddCopy.py <input file> <output file>")
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if outputFile == ".":
    outputFile = inputFile.split("/")[-1]

if not os.path.exists(inputFile):
    print(f"Input file '{inputFile}' does not exist.")
    sys.exit(1)

if os.path.exists(outputFile):
    print(f"Output file '{outputFile}' already exists. Overwrite? (y/n)")
    response = input().strip().lower()
    if response != 'y':
        print("Operation cancelled.")
        sys.exit(1)

# Check if the input and output files are the same
if os.path.abspath(inputFile) == os.path.abspath(outputFile):
    print("Input and output files are the same. Operation cancelled.")
    sys.exit(1)

try:
    os.system(f"dd if='{inputFile}' of='{outputFile}' bs=1M status=progress conv=sync")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
