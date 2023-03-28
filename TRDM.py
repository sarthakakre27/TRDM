from file_parser import parse_file
import networkx as nx
import matplotlib.pyplot as plt

# function to find node with max bid, nodes are in the form of ('node_name': str, bid: int)
def find_max_bid(graph):
    # find the node with max bid
    max_bid = 0
    for node in graph.nodes:
        if node[1] > max_bid:
            max_bid = node[1]
            node_name = node[0]
    return (node_name, max_bid)


# function to find the path from source to destination
def find_path(graph, source, destination):
    # find the path from source to destination
    path = nx.all_shortest_paths(graph, source, destination)
    return path






if __name__ == '__main__':
    # example graph
    G = nx.DiGraph()
    G.add_node(('A', 1))
    G.add_node(('B', 2))
    G.add_node(('C', 3))
    G.add_node(('D', 4))
    G.add_node(('E', 5))
    G.add_node(('F', 6))
    G.add_node(('G', 79))
    G.add_node(('H', 8))

    G.add_edge(('A', 1), ('B', 2))
    G.add_edge(('A', 1), ('C', 3))
    G.add_edge(('B', 2), ('D', 4))
    G.add_edge(('B', 2), ('E', 5))
    G.add_edge(('B', 2), ('G', 79))
    G.add_edge(('C', 3), ('F', 6))
    G.add_edge(('C', 3), ('G', 79))
    G.add_edge(('D', 4), ('H', 8))
    G.add_edge(('E', 5), ('H', 8))
    G.add_edge(('F', 6), ('H', 8))
    G.add_edge(('G', 79), ('H', 8))


    # find the node with max bid
    max_bid = find_max_bid(G)
    print(max_bid)
    nx.draw(G, with_labels=True)
    plt.savefig("filename.png")
    
    # find the path from source to destination
    path = find_path(G, ('A', 1), ('G', 79))
    # print(path)
    for p in path:
        print(p)