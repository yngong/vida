import sys
import re
import os

# Sanitize the header by replacing all characters that are not alphanumeric, -, or _
# with an underscore (_)
def sanitize_header(header):
    sanitized = re.sub(r'[^\w\-]', '_', header)  # Replace all non-alphanumeric, non-underscore, non-hyphen characters with _
    return sanitized

# Rename the headers in the FASTA file and create a mapping in a TSV file
def rename_fasta(input_fasta, output_fasta, mapfile):
    with open(input_fasta, 'r') as fasta_in, open(output_fasta, 'w') as fasta_out, open(mapfile, 'w') as map_out:
        header_count = 1  # Counter for generating new header names
        
        for line in fasta_in:
            if line.startswith(">"):
                original_header = line.strip()[1:]  # Remove the '>' and newline characters
                sanitized_header = sanitize_header(original_header)  # Clean up the header by replacing special characters
                new_header = f"seq_{header_count}_"  # Create a new header format (e.g., A_1_E)
                
                # Write the mapping of new header to original (sanitized) header in the mapfile
                map_out.write(f"{new_header}\t{sanitized_header}\n")
                
                # Write the new header to the output FASTA file
                fasta_out.write(f">{new_header}\n")
                header_count += 1
            else:
                # For sequence lines, write them directly to the output FASTA file
                fasta_out.write(line)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python rename_fasta.py <input_fasta> <output_fasta> <mapfile.tsv>")
        sys.exit(1)  # Exit if arguments are not correct
    
    # Get arguments from the command line
    input_fasta = sys.argv[1]
    output_fasta = sys.argv[2]
    mapfile = sys.argv[3]
    
    # Check if the input FASTA file exists
    if not os.path.isfile(input_fasta):
        print(f"Error: File {input_fasta} not found")
        sys.exit(1)

    # Start the renaming process
    rename_fasta(input_fasta, output_fasta, mapfile)
    print(f"Successfully renamed headers in {input_fasta} and saved as {output_fasta}. Mapping saved in {mapfile}")
