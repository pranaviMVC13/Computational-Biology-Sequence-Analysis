#A faster approach for finding the frequency of patterns in a text. Making BW matching more efficient

def Better_BWMATCHING(FirstColumn, LastColumn, Pattern):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            if LastColumn.find(symbol,top,bottom+1) != -1:
                top = FirstColumn.index(symbol) + CountSymbol(symbol, top, LastColumn)
                bottom = FirstColumn.index(symbol) + CountSymbol(symbol , bottom+1 , LastColumn) - 1
            else:
                return 0
        else:
            return ( bottom - top + 1 )


def CountSymbol(sym,pos,str):

    cnt = str.count(sym,0,pos);
    return cnt

if __name__ == "__main__":

    #sample_str = "GGCGCCGC$TAGTCACACACGCCGTA"
    #patterns = ['ACC', 'CCG', 'CAG']

    # Formatting data
    patterns = []
    sample_dataset = open('datasets/rosalind_ba9m.txt').read().strip().split()
    sample_str = sample_dataset[0]
    for i in range(1,len(sample_dataset)):
        patterns.append(sample_dataset[i])

    FirstColumn = ''.join(sorted(sample_str))

    freq_pattern = map(str, patterns)
    print ' '.join(map(str, [Better_BWMATCHING(FirstColumn,sample_str, p) for p in freq_pattern]))