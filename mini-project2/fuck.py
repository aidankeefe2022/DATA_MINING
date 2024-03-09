import queue
from itertools import combinations
import test_case_graphs
import networkx as nx
import matplotlib.pyplot as plt
import math

f = open("fb-pages-tvshow.edges", "rb")

G = nx.read_edgelist(f, delimiter=",")
f.close()


#Part 2

def num_of_verts(edge_list):
    vert_set  = set()
    for x in edge_list:
        vert_set.add(x[0])
        vert_set.add(x[1])

    return len(vert_set)


def degree_of_vertex(edge_list, vertex):
    return len(cnd(edge_list)[vertex])

#creates a dict that is in the form of vertex : [list of its neighbor nodes]
def cnd(edge_list):
    if any(0 in t for t in edge_list):
        var1 = 0
        var2 = 0
    else:
        var1 = 1
        var2 = 1
    neighbor_dict = {}
    for vertex in range(var1, num_of_verts(edge_list) + var2):
        for edge in edge_list:
            if vertex not in neighbor_dict.keys():
                neighbor_dict[vertex] = []
            if edge[0] == vertex:
                neighbor_dict[vertex].append(edge[1])
            elif edge[1] == vertex:
                neighbor_dict[vertex].append(edge[0])
    return neighbor_dict


def Clustering_coefficient(edge_list, vert):
    val = 0
    neighbor_dict = cnd(edge_list)

    num_of_edges = 0
    for x in range(0, len(neighbor_dict[vert])):
        y = len(neighbor_dict[vert]) - 1
        while (True):
            if y != x:
                to_check = neighbor_dict[vert][y]
                if neighbor_dict[vert][x] in neighbor_dict[to_check]:
                    num_of_edges += 1
            else:
                break
            y = y - 1
    # this is the math.comb function that does the same thing as n choose 2
    # this if statment is to avoid divide by zero errors
    if math.comb(len(neighbor_dict[vert]), 2) != 0:
        val = num_of_edges / math.comb(len(neighbor_dict[vert]), 2)
    else:
        val = 1

    return val

#TODO tommy
def Betweenness_centrality(edge_list, vertex):
    centrality = 0

    return centrality

def average_shortest_path_length(edge_list):
    list_of_lens = []
    if any(0 in t for t in edge_list):
        list_of_verts = [x for x in range(0, num_of_verts(edge_list))]
    else:
        list_of_verts = [x for x in range(1,num_of_verts(edge_list)+1)]
    all_vert_comb = list(combinations(list_of_verts, 2))
    for vert in all_vert_comb:
        list_of_lens.append(shortest_path_length(vert[0],vert[1],edge_list))
    return sum(list_of_lens)/len(list_of_lens)


def shortest_path_length(vert1, vert2, edgelist):
    n_dict = cnd(edgelist)
    dist_dict = {}
    already_visited = set()
    my_queue = queue.Queue()
    my_queue.put(vert1)
    dist_dict[vert1] = 0
    while my_queue.not_empty:
        current_vertex = my_queue.get()
        if current_vertex == vert2:
            return dist_dict[current_vertex]
        for neighbor in n_dict[current_vertex]:
            if neighbor not in already_visited:
                my_queue.put(neighbor)
                already_visited.add(neighbor)
                dist_dict[neighbor] = dist_dict[current_vertex] + 1

    return dist_dict[vert2]

#TODO tommy
def adjacency_matrix(edge_list):
    matrix = [[0 for _ in range(num_of_verts(edge_list))] for _ in range(num_of_verts(edge_list))] #this makes a sqare matrix with lengh and hight equal to the number of nodes (2D array) filled with all zeros

    for edge in edge_list:
        matrix[edge[0]][edge[1]] = 1

    return matrix

#TODO aidan
def power_iteration(edge_list):
    #do when adjmatrix is done

    return False



#part3

#TODO tommy
def create_visualization(G):
    return nx.draw_networkx(G)


def top_ten_degree_nodes(G):
    return sorted(G.degree(), key=lambda x: x[1], reverse=True)[:10]


#TODO tommy
def top_ten_highest_betweenness_centrality(G):
    dict1 = nx.betweenness_centrality(G)
    for v in dict1.keys():
        list1.append((dict1[v], v))

    return sorted(list1,reverse=True)[:10]

#TODO aidan
def top_ten_highest_cluster_coefficient(G):
    x = nx.clustering(G)
    list = []
    for vert in x:
        if x[vert] == 1 :
            list.append(vert)
    return get_degree_order_node(list_of_vertices=list,G=G)[:10]

#used to order the nodes with cluster coeffiecnt of 1.0 in a way so they can be logically deciminated
def get_degree_order_node(list_of_vertices, G):
    list = []
    for v in list_of_vertices:
        list.append((G.degree(nbunch=v), v))
    return sorted(list, reverse=True)
#TODO tommy
def top_ten_highest_eigenvector_centrality(G):
    dict1 = nx.eigenvector_centrality(G)
    for v in dict1.keys():
        list1.append((dict1[v], v))

    return sorted(list1,reverse=True)[:10]

#TODO aidan
def top_ten_highest_pagerank(G):
    list = []
    dict = nx.pagerank(G)
    for v in dict:
        list.append((v,dict[v]))
    return sorted(list, key=lambda x: x[1], reverse=True)[:10]


print(nx.average_shortest_path_length(test_case_graphs.g7))
