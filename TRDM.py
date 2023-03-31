# from file_parser import parse_file
import networkx as nx
import matplotlib.pyplot as plt

# function to find node with max bid, nodes are in the form of ('node_name': str, bid: int)
def find_max_bid(graph, source):
    # find the node with max bid, there can be multiple nodes with same bid
    max_bids = []
    max_bid = 0
    # for node in graph.nodes:
    #     if node[1] > max_bid:
    #         max_bid = node[1]
    #         node_name = node[0]
    # return (node_name, max_bid)
    for node in graph.nodes:
        if node[1] > max_bid:
            max_bid = node[1]
            max_bids = [node]
        elif node[1] == max_bid:
            max_bids.append((node[0], node[1]))
    
    # print(max_bids)
    # find which node is closer to the source
    min_distance = 100000
    min_node = None
    for node in max_bids:
        distance = nx.shortest_path_length(graph, source, node)
        if distance < min_distance:
            min_distance = distance
            min_node = node
    return min_node

# function to find the path from source to destination
def find_path(graph, source, destination):
    # find the path from source to destination
    paths = nx.all_shortest_paths(graph, source, destination)
    return [path for path in paths]

def create_subgraph(G, node):
    # print("-----------------")
    # print(node)
    # print("-----------------")
    edges = nx.dfs_successors(G, node)
    nodes = []
    for k,v in edges.items():
        nodes.extend([k])
        nodes.extend(v)
    
    # print(nodes)
    return G.subgraph(nodes)


def choose_shortest_path(shortest_paths):
    if len(shortest_paths) == 1:
        return shortest_paths[0]
    # find the first node that does not match in all paths
    num_shortest_paths = len(shortest_paths)
    first_non_match = [shortest_paths[0][0]]*num_shortest_paths

    for i in range(1, len(shortest_paths[0])):
        for j in range(1, num_shortest_paths):
            if shortest_paths[j][i] != shortest_paths[0][i]:
                first_non_match[j] = shortest_paths[j][i]
                first_non_match[0] = shortest_paths[0][i]
                break

    # print("first non matches")
    # print(first_non_match)
    # print("-----------------")
    # array of subgraphs
    subgraphs = []
    for i in range(len(first_non_match)):
        # print("subgraph " + str(i))
        # print("-----------------")
        sub_G = create_subgraph(G, first_non_match[i])
        # print("subgraph nodes")
        # print(sub_G.nodes)
        # print("-----------------")
        # remove the nodes in shortest path and their decendants from the subgraph
        nodes_to_remove = []
        for node in shortest_paths[i][shortest_paths[i].index(first_non_match[i])+1:]:
            # print(node)
            # print("shortest path - ")
            # print(shortest_paths[i])
            # nodes_to_remove.extend(nx.descendants(sub_G, node))
            try:
                decendants = nx.descendants(sub_G, node)
                nodes_to_remove.extend(decendants)
                nodes_to_remove.append(node)
            except:
                pass
            # print("printing nodes to remove" + str(nodes_to_remove))
        sub_G = nx.DiGraph(sub_G)
        # sub_G.remove_nodes_from(nodes_to_remove)
        for node in nodes_to_remove:
            try:
                sub_G.remove_node(node)
            except:
                pass
        # print(sub_G.nodes)
        subgraphs.append(sub_G)
        
    
    for i in range(len(subgraphs)):
        print("subgraph " + str(i))
        print(subgraphs[i].nodes)
        print("-----------------")



if __name__ == '__main__':
    # example graph
    G = nx.DiGraph()
    # G.add_node(('A', 1))
    # G.add_node(('B', 2))
    # G.add_node(('C', 3))
    # G.add_node(('D', 4))
    # G.add_node(('E', 5))
    # G.add_node(('F', 6))
    # G.add_node(('G', 79))
    # G.add_node(('H', 8))
    # # G.add_node(('I', 79))

    # G.add_edge(('A', 1), ('B', 2))
    # # G.add_edge(('A', 1), ('I', 79))
    # G.add_edge(('A', 1), ('C', 3))
    # G.add_edge(('B', 2), ('D', 4))
    # G.add_edge(('B', 2), ('E', 5))
    # G.add_edge(('B', 2), ('G', 79))
    # G.add_edge(('C', 3), ('F', 6))
    # G.add_edge(('C', 3), ('G', 79))
    # G.add_edge(('D', 4), ('H', 8))
    # G.add_edge(('E', 5), ('H', 8))
    # G.add_edge(('F', 6), ('H', 8))
    # G.add_edge(('G', 79), ('H', 8))

#     s 0 a b c
# a 4 d e
# b 2 g h
# c 5 o
# d 3 f
# e 4
# f 7
# g 3 i j
# h 5 j k
# i 3 j
# j 12 l m
# k 9
# l 18 n
# m 8
# n 15
# o 2 p q
# p 4
# q 6 p
    G.add_node(('s', 0))
    G.add_node(('a', 4))
    G.add_node(('b', 2))
    G.add_node(('c', 5))
    G.add_node(('d', 3))
    G.add_node(('e', 4))
    G.add_node(('f', 7))
    G.add_node(('g', 3))
    G.add_node(('h', 5))
    G.add_node(('i', 3))
    G.add_node(('j', 12))
    G.add_node(('k', 9))
    G.add_node(('l', 18))
    G.add_node(('m', 8))
    G.add_node(('n', 15))
    G.add_node(('o', 2))
    G.add_node(('p', 4))
    G.add_node(('q', 6))

    G.add_edge(('s', 0), ('a', 4))
    G.add_edge(('s', 0), ('b', 2))
    G.add_edge(('s', 0), ('c', 5))
    G.add_edge(('a', 4), ('d', 3))
    G.add_edge(('a', 4), ('e', 4))
    G.add_edge(('b', 2), ('g', 3))
    G.add_edge(('b', 2), ('h', 5))
    G.add_edge(('c', 5), ('o', 2))
    G.add_edge(('d', 3), ('f', 7))
    G.add_edge(('g', 3), ('i', 3))
    G.add_edge(('g', 3), ('j', 12))
    G.add_edge(('h', 5), ('j', 12))
    G.add_edge(('h', 5), ('k', 9))
    G.add_edge(('i', 3), ('j', 12))
    G.add_edge(('j', 12), ('l', 18))
    G.add_edge(('j', 12), ('m', 8))
    G.add_edge(('l', 18), ('n', 15))
    G.add_edge(('o', 2), ('p', 4))
    G.add_edge(('o', 2), ('q', 6))
    G.add_edge(('q', 6), ('p', 4))


    # find the node with max bid
    max_bid = find_max_bid(G, ('s', 0))
    # print(max_bid)
    nx.draw(G, with_labels=True)
    plt.savefig("filename.png")
    
    # find the path from source to destination
    path = find_path(G, ('s', 0), max_bid)
    # print(path)
    # path[1][1] = ('B', 2)
    choose_shortest_path(path)
    # for p in path:
    #     print(p)