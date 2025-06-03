#!/usr/bin/env python3
import os
import argparse

def load_mapfile(mapfile):
    """Load a tab-delimited mapping of keys to values."""
    mapping = {}
    with open(mapfile, 'r') as mf:
        for line in mf:
            key, value = line.strip().split("\t")
            mapping[key] = value
    return mapping

def restore_by_substring(input_file, output_file, mapfile):
    """Replace substrings in each line using mapping."""
    mapping = load_mapfile(mapfile)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            modified_line = line
            for key, value in mapping.items():
                if key in modified_line:
                    modified_line = modified_line.replace(key, value)
            outfile.write(modified_line)

def main():
    parser = argparse.ArgumentParser(
        description="Replace substrings in a file using a TSV mapping file."
    )
    parser.add_argument("-i", "--input", required=True, help="Input text file")
    parser.add_argument("-o", "--output", required=True, help="Output file with replaced substrings")
    parser.add_argument("-m", "--mapfile", required=True, help="TSV file mapping keys to replacement values")

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        parser.error(f"Input file not found: {args.input}")
    if not os.path.isfile(args.mapfile):
        parser.error(f"Mapping file not found: {args.mapfile}")

    restore_by_substring(args.input, args.output, args.mapfile)
    print(f"Processed file saved to: {args.output}")

if __name__ == "__main__":
    main()
