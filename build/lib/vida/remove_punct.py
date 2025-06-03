#!/usr/bin/env python3

import argparse
import re

def remove_punctuation_from_header(line):
    """
    Remove punctuation characters from header line, except for |, >, /, -, and _.
    Also remove spaces.
    """
    # Remove punctuation except specified ones
    # The original Java regex removed: !"#$%&'()*+,.:;<=?@[\]^`{}~
    # We keep | > / - _
    # So remove: !"#$%&'()*+,.:;<=?@[\]^`{}~
    # Note: re.escape may be used for safer escaping but here we hardcode.
    # Remove spaces as well
    cleaned = re.sub(r'[!"#$%&\'()*+,.:;<=?@\[\]^`{}~]+', '', line)
    cleaned = cleaned.replace(' ', '')
    return cleaned

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.rstrip('\n')
            if line.startswith('>'):
                cleaned_header = remove_punctuation_from_header(line)
                print(cleaned_header, file=outfile)
            else:
                print(line, file=outfile)

def main():
    parser = argparse.ArgumentParser(description="Remove punctuation from FASTA headers except |, >, /, -, and _")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file")
    args = parser.parse_args()

    process_file(args.input, args.output)

if __name__ == "__main__":
    main()
