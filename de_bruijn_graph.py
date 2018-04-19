#Reading and parsing the input
input_list = open('datasets/rosalind_dbru.txt').read().splitlines()

#input_list = ['TGAT' , 'CATG','TCAT','ATGC','CATC','CATC']
s = []
c = {}
rev = ''

# Finding the reverse compliment  GCAT-- reverse compliment : CGTA
# list reverse = [::-1]
for ele in input_list:
    s.append(ele)

    for c in ele[::-1]:
        rev += "GCAT"["CGTA".find(c)]
    s.append(rev)
    rev = ''
s = list(set(s))

# Finding the edges in de-bruijn graph
for i in range(len(s)):
    print("("+s[i][:len(s[i])- 1]+", "  +s[i][1:]+")")


