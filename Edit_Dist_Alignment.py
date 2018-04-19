import numpy as np

def cost( t, s):
        return (0 if t == s else 1)

def Edit_Dist_Alignment(t, s):
        n = len(t)
        m = len(s)

        edit_dist = np.zeros((n + 1, m + 1))
        back_trace = np.zeros((n + 1, m + 1), dtype=int)
        back_trace[0, 1:] = 1
        back_trace[1:, 0] = 1

        for i in xrange(1, n + 1):
            edit_dist[i, 0] = edit_dist[i - 1, 0] + 1
        for j in xrange(1, m + 1):
            edit_dist[0, j] = edit_dist[0, j - 1] + 1

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                d = [edit_dist[i - 1, j] + 1, \
                     edit_dist[i - 1, j - 1] + cost(s[j - 1], t[i - 1]), \
                     edit_dist[i, j - 1] + 1]
                edit_dist[i, j] = min(d)
                back_trace[i, j] = 1 + np.argmin(d)

        min_score = edit_dist[i,j]
        # backtrace
        Strings_new = [[], []]
        i = n
        j = m

        while i != 0 or j != 0:
            if back_trace[i,j] == 1:
                Strings_new[0].append(t[i - 1])
                Strings_new[1].append('-')
                i -= 1
            elif back_trace[i,j] == 2:
                Strings_new[0].append(t[i - 1])
                Strings_new[1].append(s[j - 1])
                i -= 1
                j -= 1
            else:
                Strings_new[0].append('-')
                Strings_new[1].append(s[j - 1])
                j -= 1
        Strings_new = ["".join(s[::-1]) for s in Strings_new]
        return (min_score, Strings_new)


if __name__ == '__main__':

    # Parse the input data.
    sample_dataset = open('datasets/rosalind_edta.txt').read()
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

    # Get the edit distance and alignment of two strings.
    edit_dist,edit_align = Edit_Dist_Alignment(strings[1], strings[0])

    #edit_dist,edit_align = Edit_Dist_Alignment("PRTTEIN","PRETTY")

    print int(edit_dist)
    print edit_align[1]
    print edit_align[0]

