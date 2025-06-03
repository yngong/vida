#!/usr/bin/env python3
import argparse
from Bio import SeqIO

def read_fasta_to_dict(file_path):
    """Read a FASTA file and return a dictionary {seq_id: sequence string}."""
    seq_dict = {}
    for record in SeqIO.parse(file_path, "fasta"):
        seq_dict[record.id] = str(record.seq).upper()
    return seq_dict

def compare_fasta_files(file1, file2):
    """Compare sequences from two FASTA files, ignoring formatting."""
    seqs1 = read_fasta_to_dict(file1)
    seqs2 = read_fasta_to_dict(file2)

    keys1 = set(seqs1.keys())
    keys2 = set(seqs2.keys())

    if keys1 != keys2:
        print("Headers differ between files.")
        print("In file1 only:", keys1 - keys2)
        print("In file2 only:", keys2 - keys1)
        return False

    for key in keys1:
        if seqs1[key] != seqs2[key]:
            print(f"Sequence differs for {key}.")
            return False

    print("The two FASTA files have identical sequences (ignoring formatting).")
    return True

def main():
    parser = argparse.ArgumentParser(description="Compare two FASTA files ignoring formatting differences.")
    parser.add_argument("-i", "--input", nargs=2, metavar=('file1.fasta', 'file2.fasta'), required=True,
                        help="Two input FASTA files to compare")
    args = parser.parse_args()

    compare_fasta_files(args.input[0], args.input[1])

if __name__ == "__main__":
    main()
