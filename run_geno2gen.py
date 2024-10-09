from basic.geno2gen import sars2
from basic.geno2gen import ev_aa
from basic.geno2gen import e11_aa

pos = 390
# gene, gene_pos = sars2_pos(pos)
# print(f"Gene: {gene}")
# print(f"Gene Position: {gene_pos}")

# gene, gene_pos = ev_aa_pos(pos)
# print(f"Gene-Position: {gene}-{gene_pos}")

gene, gene_pos = e11_aa(pos)
print(f"Gene-Position: {gene}-{gene_pos}")
