import networkx as nx
import matplotlib.pyplot as plt
import math

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

#TODO tommy
def degree_of_vertex(edge_list):
    degree = 0

    return degree

#TODO aidan
def Clustering_coefficient(edge_list, vertex):
    val = 0
    neighbor_dict = {}
    for vertex in range(num_of_verts(edge_list)):
        for edge in edge_list:
            if neighbor_dict[vertex] == None:
                neighbor_dict[vertex] = []
            if edge[0] == vertex:
                neighbor_dict[vertex].append(edge[1])
            elif edge[1] == vertex:
                neighbor_dict[vertex].append(edge[0])

    num_of_edges = 0
    for x in range(0, len(neighbor_dict[vertex])):

        y = len(neighbor_dict[vertex]) - 1
        while (True):
            if y != x:
                to_check = neighbor_dict[vertex][y]
                if neighbor_dict[vertex][x] in neighbor_dict[to_check]:
                    num_of_edges += 1
            else:
                break
            y = y - 1
    # this is the math.comb function that does the same thing as n choose 2
    # this if statment is to avoid divide by zero errors
    if math.comb(len(neighbor_dict[vertex]), 2) != 0:
        val = num_of_edges / math.comb(len(neighbor_dict[vertex]), 2)
    else:
        val = 0

    return val

#TODO tommy
def Betweenness_centrality(edge_list):
    centrality = 0

    return centrality

#TODO aidan
def average_shortest_path_length(edge_list):
    average_length = 0
    all_vert_comb = 0
    for x in range(num_of_verts(edge_list)):
        #find the comb on all vertex with not mirros and then look for the shortest path bewteen all of them this will be eaiser than dikstra bs to remove dups that scew the average
        x =1

    return average_length

def shortest_path_length(vert1, vert2, edgelist):


#TODO tommy
def adjacency_matrix(edge_list):
    matrix = [[0 for _ in range(num_of_verts(edge_list))] for _ in range(num_of_verts(edge_list))] #this makes a sqare matrix with lengh and hight equal to the number of nodes (2D array)

    return matrix

#TODO aidan
def power_iteration(edge_list):
    return False

#part3

#TODO tommy
def create_visualization(G):
    return False

#TODO aidan
def top_ten_degree_nodes(G):
    return sorted(G.degree, key=degree_of_vertex)

#TODO tommy
def top_ten_highest_betweenness_centrality(G):
    return False

#TODO aidan
def top_ten_highest_cluster_coefficient(G):
    return False

#TODO tommy
def top_ten_highest_eigenvector_centrality(G):
    return False

#TODO aidan
def top_ten_highest_pagerank(G):
    return False
