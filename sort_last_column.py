#!/usr/bin/env python3
import sys

def extract_sort_print_column(filename):
    with open(filename) as f:
        # Extract the last column
        last_column = [line.strip().split("\t")[-1] for line in f if line.strip()]
    # Remove header if it is there
    try:
        float(last_column[0])
    except ValueError:
        last_column = last_column[1:]
    # Sort the values
    last_column.sort()
    # Print in the terminal
    print("\n".join(last_column))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 sort_last_column.py <filename.tsv>")
        sys.exit(1)
    filename = sys.argv[1]
    extract_sort_print_column(filename)

#### Run the script bytyping in the command line: sort_last_column.py filename.tsv
