# VIDA: Virus Data Analysis Toolkit

**VIDA** (Virus Data Analysis Toolkit) is a modular and extensible Python package designed for the analysis of viral genomic sequences and phylogenies. It offers streamlined CLI tools for preprocessing, alignment, and tree-building, specifically geared towards RNA viruses like Influenza, SARS-CoV-2, and Enterovirus.

---

## 🚀 Features (Python Modules)

* 🧬 **FASTA Header Cleaning**
  Remove punctuation from headers (except `|`, `>`, `/`, `-`, `_`) to ensure downstream compatibility.

* 🔹 **Segment Splitting**
  Split multi-segment FASTA files (e.g., from GISAID) into separate files by segment.

* 💩 **N-content Filtering**
  Filter sequences with excessive ambiguous bases (`N`) using a custom threshold.

* 🔽 **Downsampling**
  Subsample sequences (e.g., by region or time) using controlled stratified sampling.

* 🎮 **Completeness Check**
  Detect and filter out incomplete viral genomes.

* 🧬 **CDS Extraction**
  Extract coding sequences based on alignment or reference structure.

* 📃 **Header Renaming & Restoration**
  Rename headers for clean alignments, and restore them post-analysis using mapping files.

* 🔢 **List-Based Selection**
  Extract specific sequences from a FASTA file based on a predefined list.

* 📂 **Two-File Combining Utility**
  Merge tabular files (e.g., clade and metadata) into a single report.

* ⚙️ **Modular CLI Design**
  Each tool is available as a standalone module under `vida`, e.g., `python -m vida.remove_punct`

---

## 🛠️ Installation

### Prerequisites

Ensure you have either [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Mamba](https://mamba.readthedocs.io/en/latest/) installed.
We recommend [Micromamba](https://mamba.readthedocs.io/en/latest/installation.html) for lightweight environments.

### Clone and Install (Development Mode)

```bash
# 1. Clone the repository
git clone https://github.com/yngong/vida.git
cd vida

# 2. (Optional) Install Mamba
conda install -n base -c conda-forge mamba

# 3. Create and activate the environment
mamba env create -f vida_env.yml
conda activate vida

# 4. Install VIDA as an editable package
pip install -e .
```

> This installs `vida` as an editable Python package. Any changes to the source code will take effect immediately.

---

## 📁 Package Structure

```
vida/
├── __init__.py
├── remove_punct.py
├── split_gisaid_by_segment.py
├── filter_fasta_by_N_content.py
├── downsampling_gisaid.py
├── filter_complete_genomes.py
├── get_seq_by_list.py
├── rename_fasta_header.py
├── extract_cds.py
├── restore_fasta_header.py
├── combine_two_files.py
```

---

## ⚖️ Usage

Run each module using Python's `-m` flag:

```bash
python -m vida.<module_name> [options]
```

### Examples

```bash
# Remove punctuation from FASTA headers
python -m vida.remove_punct -i input.fasta -o output.fasta

# Rename headers for clean alignments
python -m vida.rename_fasta_header -i aligned.fas -o renamed.fas -m renamed.map

# Filter by N-content
python -m vida.filter_fasta_by_N_content -i input.fas -t 3 -k kept.fas -r removed.fas
```

---

## 📃 Example Shell Workflow: `run_flu_pipeline.sh`

This shell script provides an end-to-end analysis pipeline:

1. Clean FASTA headers
2. Split sequences by segment
3. Filter by `N` content and completeness
4. Subsample to reduce dataset size
5. Align with MAFFT
6. Build phylogenetic trees with FastTree
7. Assign clades using Nextclade
8. Rename and restore headers
9. Combine clade and metadata for downstream visualization

---

## 👨‍💼 Author & Contributions

Developed and maintained by the laboratory of [Yu-Nong Gong](https://example.com), focusing on viral evolution and genomic epidemiology.

Contributions are welcome! Please use GitHub Issues or submit a pull request.

---

## 📚 License

This project is licensed under the MIT License.

> MIT License allows reuse, modification, and distribution with minimal restrictions. It's compatible with both open and closed-source use cases.
