# Virus Informatics and Data Analysis (VIDA)

## Overview
Virus Informatics and Data Analysis (VIDA) is a collection of Python scripts designed for viral bioinformatics analysis. This repository provides tools for sequence processing, quality control, genome annotation, and comparative genomics, with a focus on Next-Generation Sequencing (NGS) data and phylogenetics.

## Scripts

### 1. **FASTA Quality Control**
- **Function:** Reads a FASTA file and filters sequences based on a user-defined cutoff for non-ATCG characters.
- **Input:** FASTA file, cutoff percentage (e.g., 3%)
- **Output:** Two FASTA files: one for qualified sequences and another for sequences exceeding the cutoff.

### 2. **FASTA Accession Extraction**
- **Function:** Extracts accession numbers from a FASTA file, using metadata from a CSV file for additional annotations.
- **Input:** FASTA file, metadata CSV
- **Output:** A mapping of accession numbers with metadata.

### 3. **Gene Extraction from MSA**
- **Function:** Uses a reference genome’s GFF3 file to extract genes from an MSA (Multiple Sequence Alignment), handling gaps appropriately.
- **Input:** MSA file, reference genome, GFF3 annotation file
- **Output:** Individual FASTA files for each gene.

### 4. **Sequence Classification Based on Metadata**
- **Function:** Categorizes sequences based on metadata fields and outputs classified/unclassified counts.
- **Input:** FASTA file, metadata CSV
- **Output:** Classified sequences stored in separate files, with unclassified sequences in a separate file.

### 5. **Longest Sequence Finder**
- **Function:** Identifies the longest sequence in a FASTA file.
- **Input:** FASTA file
- **Output:** The longest sequence with its metadata.

## Usage
Each script includes a usage message if incorrect input is provided or if only the script name is executed. Ensure that Biopython and other dependencies are installed before running the scripts.

```sh
python script.py <input_file> [additional parameters]
```

## Dependencies
- Python 3
- Biopython
- Pandas (for metadata processing)

## Contributing
Contributions are welcome! Feel free to submit pull requests for bug fixes, enhancements, or new tools related to viral bioinformatics.

## License
MIT License

---
This repository aims to support researchers working on viral genomics, phylogenetics, and epidemiology by providing automated, efficient, and reproducible workflows.


