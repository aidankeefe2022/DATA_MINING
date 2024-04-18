#Please do not change function names and number of parameters.
#Please check the assignment requirements what function should return.
import numpy as np
import matplotlib.pyplot as plt
import random

#TODO: first to get it done
def k_means_clustering(data_matrix, k, epsilon):
    # Function body left blank
    iteration = 0
    clusters = {}
    mean_points = []
    range_of_matrix = [sum(data_matrix[:,0]), sum(data_matrix[:,1])]
    for x in range(k):
        mean_points.append(random.uniform(range_of_matrix[0], range_of_matrix[1]))




    pass

#TODO: Tommy
def dbscan_clustering(data_matrix, minpts, epsilon):
    # Function body left blank
    pass

#TODO: anyone
def compute_clustering_precision(true_labels, cluster_labels):
    # Function body left blank
    pass