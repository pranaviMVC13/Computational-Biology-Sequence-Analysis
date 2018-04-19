'''To get the max number of gap symbols in an optimal alignment of two strings'''
# Find thr length of the longest common subsequence.
def Maximum_Gap_Symbols(s, t):

    LCS = [[0 for j in xrange(len(t)+1)] for i in xrange(len(s)+1)]

    for i in xrange(len(s)):
        for j in xrange(len(t)):
            if s[i] == t[j]:
                LCS[i+1][j+1] = LCS[i][j]+1
            else:
                LCS[i+1][j+1] = max(LCS[i+1][j],LCS[i][j+1])

    # sum of length of strings - 2(length of longest common sub sequence)
    return len(s) + len(t) - 2*LCS[len(s)][len(t)]


if __name__ == '__main__':


    # Parse the input data.
     sample_dataset = open('datasets/rosalind_mgap.txt').read()
     strings = []
     seq = ""
     for line in sample_dataset.strip().split():

         if line.startswith(">"):
             strings.append(''.join(seq))
             name, seq = line, []
         else:
             seq.append(line)
     strings.append(''.join(seq))
     strings.pop(0)

    #v = "AACGTA"
    #w = "ACACCTA"
    #max_gaps = str(Maximum_Gap_Symbols(v, w))

    # Get the maximum number of gaps.
     max_gaps = str(Maximum_Gap_Symbols(strings[0],strings[1]))
     print max_gaps