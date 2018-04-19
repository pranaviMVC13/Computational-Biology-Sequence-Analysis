'''To count the number of optimal edit alignments of strings v and w'''
#Calculating the score the same way as in edit distance a

def count_opt_alignments(s1, s2):

    # for 2D arrays
    from numpy import zeros

    # Initialize the matrices
    SM = zeros((len(s1)+1, len(s2)+1), dtype=int)
    opt_align_count = zeros((len(s1)+1, len(s2)+1), dtype=int)
    mod = 2 ** 27 - 1

    for i in xrange(0, len(s1)+1):
        SM[i][0] = i
        opt_align_count[i][0] = 1
    for j in xrange(1, len(s2)+1):
        SM[0][j] = j
        opt_align_count[0][j] = 1

    # Calculate the score
    for i in xrange(1, len(s1)+1):
        for j in xrange(1, len(s2)+1):
            scores = [SM[i-1][j-1] + (s1[i-1] != s2[j-1]), SM[i-1][j]+1, SM[i][j-1]+1]
            SM[i][j] = min(scores)

            opt_align_count[i][j] += [0, opt_align_count[i-1][j-1]][scores[0] == SM[i][j]]
            print SM[i][j]
            print opt_align_count
            opt_align_count[i][j] += [0, opt_align_count[i-1][j]][scores[1] == SM[i][j]]
            opt_align_count[i][j] += [0, opt_align_count[i][j-1]][scores[2] == SM[i][j]]

            # Take the mod and store
            opt_align_count[i][j] = opt_align_count[i][j]  % mod

    return opt_align_count[len(s1)][len(s2)]

if __name__ == '__main__':

    str1 = "PLEASANTLY"
    str2 = "MEANLY"
    count = str(count_opt_alignments(str1, str2))

    # Parse the input data.
    """sample_dataset = open('datasets/rosalind_ctea.txt').read()
    strings = []
    seq =""
    name = ""
    for line in sample_dataset.strip().split():

        if line.startswith(">"):
            strings.append(''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    strings.append(''.join(seq))
    strings.pop(0)

    count = str(count_opt_alignments(strings[0], strings[1]))"""
    print count