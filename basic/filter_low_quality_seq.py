#!/usr/bin/env python3

import sys
from Bio import SeqIO

def print_usage():
    """Prints usage message and exits the script."""
    print("Usage: python filter_fasta.py <input.fasta> <cutoff_percentage>")
    print("Example: python filter_fasta.py sequences.fasta 3")
    sys.exit(1)

def filter_sequences(fasta_file, cutoff):
    """Filters sequences based on the percentage of non-ATCG bases."""
    qualified_records = []
    filtered_records = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()  # Convert to uppercase
        if len(seq) == 0:
            continue  # Skip empty sequences
        
        non_atcg_count = sum(1 for base in seq if base not in "ATCG")
        non_atcg_percentage = (non_atcg_count / len(seq)) * 100

        if non_atcg_percentage > cutoff:
            filtered_records.append(record)
        else:
            qualified_records.append(record)

    # Save results
    if qualified_records:
        SeqIO.write(qualified_records, "qualified.fasta", "fasta")
        print(f"✅ Saved {len(qualified_records)} qualified sequences to 'qualified.fasta'")
    else:
        print("⚠ No qualified sequences found.")

    if filtered_records:
        SeqIO.write(filtered_records, "filtered_out.fasta", "fasta")
        print(f"❌ Saved {len(filtered_records)} filtered sequences to 'filtered_out.fasta'")
    else:
        print("✅ No sequences exceeded the cutoff, 'filtered_out.fasta' is not created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()

    try:
        fasta_filename = sys.argv[1]
        cutoff_percentage = float(sys.argv[2])
        if cutoff_percentage < 0 or cutoff_percentage > 100:
            raise ValueError
    except ValueError:
        print("Error: Cutoff percentage must be a number between 0 and 100.")
        print_usage()

    filter_sequences(fasta_filename, cutoff_percentage)
