from itertools import permutations





def replace_currency(substring, list):
    for n in list:
        list.sort()
        if substring in str(n):
            list.remove(n)

def cycles_algorithm(Graph):
    nodes = list(Graph.nodes)
    perm = permutations(nodes, 2)
    permutationsList = list(perm)
    cycles = []

    for i in permutationsList:
        a,b = i
        if (a != b):
            cycles.append((a, b))

    print(cycles)
    print(len(cycles))
    return cycles


def algorithm(Graph, cycles):
    x = 0
    firstNode = None
    secondNode = None
    thirdNode = None
    lastNode = None
    nodes = list(Graph.nodes)
    valueList = []

    while x < len(nodes)-1:
        for cycle in cycles:
            a, b = cycle
            firstNode = nodes[x]
            secondNode = a
            thirdNode = b
            lastNode = nodes[x]

            if firstNode != a and lastNode != b:
                dict = Graph.get_edge_data(firstNode, secondNode, 0)
                dict2 = Graph.get_edge_data(secondNode, thirdNode, 0)
                dict3 = Graph.get_edge_data(thirdNode, lastNode, 0)

                if dict != 0 and dict2 != 0 and dict3 != 0:
                    value = float(1.0 * dict['weight'] * dict2['weight'] * dict3['weight'])
                    if value > 1.019:
                        valueList.append((value, firstNode, secondNode, thirdNode, lastNode))

        x += 1
    print(len(valueList))
    valueList.sort(reverse=True)
    print(valueList)
    return valueList