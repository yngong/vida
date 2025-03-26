import matplotlib.pyplot as plt
from Bio import SeqIO, Align
import itertools
import sys
import pandas as pd
from tqdm import tqdm  # Progress bar support

# Initialize the aligner with high gap penalties for strict local alignment
aligner = Align.PairwiseAligner()
aligner.mode = "local"
#aligner.match_score = 2
#aligner.mismatch_score = -1
aligner.open_gap_score = -5
aligner.extend_gap_score = -1

def load_sequences(file):
    """Load sequences from a FASTA file and return a list of sequences."""
    return [str(rec.seq) for rec in SeqIO.parse(file, "fasta")]

def sequence_identity(seq1, seq2):
    """Compute sequence identity using PairwiseAligner."""
    alignments = aligner.align(seq1, seq2)
    best_alignment = alignments[0]  # Get the best alignment
    aligned_seq1, aligned_seq2 = str(best_alignment[0]), str(best_alignment[1])  # Extract aligned sequences

    # Calculate sequence identity (matches / total aligned positions)
    matches = sum(1 for i, j in zip(aligned_seq1, aligned_seq2) if i == j)
    total = sum(1 for i, j in zip(aligned_seq1, aligned_seq2) if i != "-" and j != "-")
    return matches / total if total > 0 else 0  # Avoid division by zero

def compute_identities(files, output_csv="sequence_identities.csv"):
    """Compute intra-group and inter-group sequence identities and save to a CSV file."""
    groups = {file: load_sequences(file) for file in files}
    intra_identities = []
    inter_identities = []

    # Compute intra-group identities
    print("\n🔹 Computing intra-group sequence identities...")
    for group, sequences in groups.items():
        for s1, s2 in tqdm(itertools.combinations(sequences, 2), 
                           total=len(sequences) * (len(sequences) - 1) // 2, 
                           desc=f"Intra {group}"):
            identity = sequence_identity(s1, s2)
            intra_identities.append(["Intra", group, identity])

    # Compute inter-group identities
    print("\n🔹 Computing inter-group sequence identities...")
    group_names = list(groups.keys())
    total_inter_comparisons = sum(len(groups[g1]) * len(groups[g2]) for i, g1 in enumerate(group_names) 
                                  for g2 in group_names[i+1:])

    with tqdm(total=total_inter_comparisons, desc="Inter-group", unit=" pair") as pbar:
        for i in range(len(group_names)):
            for j in range(i + 1, len(group_names)):
                file1, file2 = group_names[i], group_names[j]
                for s1 in groups[file1]:
                    for s2 in groups[file2]:
                        identity = sequence_identity(s1, s2)
                        inter_identities.append(["Inter", f"{file1} vs {file2}", identity])
                        pbar.update(1)

    # Save results to CSV
    df = pd.DataFrame(intra_identities + inter_identities, columns=["Type", "Group", "Identity"])
    df.to_csv(output_csv, index=False)
    print(f"\n✅ Sequence identities saved to: {output_csv}")

    return intra_identities, inter_identities

def plot_histogram(csv_file):
    """Load sequence identities from CSV and plot a histogram."""
    df = pd.read_csv(csv_file)

    # Drop NaN values to avoid plotting errors
    df = df.dropna(subset=["Identity"])

    plt.figure(figsize=(8, 6))

    # Convert Identity column to numeric format (ensuring proper plotting)
    df["Identity"] = pd.to_numeric(df["Identity"], errors="coerce")

    # Separate intra-group and inter-group identity values
    intra_df = df[df["Type"] == "Intra"]
    inter_df = df[df["Type"] == "Inter"]

    # Ensure that at least one group has data to plot
    if not intra_df.empty:
        plt.hist(intra_df["Identity"], bins=20, alpha=0.5, label="Intra-group", color="blue")
    if not inter_df.empty:
        plt.hist(inter_df["Identity"], bins=20, alpha=0.5, label="Inter-group", color="green")

    plt.xlabel("Sequence Identity")
    plt.ylabel("Frequency")
    plt.title("Histogram of Sequence Identities (Inter- and Intra-group)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python identity_histogram.py file1.fasta file2.fasta [file3.fasta ...]")
        sys.exit(1)

    fasta_files = sys.argv[1:]
    compute_identities(fasta_files)

    # Ensure histogram is plotted after computing sequence identities
    plot_histogram("sequence_identities.csv")
