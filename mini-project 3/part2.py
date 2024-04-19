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
    mean_points_prev = []
    range_of_matrix = [sum(data_matrix[:,0]), sum(data_matrix[:,1])]
    for x in range(k):
        mean_points.append((random.uniform(range_of_matrix[0], range_of_matrix[1]),random.uniform(range_of_matrix[0],range_of_matrix[1])))
        mean_points_prev.append((random.uniform(range_of_matrix[0], range_of_matrix[1]),random.uniform(range_of_matrix[0],range_of_matrix[1])))
        clusters[x] = []
    while True:
        #clear clusters
        for key in clusters.keys():
            clusters[key] = []

        # cluster assignment
        for point1 in data_matrix:
            i = 0
            this_cluster = ""
            min_distance = int(np.inf)
            for point2 in mean_points:
                if find_L2dist(point1, point2) < min_distance:
                    min_distance = find_L2dist(point1, point2)
                    this_cluster = i

            clusters[this_cluster].append(point1)

        # new mean_points
        for index in range(k):
            mean_points[index] = sum(clusters[index]) / len(clusters[index])
        #check if epsilon has been reached
        sum_distance = 0
        for index in range(k):
            sum_distance += find_L2dist(mean_points[index], mean_points_prev[index])
        if sum_distance < epsilon:
            return clusters, mean_points
        else:
            mean_points_prev = mean_points





def find_L2dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

#TODO: Tommy
def dbscan_clustering(data_matrix, minpts, epsilon):
    # Function body left blank
    pass

#TODO: anyone
def compute_clustering_precision(true_labels, cluster_labels):
    # Function body left blank
    pass