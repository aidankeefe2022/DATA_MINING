import networkx as nx
from math import comb
import matplotlib.pyplot as plt
import numpy as np

# creates the graph from homework 3
G = nx.Graph()

G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(3, 12)
G.add_edge(12, 6)
G.add_edge(12, 7)
G.add_edge(12, 8)
G.add_edge(12, 9)
G.add_edge(12, 10)
G.add_edge(12, 11)
G.add_edge(6, 7)
G.add_edge(1, 2)
G.add_edge(4, 5)
G.add_edge(5, 11)

G_problem_10 = nx.DiGraph()
G_problem_10.add_edge(1, 2)
G_problem_10.add_edge(1, 3)
G_problem_10.add_edge(1, 4)
G_problem_10.add_edge(2, 1)
G_problem_10.add_edge(3, 2)
G_problem_10.add_edge(3, 5)
G_problem_10.add_edge(4, 3)
G_problem_10.add_edge(5, 3)


# this returns the betweenness centrailty of verts 3 and 12
def betweenness_centrality(input_G):
    # this is with normailization turned off
    vals = nx.betweenness_centrality(input_G, normalized=False)
    print(vals)
    return dict(vals)[3], dict(vals)[12]


# returns the eigenvector_centrailty for vets 3 and 12
def prestige(input_G):
    vals = nx.eigenvector_centrality(input_G, max_iter=100)
    return vals[3], vals[12]


# this returns the average shortest length from G
def avg_shortest_path_length(input_G):
    return nx.average_shortest_path_length(input_G)


# creates a histogram that shows the degree distrobution of all verts is the graph G
def degree_of_all(input_G):
    dict_degrees = dict(nx.degree(input_G))  # get the degrees of all nodes in a dict
    degree_vals_fb = dict_degrees.values()  # get a list of all degree values
    plt.hist(degree_vals_fb, bins=7)
    plt.xlabel('degree of node')
    plt.ylabel('number of nodes with degree')


# this returns the clustering coefficient of vert 3
def cluster_coff(G):
    print(nx.clustering(G))
    return (nx.clustering(G))


# this represents the graph as a dictionary with the key being a node and a value being the nodes that connect to it
def cluster_of_graph_no_nx(G):
    cluster_dict = {}
    edges = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4, 5, 12], 4: [3, 5], 5: [4, 3, 11], 6: [7, 12], 7: [6, 12], 8: [12],
             9: [12], 10: [12], 11: [12, 5], 12: [3, 6, 7, 8, 9, 10, 11]}
    for vert in edges.keys():
        num_of_edges = 0
        for x in range(0, len(edges[vert])):
            bool = True
            y = len(edges[vert]) - 1
            while (bool):
                if y != x:
                    to_check = edges[vert][y]
                    if edges[vert][x] in edges[to_check]:
                        num_of_edges += 1
                else:
                    bool = False
                y = y - 1
        # this is the math.comb function that does the same thing as n choose 2
        # this if statment is to avoid divide by zero errors
        if comb(len(edges[vert]), 2) != 0:
            cluster_dict[vert] = num_of_edges / comb(len(edges[vert]), 2)
        else:
            cluster_dict[vert] = 0

    return cluster_dict


def ER_graph(G):
    er = nx.erdos_renyi_graph(200, 0.1)
    bc_fb = nx.betweenness_centrality(er, normalized=True, endpoints=True)
    node_color = [20000 * er.degree(v) for v in er]  # this changes the color of the nodes based on their degree
    node_size = [v * v for v in bc_fb.values()]  # this changes the size based on their betweenness centrailty
    pos = nx.spring_layout(er)
    plt.figure(figsize=(20, 20))
    nx.draw_networkx(er, pos=pos, with_labels=False, node_color=node_color, node_size=node_size)

def average_clust_co(G):
    x = cluster_of_graph_no_nx(G)
    x = x.values()
    sum = 0
    for num in x:
        sum += num
    return sum / len(x)

#this returns the p after x about of iterations
def prestige_my_version(input_G, iter):
    dict_answer = {}
    adj_matrix = nx.adjacency_matrix(input_G).todense() #turns the nx directed graph in to an adj. matrix
    
    p = [[float(1) for _ in range(len(adj_matrix[0]))]]
    #this is the main power iteration loop
    for i in range(iter):
        sum = 0
        p = np.matmul(p, adj_matrix)
        for x in range(len(p[0])):
            sum += (p[0][x]) ** 2
        for j in range(len(p[0])):
            p[0][j] = float(float(p[0][j]) / float(np.sqrt(sum)))
        print(p)

    for i in range(len(p[0])):
        dict_answer[i+1] = p[0][i]
    return dict_answer

print(prestige_my_version(G_problem_10,3))

