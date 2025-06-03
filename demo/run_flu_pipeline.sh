# Move to the raw data directory
cd 0_raw

# Step 1: Remove unwanted punctuation from FASTA headers
python -m vida.remove_punct -i gisaid_epiflu_sequence.fasta -o output.fas

# Step 2: Split GISAID multi-segment FASTA into individual segments
python -m vida.split_gisaid_by_segment -i output.fas -d segment

# Step 3: Filter HA segment by N content threshold
python -m vida.filter_fasta_by_N_content -i segment/HA.fas -t 3 -k Kept_HA.fas -r Removed_HA.fas

# Step 4: Downsample the HA sequences
python -m vida.downsampling_gisaid -i Kept_HA.fas -c 2 -o passed_HA.fas

# Step 5: Replace raw HA with passed HA and filter for complete genomes
cd segment
mv HA.fas raw_HA.fas
cp ../passed_HA.fas HA.fas
python -m vida.filter_complete_genomes -o ../new
cd ..

# Step 6: Run Nextclade on the filtered HA sequences
nextclade dataset get --name 'flu_h1n1pdm_ha' --output-dir '../3_clade_designation/flu_h1n1pdm_ha'
nextclade run \
  -D ../3_clade_designation/flu_h1n1pdm_ha \
  -O ../3_clade_designation \
  new_HA.fas

cd ..

# Step 7: Copy and rename the processed segment FASTA files
cd 1_alignment
cp ../0_raw/new_*.fas ./
for i in *.fas; do
  mv "$i" "$(echo $i | cut -d'_' -f2)"
done

# Step 8: For each segment
for i in *.fas; do
  # Extract sequences listed in selected.list
  python -m vida.get_seq_by_list -i "$i" -l selected.list -o "$(basename "$i" .fas)"_sub.fas

  # Align the subset sequences using MAFFT
  mafft --anysymbol "$(basename "$i" .fas)"_sub.fas > "$(basename "$i" .fas)"_align.fas

  # Rename FASTA headers and save the mapping
  python -m vida.rename_fasta_header \
    -i "$(basename "$i" .fas)"_align.fas \
    -o "Renamed_$(basename "$i" .fas)"_align.fas \
    -m "$(basename "$i" .fas)"_align.map
done

# Step 9: Simplify the header maps for tree labeling
for i in *.map; do
  cut -d"|" -f1,2,3 "$i" | sed 's/|/_/g' > "$(basename "$i" .map)"_new.map
done

cd ..

# Step 10: Generate trees from aligned sequences
cd 2_trees
cp ../1_alignment/Renamed_*_align.fas ./

for i in Renamed_*_align.fas; do
  # Extract coding sequences
  python -m vida.extract_cds -i "$i" -o "$(basename "$i" .fas)"_output.fasta

  # Build maximum-likelihood tree using FastTree
  fasttree -gtr -nt < "$(basename "$i" .fas)"_output.fasta > "$(echo $i | cut -d"_" -f2).nwk"
done

# Step 11: Restore original FASTA headers in tree files
for i in *.nwk; do
  python -m vida.restore_fasta_header \
    -i "$i" \
    -o "Restored_$i" \
    -m ../1_alignment/"$(basename "$i" .nwk)"_align_new.map
done

cd ..

# Step 12: Generate clade designation table
cd 3_clade_designation

# Extract strain names and clade info from Nextclade results
for i in $(cat ../1_alignment/selected.list); do
  grep "$i""|" nextclade.csv | cut -d";" -f2 | cut -d"|" -f1,2,3 | sed 's/|/_/g' >> strainname
  grep "$i""|" nextclade.csv | cut -d";" -f3 >> clade
done

# Combine strain names with clades
python -m vida.combine_two_files -i strainname -j clade -o Comb_strainname

# Format final output
echo -e "Taxa\tClade" > clade.tsv
cat Comb_strainname >> clade.tsv

# Clean up intermediate files
rm Comb_strainname clade strainname

cd ..
