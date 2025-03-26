from Bio import SeqIO
import pandas as pd
import sys
import os
import re

def extract_accession(header):
    """
    Extracts the Accession Number from a FASTA header formatted like:
    >accn|JF414933 ...
    """
    parts = header.split("|")
    if len(parts) > 1:
        return parts[1].split()[0]  # Extract "JF414933" and remove trailing spaces
    return header  # Fallback in case format is unexpected

def clean_classification_name(name):
    """
    Replaces special characters (e.g., '/', spaces) with underscores.
    """
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)

def split_fasta_by_classification(fasta_file, mapping_csv, output_dir="split_fasta"):
    """
    Splits a FASTA file into multiple files based on classification mapping.
    Also provides statistics on categorized and uncategorized sequences.
    """
    # Load classification mapping
    mapping_df = pd.read_csv(mapping_csv)
    mapping_df["Classification"] = mapping_df["Classification"].astype(str).apply(clean_classification_name)
    classification_map = dict(zip(mapping_df["Accession"], mapping_df["Classification"]))

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize storage for sequences
    classified_seqs = {}
    unclassified_seqs = []
    classified_count = 0
    unclassified_count = 0

    # Read the FASTA file and assign sequences to categories
    for record in SeqIO.parse(fasta_file, "fasta"):
        accession = extract_accession(record.id)  # Extract correct Accession Number
        classification = classification_map.get(accession, "Unclassified")  # Default to "Unclassified"

        if classification == "Unclassified":
            unclassified_seqs.append(record)
            unclassified_count += 1
        else:
            classified_count += 1
            if classification not in classified_seqs:
                classified_seqs[classification] = []
            classified_seqs[classification].append(record)

    # Write sequences into separate FASTA files
    for classification, records in classified_seqs.items():
        output_fasta = os.path.join(output_dir, f"{classification}.fasta")
        SeqIO.write(records, output_fasta, "fasta")
        print(f"✅ Saved {len(records)} sequences to {output_fasta}")

    # Write Unclassified sequences into a separate file
    if unclassified_seqs:
        unclassified_fasta = os.path.join(output_dir, "Unclassified.fasta")
        SeqIO.write(unclassified_seqs, unclassified_fasta, "fasta")
        print(f"⚠️ Saved {len(unclassified_seqs)} unclassified sequences to {unclassified_fasta}")

    # Print summary statistics
    print("\n🔹 Classification Summary 🔹")
    print(f"✅ Categorized Sequences: {classified_count}")
    print(f"❌ Unclassified Sequences: {unclassified_count}")
    print(f"📁 Output directory: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_fasta.py sequences.fasta classification_mapping.csv")
        sys.exit(1)

    fasta_file = sys.argv[1]
    mapping_csv = sys.argv[2]
    
    split_fasta_by_classification(fasta_file, mapping_csv)
