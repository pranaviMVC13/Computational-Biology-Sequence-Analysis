CODON_LOOKUP = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def protein_string(input):

    "seperating the dns_string and introns given in the input"

    dna_str = ''
    introns = []
    dna_str_del = []

    split_input = input.split()
    a = split_input.pop(0)

    for i in range(len(split_input)):
        if split_input[i].startswith('>R'):
            break
        dna_str = dna_str + split_input[i]
        dna_str_del.append(split_input[i])


    for s in dna_str_del:
        split_input.remove(s)

    for s in split_input:
        if s.startswith('>R'):
          split_input.remove(s)

    introns = split_input

    "replacing the intron substring with '' "
    for intron in introns:
        dna_str = dna_str.replace(intron, '')

    prot_str = ''
    "replacing the values in dna_string from codon lookup"
    for i in range(0, len(dna_str), 3):
        codon = CODON_LOOKUP[dna_str[i:i+3]]
        if codon == 'Stop' or codon == '-':
            break;
        prot_str += codon
    return ''.join(list(prot_str))


if __name__ == "__main__":
    sample_dataset = open('datasets/rosalind_splc.txt').read().strip()

    print protein_string(sample_dataset)