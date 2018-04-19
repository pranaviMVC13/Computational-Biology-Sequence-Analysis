"parsing the input to group nodes and string"

def overlap_graph(input, n):

    vertices = []
    graph = []
    node = ''
    dna_str = ''
    "parse nodes and dna strings"
    strings = input.strip().split()
    for i in range(len(strings)):

        if strings[i].startswith('>R'):
            graph.append((node, dna_str))
            dna_str = ''
            node = strings[i]
            node = node[1:]
            continue
        dna_str = dna_str + strings[i]
    graph.append((node,dna_str))
    graph.pop(0)


    for v1, s1 in graph:
        for v2, s2 in graph:
            if v1 != v2 and s1.endswith(s2[:n]):
                vertices.append((v1, v2))

    return vertices


if __name__ == "__main__":

    sample_dataset = open('datasets/rosalind_grph.txt').read()

    vertices =  overlap_graph(sample_dataset, 3)
    for vertex in vertices:
        print vertex[0], vertex[1]


