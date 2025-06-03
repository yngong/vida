#!/usr/bin/env python3
import argparse
from Bio import SeqIO

def main():
    parser = argparse.ArgumentParser(
        description="Filter FASTA sequences whose headers contain any substring from a given list."
    )
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-l", "--list", required=True, help="File containing list of substrings to match in headers")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file")

    args = parser.parse_args()

    # Read target substrings from list file
    with open(args.list) as f:
        targets = [line.strip() for line in f if line.strip()]

    # Parse input FASTA and filter records
    matched_records = []
    for record in SeqIO.parse(args.input, "fasta"):
        if any(target in record.description for target in targets):
            matched_records.append(record)

    # Write filtered records to output file
    SeqIO.write(matched_records, args.output, "fasta")

if __name__ == "__main__":
    main()
