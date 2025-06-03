#!/usr/bin/env python3

import os
import argparse
from Bio import SeqIO

def main():
    parser = argparse.ArgumentParser(description="Split GISAID sequences by genome segment")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-d", "--dir", required=True, help="Output directory to save segmented FASTA files")
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.dir, exist_ok=True)

    seen_acc_segment = set()
    seen_strain_segment = set()

    with open(args.input) as infile:
        # Parse input FASTA file
        for record in SeqIO.parse(infile, "fasta"):
            # Split the header using '|' delimiter and remove spaces
            parts = record.description.replace(" ", "").split("|")
            acc = parts[0].replace(">", "")  # Accession number without '>'
            strain = parts[1]                # Strain name
            segment = parts[3]               # Genome segment identifier

            key_acc = f"{acc}_{segment}"
            key_strain = f"{strain}_{segment}"

            # Check if accession-segment or strain-segment combination has appeared
            if key_acc not in seen_acc_segment and key_strain not in seen_strain_segment:
                seen_acc_segment.add(key_acc)
                seen_strain_segment.add(key_strain)

                # Append sequence to the corresponding segment file inside output directory
                out_file = os.path.join(args.dir, f"{segment}.fas")
                with open(out_file, "a") as outfh:
                    SeqIO.write(record, outfh, "fasta")

if __name__ == "__main__":
    main()
