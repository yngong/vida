# VIDA: Virus Data Analysis Toolkit

**VIDA** (Virus Data Analysis Toolkit) is a modular and extensible toolkit for analyzing viral sequences and phylogenies. It includes streamlined workflows for structure prediction, multiple sequence alignment, tree building, and visualization, especially designed for RNA viruses like Influenza, SARS-CoV-2, and Enterovirus.

---

## 🚀 Features

- Fast multiple sequence alignment with MAFFT
- Rapid phylogenetic tree inference with FastTree
- Seamless integration with Nextclade for clade assignment
- Structural annotation and docking (via optional plugins)
- Extensible Python modules for sequence parsing and batch processing
- Ready-to-use CLI and visualization functions

---

## 🛠️ Installation

## Clone and install locally (development mode)

**Prerequisites**:
Before proceeding, ensure you have either **[Conda](https://docs.conda.io/en/latest/miniconda.html)** or **[Mamba](https://mamba.readthedocs.io/en/latest/)** installed on your system.

If not, install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or use [Micromamba](https://mamba.readthedocs.io/en/latest/installation.html) as a lightweight alternative.

---

1. **Clone the repository:**

```bash
git clone https://github.com/yngong/vida.git
cd vida
```

2. **(Optional but recommended) Install Mamba in the base environment:**

```bash
conda install -n base -c conda-forge mamba
```

3. **Create and activate the environment:**

```bash
mamba env create -f vida_env.yml
conda activate vida
```

4. **Install the package in development mode:**

```bash
pip install -e .
```

This installs `vida` as an editable Python package. Any changes you make to the source code will be reflected immediately without reinstalling.

---

## Package Structure

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

## Usage

Each module can be executed using the command-line interface:

```bash
python -m vida.<module_name> [options]
```

### Examples

1. **Remove punctuation from FASTA headers:**

```bash
python -m vida.remove_punct -i input.fasta -o output.fasta
```

2. **Rename headers for alignment:**

```bash
python -m vida.rename_fasta_header -i aligned.fas -o renamed.fas -m renamed.map
```

---

## Example Workflow (run\_flu\_pipeline.sh)

1. Clean original FASTA and split by segment
2. Filter sequences (high N content, non-full-length genomes)
3. Subsample by region or time
4. Align using MAFFT
5. Build trees using FastTree
6. Annotate clades using Nextclade
7. Integrate clade and metadata info into summary reports

---

## Authors & Contributions

Developed by the laboratory of [Yu-Nong Gong](https://example.com), focused on RNA virus evolution and surveillance. Contributions via pull requests or issues are welcome.

---

## License

MIT License
