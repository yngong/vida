1. load the metadata (as a CSV file) to split fasta files into species level and extracted classification mapping saved to: classification_mapping.csv
    * ```python extract_metadata.py alpha.csv```

2. split fasta file based on classification_mapping.csv
    * ```python split_fasta.py alpha.fasta classification_mapping.csv```

3. select the longest one genome as a coordinate:
    * ```python ../find_longest_fasta.py Human_coronavirus_229E.fasta```

```
Bat_coronavirus_HKU10.fasta

✅ Longest sequence: accn|OQ297725
🔹 Length: 28586
🧬 Sequence (first 100 bp): TGGTTGGTTGCTGTTCTCCAACTCCAACTACTTTTTAGGTGAGTTGKATCTTACTTTTGGCAATCGCGGTGGTACCACTGTTGTGATTTTCTATCTGCGG...

Rhinolophus_bat_coronavirus_HKU2.fasta

✅ Longest sequence: accn|MH697599
🔹 Length: 27183
🧬 Sequence (first 100 bp): CACTTAAAGATATAATCTATCTGTCGATAGAGTCCTTATCTTTTTAGACTTTCCAGTCTACTCTTCTCAACTAAACGAAATTTACGTCTTTTTGTGTATG...

Wencheng_Sm_shrew_coronavirus.fasta

✅ Longest sequence: accn|KY967725
🔹 Length: 26042
🧬 Sequence (first 100 bp): TAATAGAGAAAATAGTGCGTGTACGTGCTGTTGTGTACTCTGTTTTCGAGCTTGTCTCGTCTTCTCAAAACTAAACGAAATTTGTAAAATACACATGTGT...
```

4. (manually) donwload gene features (as a gff3 file) from NCBI

5. do multiple sequence alignment (MSA)

```
for i in `ls *.fasta`
do
	mkdir `echo $i | cut -d"." -f1`
	cd `echo $i | cut -d"." -f1`
	cp ../`echo $i | cut -d"." -f1`*.fa* ./
	mafft $i > `echo $i | cut -d"." -f1`_aligned.fas
cd ../
done
```

6. split MSA
	* ```python ../extract_genes.py Wencheng_Sm_shrew_coronavirus_aligned.fas KY967725 ../KY967725.gff3```
	* ```python ../extract_genes.py Rhinolophus_bat_coronavirus_HKU2_aligned.fas MH697599 ../MH697599.gff3```
	* ```python ../extract_genes.py Bat_coronavirus_HKU10_aligned.fas OQ297725 ../OQ297725.gff3```

7. remove partial sequences (e.g., <97% of RdRp gene)
	* ```python filter_low_quality_seq.py S.fasta 3```

8. calculate sequence identities
    * ``` python identity_histogram.py split_fasta/Bat_coronavirus_HKU10/qualified.fasta split_fasta/Rhinolophus_bat_coronavirus_HKU2/qualified.fasta split_fasta/Wencheng_Sm_shrew_coronavirus/qualified.fasta ```
    * ``` ```