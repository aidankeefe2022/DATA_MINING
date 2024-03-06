import networkx as nx
import matplotlib.pyplot as plt

f = open("fb-pages-tvshow.edges", "rb")

G = nx.read_edgelist(f, delimiter=",")
f.close()
print(G)
print([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)])

#Part 2

def num_of_verts(edge_list):
    vert_set  = set()
    for x in edge_list:
        vert_set.add(x[0])
        vert_set.add(x[1])

    return len(vert_set)

def degree_of_vertex(edge_list):
    degree = 0

    return degree

def Clustering_coefficient(edge_list):
    clust = 0

    return clust

def Betweenness_centrality(edge_list):
    centrality = 0

    return centrality


def average_shortest_path_length(edge_list):
    average_length = 0

    return average_length

def adjacency_matrix(edge_list):
    matrix = [[0 for _ in range(num_of_verts(edge_list))] for _ in range(num_of_verts(edge_list))] #this makes a sqare matrix with lengh and hight equal to the number of nodes (2D array)

    return matrix

def power_iteration(edge_list):
    return False

#part3

def create_visualization(G):
    return False

def top_ten_degree_nodes(G):
    return sorted(G.degree, key=degree_of_vertex)

def top_ten_highest_betweenness_centrality(G):
    return False

def top_ten_highest_cluster_coefficient(G):
    return False

def top_ten_highest_eigenvector_centrality(G):
    return False

def top_ten_highest_pagerank(G):
    return False

def