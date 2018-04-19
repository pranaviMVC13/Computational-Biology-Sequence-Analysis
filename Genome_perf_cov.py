#Reading and parsing the input
input_dataset = open('datasets/rosalind_pcov.txt').read().splitlines()
#input_dataset = ['ATTAC' , 'TACAG' , 'GATTA','ACAGA','CAGAT','TTACA','AGATT']

edge_dic = {}
super_string =''

for ele in input_dataset:
    key = ele[:-1]
    edge_dic[key] = ele[1:]
k = edge_dic.iterkeys().next()

#cyclic super string
while edge_dic != {}:
    super_string += edge_dic[k][-1]
    key = k
    k = edge_dic[k]
    edge_dic.pop(key)

print super_string