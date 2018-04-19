
dna_str = open('datasets/rosalind_dna.txt').read().strip()

nucleotides = {}
nucleotides_sorted = []

for c in dna_str:
    if not nucleotides.has_key(c):
        nucleotides[c] = 0
    nucleotides[c] += 1

for key in sorted(nucleotides.iterkeys()):
    nucleotides_sorted.append(nucleotides[key])

print nucleotides_sorted
