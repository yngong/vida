import sys

def read_list_file(list_file):
    """Read list file and return a set of sequence names."""
    with open(list_file, 'r') as f:
        return {line.strip() for line in f if line.strip()}

def process_seq_file(seq_file, valid_sequences, output_file):
    """Read sequence file and write matching sequences to output file."""
    should_print = False
    with open(seq_file, 'r') as f, open(output_file, 'w') as out_f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                should_print = line[1:] in valid_sequences
                if should_print:
                    out_f.write(f"{line}\n")
            elif should_print:
                out_f.write(f"{line}\n")

def main():
    if len(sys.argv) != 4:
        print("Error")
        print("Syntax: python get_seq_8_list.py seq_file list_file output_file")
        sys.exit(1)
    
    list_file, seq_file, output_file = sys.argv[2], sys.argv[1], sys.argv[3]
    valid_sequences = read_list_file(list_file)
    process_seq_file(seq_file, valid_sequences, output_file)

if __name__ == "__main__":
    main()
