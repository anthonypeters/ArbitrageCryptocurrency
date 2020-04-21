from itertools import permutations
from firebase import firebase

firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", "")


def replace_currency(substring, currency_list):
    for n in currency_list:
        if substring in str(n):
            currency_list.remove(n)


def cycles_algorithm(graph):
    nodes = list(graph.nodes)
    perm = permutations(nodes, 2)
    permutations_list = list(perm)
    cycles = []

    for i in permutations_list:
        a, b = i
        if a != b:
            cycles.append((a, b))

    print(cycles)
    print(len(cycles))
    return cycles


def n_hayward(graph, cycles):
    x = 0
    nodes = list(graph.nodes)
    valueList = []

    while x < len(nodes)-1:
        for cycle in cycles:
            a, b = cycle
            first_node = nodes[x]
            second_node = a
            third_node = b
            last_node = nodes[x]

            if first_node != a and last_node != b:
                weight_dict = graph.get_edge_data(first_node, second_node, 0)
                weight_dict2 = graph.get_edge_data(second_node, third_node, 0)
                weight_dict3 = graph.get_edge_data(third_node, last_node, 0)

                if weight_dict != 0 and weight_dict2 != 0 and weight_dict3 != 0:
                    value = float(1.0 * weight_dict['weight'] * weight_dict2['weight'] * weight_dict3['weight'])
                    if value > 1.019:
                        tuple = (value, first_node, second_node, third_node, last_node)
                        valueList.append(tuple)

        x += 1

    print(len(valueList))
    valueList.sort(reverse=True)
    print(valueList)
    firebase.post('/crypto-arbitrage-6575e/Opportunities', valueList)
    return valueList
