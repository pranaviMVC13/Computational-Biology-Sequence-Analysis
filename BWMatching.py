# To find total number of matches of Pattern in Text
#Using the last column, first column and last to first mapping

def BWMATCHING(LastColumn, Pattern):
    top = 0
    bottom = len(LastColumn)-1
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            if LastColumn.find(symbol,top,bottom+1) != -1:
                topIndex = LastColumn.index(symbol, top, bottom+1)
                bottomIndex = LastColumn.rfind(symbol,top,bottom+1)
                top = last_to_first_map(LastColumn, topIndex)
                bottom = last_to_first_map(LastColumn, bottomIndex)
            else:
                return 0
        else:
            return ( bottom - top + 1 )


def last_to_first_map(str,idx_rot):
    last = str
    first = ''.join(sorted(last))

    sym_at_id = str[idx_rot]
    count = 0
    for i in range(idx_rot):
        if sym_at_id == str[i]:
            count += 1

    x = first.index(sym_at_id)
    idx_first = x + count
    return idx_first

if __name__ == "__main__":

    #sample_str = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    #patterns = ['CCT', 'CAC', 'GAG', 'CAG','ATC']

    sample_dataset = open('datasets/rosalind_ba9l.txt').read().strip().split()
    sample_str = sample_dataset[0]
    patterns= []
    freq = []

    #Formatting data
    for i in range(1,len(sample_dataset)):
        patterns.append(sample_dataset[i])

    """for i in range(len(patterns)):
        freq.append(BWMATCHING(sample_str,patterns[i]))

    print freq"""

    freq_pattern = map(str, patterns)
    print ' '.join(map(str, [BWMATCHING(sample_str, p) for p in freq_pattern]))