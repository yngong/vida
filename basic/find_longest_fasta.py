import sys
from Bio import SeqIO

def find_longest_sequence(fasta_file):
    """
    Find the longest sequence in a FASTA file.
    """
    longest_record = None
    max_length = 0

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_length = len(record.seq)
        if seq_length > max_length:
            longest_record = record
            max_length = seq_length

    return longest_record

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_longest_fasta.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    longest_seq = find_longest_sequence(fasta_file)

    if longest_seq:
        print(f"\n✅ Longest sequence: {longest_seq.id}")
        print(f"🔹 Length: {len(longest_seq.seq)}")
        print(f"🧬 Sequence (first 100 bp): {longest_seq.seq[:100]}...\n")
    else:
        print("⚠️ No sequences found in the file.")
