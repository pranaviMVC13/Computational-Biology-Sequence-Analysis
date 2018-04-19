"Dictonary table for frequencies"
codon_freq = {'F':2, 'L':6, 'S':6, 'Y':2, 'Stop':3, 'C':2, 'W':1, 'P':4, 'H':2, 'Q':2, 'R':6, 'I':3, 'M':1, 'T':4,
              'N':2, 'K':2, 'V':4, 'A':4, 'D':2, 'E':2, 'G':4}

dataset = open('datasets/rosalind_mrna.txt').read().strip()

"""Number of RNA strings"""
count = codon_freq['Stop'] ;    "stop codon - termination of translation"
for codon in dataset:
    count = count * codon_freq[codon]

n_rna = count % 1000000
print n_rna