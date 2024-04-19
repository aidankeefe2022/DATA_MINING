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
    clusters_list = []
    mean_points = []
    mean_points_prev = []

    range_of_matrix = [(max(data_matrix[:,0]) ,min(data_matrix[:,0])), (max(data_matrix[:,1]) , min(data_matrix[:,1]))]
    for x in range(k):
        mean_points.append([random.uniform(range_of_matrix[0][0], range_of_matrix[0][1]),random.uniform(range_of_matrix[1][0],range_of_matrix[1][1])])

        clusters[x] = []
    mean_points = np.array(mean_points)
    mean_points_prev = np.array(mean_points)

    while True:
        #clear clusters
        for key in clusters.keys():
            clusters[key] = []
        clusters_list = []
        # cluster assignment
        for point1 in data_matrix:
            i = 0
            this_cluster = ""
            min_distance = 999999999
            for point2 in mean_points:

                if find_L2dist(point1, point2) < min_distance:
                    min_distance = find_L2dist(point1, point2)
                    this_cluster = i
                i += 1
            clusters[this_cluster].append(point1)
            clusters_list.append(this_cluster)

        # new mean_points
        for index in range(k):
            if len(clusters[index]) != 0:
                mean_points[index] = sum(clusters[index]) / len(clusters[index])
        #check if epsilon has been reached
        sum_distance = 0
        for index in range(k):
            sum_distance += find_L2dist(mean_points[index], mean_points_prev[index])
        if sum_distance < epsilon:
            return clusters_list, mean_points
        else:
            mean_points_prev = mean_points





def find_L2dist(point1, point2):
    return np.linalg.norm(point1 - point2)

#TODO: Tommy
def dbscan_clustering(data_matrix, minpts, epsilon):
    # Function body left blank
    pass

#TODO: anyone
def compute_clustering_precision(true_labels, cluster_labels):
    # Function body left blank
    pass