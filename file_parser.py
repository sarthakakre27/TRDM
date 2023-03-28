import argparse
import networkx as nx

def parse_file(input_file):
    # open the file in read mode
    with open(input_file, 'r') as f:

        G = nx.DiGraph()

        # read the file line by line
        for line in f:
            # split the line by space
            line = line.split()
            # print the line
            print(line)
            print(line[0],'aaaaa')

            if line[0] not in G:
                G.add_node(line[0], valuation=ord(line[1]))
            else:
                G.nodes[line[0]]["valuation"]=ord(line[1])

            for i in range(2,len(line)):
                if line[i] not in G:
                    G.add_node(line[i])
                G.add_edge(len[0], len[i])

        print(G.graph,'aaaaaa')
            

            
































if __name__ == '__main__':
    # take input file name from user in argument
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file name")
    args = parser.parse_args()
    input_file = args.input_file

    # function call to parse the file
    parse_file(input_file)
    # parse_file('data.txt')