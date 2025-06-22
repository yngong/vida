# Directory structure to be assumed:
# project_root/
# ├── setup.py
# ├── README.md
# ├── vida/
# │   ├── __init__.py
# │   ├── remove_punct.py
# │   ├── split_gisaid_by_segment.py
# │   ├── filter_fasta_by_n_content.py
# │   ├── downsampling_gisaid.py
# │   ├── filter_complete_genomes.py
# │   ├── get_seq_by_list.py
# │   ├── rename_fasta_header.py
# │   ├── extract_cds.py
# │   ├── restore_fasta_header.py
# │   └── combine_two_files.py

# Each script in vida/ should contain a main() function and the standard:
# if __name__ == "__main__":
#     main()

# setup.py:
from setuptools import setup, find_packages

setup(
    name="vida",
    version="0.1.0",
    author="Yu-Nong Gong",
    author_email="your.email@example.com",
    description="Virus Data Analysis Toolkit (VIDA)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vida",  # replace with actual repo
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],  # fill in if needed (e.g., biopython)
    entry_points={
        'console_scripts': [
            'vida-remove-punct=vida.remove_punct:main',
            'vida-split-segment=vida.split_gisaid_by_segment:main',
            'vida-filter-N=vida.filter_fasta_by_n_content:main',
            'vida-downsample=vida.downsampling_gisaid:main',
            'vida-filter-complete=vida.filter_complete_genomes:main',
            'vida-get-seq=vida.get_seq_by_list:main',
            'vida-rename-header=vida.rename_fasta_header:main',
            'vida-extract-cds=vida.extract_cds:main',
            'vida-restore-header=vida.restore_fasta_header:main',
            'vida-combine-files=vida.combine_two_files:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)
