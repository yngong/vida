import sys
import os

# Load the mapfile to get the mapping of new headers to original headers
def load_mapfile(mapfile):
    mapping = {}
    with open(mapfile, 'r') as mf:
        for line in mf:
            new_header, original_header = line.strip().split("\t")
            mapping[new_header] = original_header
    return mapping

# Restore the renamed FASTA file using the mapfile and save as a new file
def restore_fasta(renamed_fasta, restored_fasta, mapfile):
    mapping = load_mapfile(mapfile)
    
    with open(renamed_fasta, 'r') as fasta_in, open(restored_fasta, 'w') as fasta_out:
        for line in fasta_in:
            if line.startswith(">"):
                new_header = line.strip()[1:]  # Remove '>'
                original_header = mapping.get(new_header, new_header)  # Restore the original header from mapfile
                fasta_out.write(f">{original_header}\n")
            else:
                fasta_out.write(line)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python restore_fasta.py <renamed_fasta> <restored_fasta> <mapfile.tsv>")
        sys.exit(1)  # Exit if arguments are not correct
    
    # Get arguments from the command line
    renamed_fasta = sys.argv[1]
    restored_fasta = sys.argv[2]
    mapfile = sys.argv[3]
    
    # Check if the provided files exist
    if not os.path.isfile(renamed_fasta):
        print(f"Error: File {renamed_fasta} not found")
        sys.exit(1)
    if not os.path.isfile(mapfile):
        print(f"Error: File {mapfile} not found")
        sys.exit(1)

    # Start the restoration process
    restore_fasta(renamed_fasta, restored_fasta, mapfile)
    print(f"Successfully restored {renamed_fasta} to {restored_fasta}")
