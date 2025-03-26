import sys
from Bio import SeqIO

def parse_gff3(gff3_file):
    """
    Parse GFF3 file to extract gene coordinates and product names, specifically for CDS.
    """
    gene_table = {}
    
    with open(gff3_file) as f:
        for line in f:
            if line.startswith("#"):  # Skip comment lines
                continue
            fields = line.strip().split("\t")
            if len(fields) < 9:
                continue  # Skip invalid lines
            
            seq_id, source, feature, start, end, _, strand, phase, attributes = fields
            start, end = int(start), int(end)
            
            # Process only CDS features
            if feature == "CDS":
                attributes_dict = {attr.split("=")[0]: attr.split("=")[1] for attr in attributes.split(";")}
                
                # Extract gene and product info, with fallback to 'unknown_gene' if gene is missing
                gene_name = attributes_dict.get("gene", attributes_dict.get("product", "unknown_gene"))
                product_name = attributes_dict.get("product", "unknown_product")
                
                if gene_name not in gene_table:
                    gene_table[gene_name] = []
                gene_table[gene_name].append((start, end, seq_id, strand, product_name))
    
    return gene_table

def map_genome_to_alignment(reference_seq):
    """
    Create a mapping from genome positions to alignment indices.
    """
    genome_pos = 0
    mapping = {}  # {Genome position -> Alignment index}
    
    for align_idx, nucleotide in enumerate(reference_seq.seq):
        if nucleotide != "-":  # Only count actual nucleotides
            genome_pos += 1
            mapping[genome_pos] = align_idx
    
    return mapping

def extract_gene_regions(msa_file, ref_id, gff3_file):
    """
    Extract CDS gene regions from an MSA based on a reference sequence.
    """
    msa_records = list(SeqIO.parse(msa_file, "fasta"))
    
    # Find the reference sequence
    reference_seq = next((rec for rec in msa_records if ref_id in rec.id), None)
    if not reference_seq:
        print(f"⚠️ Reference sequence '{ref_id}' not found in MSA!")
        sys.exit(1)

    print(f"🔹 Using reference: {reference_seq.id} ({len(reference_seq.seq.replace('-', ''))} bp)")  # Update here

    # Parse GFF3 file
    gene_table = parse_gff3(gff3_file)

    # Create mapping from genome position to alignment index
    mapping = map_genome_to_alignment(reference_seq)

    # Extract gene regions
    for gene_name, regions in gene_table.items():
        for start, end, seq_id, strand, product_name in regions:
            if start not in mapping or end not in mapping:
                print(f"⚠️ Skipping {gene_name}: Position not found in alignment!")
                continue

            align_start = mapping[start]
            align_end = mapping[end]

            # Use gene name (or fallback to product) as the file name
            output_file = f"{gene_name}.fasta"
            with open(output_file, "w") as out_f:
                for record in msa_records:
                    gene_seq = record.seq[align_start:align_end].replace("-", "")  # Update here to remove gaps
                    out_f.write(f">{record.id}\n{gene_seq}\n")

            print(f"✅ Saved {output_file} [{align_start} - {align_end}]")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_genes.py <msa.fasta> <reference_id> <gff3_file>")
        sys.exit(1)

    msa_file = sys.argv[1]
    reference_id = sys.argv[2]  # e.g., "OQ297725"
    gff3_file = sys.argv[3]

    extract_gene_regions(msa_file, reference_id, gff3_file)
