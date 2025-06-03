#!/usr/bin/env python3
import sys
from Bio import SeqIO

def print_usage():
    print("Usage: python generateGenome4GISAID.py -o OUTPUT_PREFIX")
    sys.exit(1)

def main():
    # Parse command line arguments manually via sys.argv
    if len(sys.argv) != 3 or sys.argv[1] != "-o":
        print("Error")
        print_usage()

    output_prefix = sys.argv[2]

    genes = ["PB2.fas", "PB1.fas", "PA.fas", "HA.fas", "NP.fas", "NA.fas", "MP.fas", "NS.fas"]
    strain_counts = {}

    # Count occurrences of each strain key across segments
    for gene_file in genes:
        for record in SeqIO.parse(gene_file, "fasta"):
            key = record.description.split("|")[0].strip()
            strain_counts[key] = strain_counts.get(key, 0) + 1

    # Filter for strains that have all 8 segments
    complete_strains = {k for k, v in strain_counts.items() if v == 8}

    # Write filtered sequences to new files with output prefix
    for gene_file in genes:
        output_file = f"{output_prefix}_{gene_file}"
        with open(output_file, "w") as out_handle:
            for record in SeqIO.parse(gene_file, "fasta"):
                key = record.description.split("|")[0].strip()
                if key in complete_strains:
                    SeqIO.write(record, out_handle, "fasta")

if __name__ == "__main__":
    main()
