def hamm_dist(x,y):
    sum = 0;
    for i in range(len(x)):
        if (x[i] != y[i]):
            sum=sum+1
    return sum

def err_corr(not_found , input_list , rev_comp_dict):
    for x in not_found:
        print x
        for y in input_list:
            print y
            if hamm_dist(x, y) == 1:
                print(x + '->' + y)
                break
            elif hamm_dist(x,rev_comp_dict[y]) == 1:
                print(x + '->' + rev_comp_dict[y])
                break

if __name__ == '__main__':
    # Reading and parsing the input
    sample_dataset = open('datasets/rosalind_corr.txt').read()
    seq = ""
    strings = []
    for line in sample_dataset.strip().split():

        if line.startswith(">"):
            strings.append(''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
            strings.append(''.join(seq))


    rev_comp_dict = {}
    c = {}
    rev = ''

    # Finding the reverse compliment  GCAT-- reverse compliment : CGTA
    # list reverse = [::-1]
    for ele in strings:
        for c in ele[::-1]:
            rev += "GCAT"["CGTA".find(c)]
        rev_comp_dict[ele] = rev
        rev = ''

    not_found = []
    for item in rev_comp_dict:
        rev_comp = rev_comp_dict[item]

        if strings.count(rev_comp) <= 0:
            not_found.append(item)


    err_corr(not_found , strings , rev_comp_dict)





