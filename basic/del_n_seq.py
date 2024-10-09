import sys
from Bio import SeqIO

if len(sys.argv) != 3:
    print("Error")
    print("Syntax: python del_n_seq.py filename percentage")
    sys.exit(1)

input_filename = sys.argv[1]
output_removed_filename = "Removed_" + input_filename
output_kept_filename = "Keeped_" + input_filename

with open(input_filename, "r") as input_file, \
        open(output_removed_filename, "w") as removed_file, \
        open(output_kept_filename, "w") as kept_file:

    sequences = SeqIO.parse(input_file, "fasta")

    for seq_record in sequences:
        seq = str(seq_record.seq).upper()
        count_n = seq.count("N")

        if count_n / len(seq) <= float(sys.argv[2]):
            SeqIO.write(seq_record, kept_file, "fasta")
        else:
            SeqIO.write(seq_record, removed_file, "fasta")

        print(seq_record.description + ": " + str(count_n))

print("Processing complete.")

