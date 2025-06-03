#!/usr/bin/env python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from typing import Optional, Tuple

def find_first_or_second_atg_with_stop(seq: str, use_second_atg: bool) -> Optional[Tuple[int, int]]:
    """
    Scan the aligned reference sequence (with gaps) to find the first or second ATG,
    then extend to the first valid stop codon (TAA, TAG, TGA).
    Return the (start, end) indices covering the full CDS region.
    """
    stop_codons = {"TAA", "TAG", "TGA"}
    atg_count = 0

    for i in range(len(seq) - 2):
        codon = seq[i:i+3].upper()
        codon_clean = codon.replace("-", "")
        if codon_clean == "ATG":
            atg_count += 1
            if not use_second_atg or atg_count == 2:
                # Found the target ATG (first or second)
                start = i
                codon_buffer = ""
                codon_indices = []
                for j in range(i, len(seq)):
                    codon_buffer += seq[j]
                    codon_indices.append(j)
                    if len(codon_buffer.replace("-", "")) == 3:
                        codon_clean = codon_buffer.replace("-", "").upper()
                        if codon_clean in stop_codons:
                            end = codon_indices[-1]
                            return (start, end + 1)  # +1 to include stop codon
                        codon_buffer = ""
                        codon_indices = []
                break  # Exit if no stop codon is found
    return None  # No valid ATG-stop pair found

def find_cds_in_aligned_sequence(seq: str, start_idx: int, end_idx: int) -> str:
    """
    Extract the CDS region (from start to end) from an aligned sequence (with gaps).
    """
    return seq[start_idx:end_idx]

def process_fasta(input_fasta: str, output_fasta: str, use_second_atg: bool):
    """
    Main logic for processing aligned sequences.
    Use the first sequence to determine CDS coordinates, then extract the same region from all sequences.
    """
    records = list(SeqIO.parse(input_fasta, "fasta"))
    if not records:
        print("No sequences found in input.")
        return

    ref_seq = str(records[0].seq)
    pos = find_first_or_second_atg_with_stop(ref_seq, use_second_atg)
    if not pos:
        print("No valid ATG and stop codon pair found in reference sequence.")
        return

    start_idx, end_idx = pos
    print(f"[Info] Using CDS region: {start_idx} to {end_idx} (from reference sequence)")

    output_records = []
    for record in records:
        cds = find_cds_in_aligned_sequence(str(record.seq), start_idx, end_idx)
        new_record = SeqRecord(
            seq=Seq(cds),  # Wrap as Seq object for compatibility with Biopython
            id=record.id,
            description="CDS extracted from alignment"
        )
        output_records.append(new_record)

    SeqIO.write(output_records, output_fasta, "fasta")
    print(f"[Done] Extracted CDS saved to {output_fasta}")

def main():
    """
    Parse command-line arguments and run the CDS extraction pipeline.
    """
    parser = argparse.ArgumentParser(description="Extract aligned CDS from multiple sequences using reference ATG position")
    parser.add_argument("-i", "--input", required=True, help="Input aligned FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file with CDS")
    parser.add_argument("-s", "--second_atg", action="store_true", help="Use second ATG in first sequence as start codon")
    args = parser.parse_args()

    process_fasta(args.input, args.output, args.second_atg)

if __name__ == "__main__":
    main()
