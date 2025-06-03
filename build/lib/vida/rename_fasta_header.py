#!/usr/bin/env python3
import re
import os
import argparse

def sanitize_header(header):
    """Replace all non-alphanumeric, non-underscore, non-hyphen characters with underscores, except for | pipe."""
    return re.sub(r'[^\w\-/|]', '_', header)


def rename_fasta(input_fasta, output_fasta, mapfile):
    """Rename headers in a FASTA file and save mapping to a TSV file."""
    with open(input_fasta, 'r') as fasta_in, open(output_fasta, 'w') as fasta_out, open(mapfile, 'w') as map_out:
        header_count = 1
        for line in fasta_in:
            if line.startswith(">"):
                original_header = line.strip()[1:]
                sanitized_header = sanitize_header(original_header)
                new_header = f"seq_{header_count}_"
                map_out.write(f"{new_header}\t{sanitized_header}\n")
                fasta_out.write(f">{new_header}\n")
                header_count += 1
            else:
                fasta_out.write(line)

def main():
    parser = argparse.ArgumentParser(
        description="Rename FASTA headers to simplified format and save a mapping file."
    )
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file with renamed headers")
    parser.add_argument("-m", "--mapfile", required=True, help="Output TSV file mapping new headers to sanitized originals")

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        parser.error(f"Input file not found: {args.input}")

    rename_fasta(args.input, args.output, args.mapfile)
    print(f"Renamed headers saved to: {args.output}")
    print(f"Header mapping saved to: {args.mapfile}")

if __name__ == "__main__":
    main()
