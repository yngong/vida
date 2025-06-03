#!/usr/bin/env python3

import argparse
from Bio import SeqIO

def calculate_N_fraction(seq):
    seq = str(seq).upper()
    return sum(seq.count(x) for x in ['N', '-', '*']) / len(seq) if len(seq) > 0 else 0

def process_fasta(input_file, threshold, output_kept, output_removed):
    with open(output_kept, "w") as kept, open(output_removed, "w") as removed:
        for record in SeqIO.parse(input_file, "fasta"):
            frac = calculate_N_fraction(record.seq)
            target = kept if frac <= threshold else removed
            SeqIO.write(record, target, "fasta")
            # print(f"{record.id}: {frac * 100:.2f}% ambiguous")

def main():
    parser = argparse.ArgumentParser(description="Filter FASTA sequences based on N/-/* content.")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-t", "--threshold", type=float, required=True,
                        help="Maximum allowed fraction of N/-/* (e.g. 0.05 for 5%)")
    parser.add_argument("-k", "--output-kept", required=True, help="Output FASTA file for kept sequences")
    parser.add_argument("-r", "--output-removed", required=True, help="Output FASTA file for removed sequences")
    args = parser.parse_args()

    process_fasta(args.input, args.threshold, args.output_kept, args.output_removed)

if __name__ == "__main__":
    main()
