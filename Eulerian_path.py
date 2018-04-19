from random import choice


##to find the start node based on in degree and out degree
def finding_start_nodes(graph):
    start_nodes = graph.keys()
    for node in start_nodes:
        out_deg = len(graph[node])
        in_deg = sum([1 for x, y in graph.items() if node in y])
        if in_deg < out_deg:
            start_node = node
            return start_node


##finding eulerian path
def find_eulerian_path(graph):
    start_node = finding_start_nodes(graph)
    edges = [start_node]
    result = []
    while len(edges) != 0:
        top_edge = edges[-1]
        if top_edge not in graph:
            result.append(edges.pop())
            continue
        out_edges = graph[top_edge]
        if len(out_edges) > 0:
            edge = choice(out_edges)
            graph[top_edge].remove(edge)
            edges.append(edge)
        elif len(out_edges) == 0:
            result.append(edges.pop())
    return result[::-1]


if __name__ == "__main__":

    """data = ['0 -> 2',
'1 -> 3',
'2 -> 1',
'3 -> 0',
'3 -> 4',
'6 -> 3',
'6 -> 7',
'7 -> 8',
'8 -> 9',
'9 -> 6']"""

    sample_dataset = open('datasets/rosalind_ba3g.txt')
    data = [line.strip() for line in sample_dataset.readlines()]

    # Reading and parsing the input
    graph = {}
    for nodes in data:
        node = nodes.split(' -> ')
        start = int(node[0])
        end = [int(x) for x in node[1].split(',')]
        graph[start] = graph.get(start, []) + end

    path = find_eulerian_path(graph)

    string = ""
    for i in range(len(path)):
        if i == 0:
            string = str(path[i])
        else:
            string += '->' + str(path[i])
    print string

