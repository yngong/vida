# VIDA: Virus Data Analysis Toolkit

**VIDA** (Virus Data Analysis Toolkit) is a modular and extensible Python package designed for preprocessing and analyzing viral genomic sequences. It includes a collection of reusable Python modules for data cleaning, filtering, alignment preparation, and CDS extraction of genomic sequences. In addition to the Python tools, I also provide accompanying shell scripts to automate the influenza genome analysis pipeline.

---

## 🚀 Features (Python Modules)

* **FASTA Header Cleaning**  
  Remove punctuation from headers (except `|`, `>`, `/`, `-`, `_`) to ensure downstream compatibility.  
  *File: `vida/remove_punct.py`*

* **Header Renaming & Restoration**  
  Rename headers for clean alignments, and restore them post-analysis using mapping files.  
  *Files: `vida/rename_fasta_header.py` and `vida/restore_fasta_header.py`*

* **Segment Splitting**  
  Split multi-segment FASTA files (e.g., from GISAID) into separate files by segment.  
  *File: `vida/split_gisaid_by_segment.py`*

* **List-Based Selection**  
  Extract specific sequences from a FASTA file based on a predefined list.  
  *File: `vida/get_seq_by_list.py`*

* **N-content Filtering**  
  Filter sequences with excessive ambiguous bases (`N`) using a custom threshold.  
  *File: `vida/filter_n_content.py`*

* **Completeness Check**  
  Detect and filter out incomplete viral genomes.  
  *File: `vida/filter_complete_genomes.py`*

* **Downsampling**  
  Subsample sequences (e.g., by region or time) using controlled stratified sampling.  
  *File: `vida/downsampling_gisaid.py`*

* **CDS Extraction**  
  Extract coding sequences based on alignment or reference structure.  
  *File: `vida/extract_cds.py`*

* **Two-File Combining Utility**  
  Merge tabular files (e.g., clade and metadata) into a single report.  
  *File: `vida/combine_two_files.py`*

* **Modular CLI Design**  
  Each tool is available as a standalone module under `vida`, e.g., `python -m vida.remove_punct`

---

## 🛠️ Installation

### Prerequisites

Ensure you have either [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Mamba](https://mamba.readthedocs.io/en/latest/) installed. We recommend [Micromamba](https://mamba.readthedocs.io/en/latest/installation.html) for lightweight environments.

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

## 📃 Example Shell Workflow: 

This shell script `run_flu_pipeline.sh` in flu folder provides an end-to-end analysis pipeline:

1. Clean FASTA headers
2. Split sequences by segment
3. Filter by `N` content and completeness
4. Subsample to reduce dataset size
5. Align with MAFFT
6. Build phylogenetic trees with FastTree
7. Assign clades using Nextclade
8. Rename and restore headers
9. Combine clade and metadata for downstream visualization

⚠️ FastTree Recommendation: For accurate phylogenetic inference, we recommend compiling the double-precision version of FastTree from the official source instead of using precompiled binaries.

📦 Output and additional files for running CatTrees app:

* Phylogenetic Trees
	* Location: 2_trees/restored_\*.nwk
	* Description: Newick-format tree files containing clade-assigned, header-restored phylogenies for each segment.

* Clade Assignments
  * Location: 3_clade_designation/clade.csv
  * Description: CSV file with Nextclade-assigned clades, sequence IDs, and quality metrics.

* Additional file needed for running CatTrees app
  * A list of reassortment strain
  * Description: one column file with reassortment strains. Please make sure "strain" as the header line.

---

## ⚙️ flu folder
* raw/ Contains the original input sequences and directory structures prior to processing. This can be used to replicate the full test pipeline.

* ack_table/Supplementary Table 1_acknowledgement_table.xlsx Supplementary Table 1 in our manuscript. We gratefully acknowledge the authors, originating and submitting laboratories of the sequences from GISAID’s EpiFlu™ Database on which this research is based.

## 👨‍💼 Author & Contributions

VIDA is developed and maintained by [Yu-Nong Gong](https://example.com). Contributions are welcome!

This toolkit was applied in the manuscript titled "Visualizing and Deciphering Influenza A(H1N1)pdm09 Reassortment in the 2019–2023 Seasons", which is currently under review. The work demonstrates the utility of VIDA in analyzing reassortment patterns in influenza viruses.

---

## 📚 License

This project is licensed under the MIT License.

> MIT License allows reuse, modification, and distribution with minimal restrictions. It's compatible with both open and closed-source use cases.
