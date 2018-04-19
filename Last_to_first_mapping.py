#Finding the mapping of a character in the suffix rotaion to the original string
#The sorted string of the last col is the first column
#Calculate the occurence number of the symbol in last column
#Find the index of the symbol in the first column and add the offset of occurence

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
    print idx_first

if __name__ == "__main__":

    sample_str = "abba$aa"
    idx_rot = 5

    #sample_dataset = open('datasets/rosalind_ba9k.txt').read().strip().split()
    #sample_str = sample_dataset[0]
    #idx_rot = int(sample_dataset[1])
    last_to_first_map(sample_str,idx_rot)