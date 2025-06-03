#!/usr/bin/env python3
import argparse
from Bio import SeqIO

def parse_key_and_segment(header):
    """
    Parse key and segment from header.
    Example header:
    >EPI_ISL_192111|A/NewMexico/17/2015|2015-03-11|NP|5|A/H1N1|pdm09|E2|
    Return (key, segment) e.g. ("NewMexico_2015_03", "HA")
    """
    parts = header.replace(" ", "").split("|")
    try:
        strain_parts = parts[1].split("/")
        date_parts = parts[2].split("-")
        segment = parts[3]
        key = f"{strain_parts[1]}_{date_parts[0]}_{date_parts[1]}"
        return key, segment
    except IndexError:
        return None, None

def main():
    parser = argparse.ArgumentParser(description="Downsample sequences from GISAID format FASTA")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-c", "--cutoff", type=int, required=True, help="Max sequences per key")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA prefix")
    args = parser.parse_args()

    seq_counts = {}
    output_file = args.output

    # Clear output file before writing
    open(output_file, "w").close()

    with open(output_file, "a") as out_handle:
        for record in SeqIO.parse(args.input, "fasta"):
            key, segment = parse_key_and_segment(record.description)
            if key is None or segment != "HA":
                continue
            count = seq_counts.get(key, 0)
            if count <= args.cutoff:
                SeqIO.write(record, out_handle, "fasta")
                seq_counts[key] = count + 1

if __name__ == "__main__":
    main()
