## finding hamming distace
def hamm_dist(x, y):
    sum = 0;
    for i in range(len(x)):
        if (x[i] != y[i]):
            sum=sum+1
    return sum

## finding the reverse compliment of a string
def rev_comp(sequence):
    rev = ''
    for c in sequence[::-1]:
        rev += "GCAT"["CGTA".find(c)]
    return rev

## correcting the reads
def error_correction(not_found , found):
    for x in not_found:
        for y in found:
            if x == y:
                continue
            if hamm_dist(x, y) == 1:
                print(x + '->' + y)
                break
            if hamm_dist(x, rev_comp(y)) == 1:
                print(x + '->' + rev_comp(y))
                break

if __name__ == "__main__":

    strings = []
    sample_data_obj = open('datasets/rosalind_corr.txt')
    for line in sample_data_obj:
        strings.append(line.strip())

    i = 0
    found = []
    not_found = []
    while i < len(strings):
        if strings[i] in strings[i + 1:] or rev_comp(strings[i]) in strings:
            found.append(strings[i])
            strings = [string for string in strings if string != strings[i] and
                    string != rev_comp(strings[i])]
        else:
            not_found.append(strings[i])
            i += 1

    error_correction(not_found , found)