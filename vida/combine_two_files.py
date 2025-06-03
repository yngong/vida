#!/usr/bin/env python3

import argparse

def combine_two_files(file1: str, file2: str, output_file: str):
    """
    Combine two text files line by line, separated by a tab.
    Write the result to the specified output file.
    """
    # Read all lines from file2 into a list, skipping empty lines
    with open(file2, 'r') as f2:
        lines2 = [line.strip() for line in f2 if line.strip()]

    # Open file1 and the output file
    with open(file1, 'r') as f1, open(output_file, 'w') as out:
        count = 0
        for line1 in f1:
            line1 = line1.strip()
            if line1:
                if count < len(lines2):
                    out.write(f"{line1}\t{lines2[count]}\n")
                    count += 1
                else:
                    raise IndexError(f"Line count mismatch: '{file1}' has more lines than '{file2}'.")

    print(f"[Done] Combined output written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Combine two files line by line, separated by a tab.")
    parser.add_argument("-i", "--input1", required=True, help="First input file (used as the left column)")
    parser.add_argument("-j", "--input2", required=True, help="Second input file (used as the right column)")
    parser.add_argument("-o", "--output", required=True, help="Output file name")
    args = parser.parse_args()

    try:
        combine_two_files(args.input1, args.input2, args.output)
    except Exception as e:
        print(f"[Error] {e}")

if __name__ == "__main__":
    main()
