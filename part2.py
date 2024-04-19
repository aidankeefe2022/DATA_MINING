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
def dbscan_clustering(D, minpts, epsilon):
    clusters = [-1]*len(D)
    corepts = []
    borderpts = []
    noisepts = []
    
    C = 0
    # Find cluster points
    for P in range(len(D)):
        # Skip points that have already been visited
        if(clusters[P] != -1):
            continue

        # Get neighbors of P
        pNeighbors = get_neighbors(D, P, epsilon)

        if(len(pNeighbors) < minpts):
            clusters[P] = 0
        else:
            C += 1
            # Assign the cluster ID to point
            clusters[P] = C

            i = 0
            # Look at each neighbor of P
            while i < len(pNeighbors):
                Pn = pNeighbors[i]
                
                if clusters[Pn] == 0:
                    clusters[Pn] = C
                elif clusters[Pn] == -1:
                    clusters[Pn] = C
                    PnNeighbors = get_neighbors(D, Pn, epsilon)
                    
                    if len(PnNeighbors) >= minpts:
                        pNeighbors = pNeighbors + PnNeighbors

                i += 1

    # Loop through clusters to find core, border, and noise points
    for i in range(len(clusters)):
        p = clusters[i]
        if (p == 0):
            noisepts.append(i)
        elif (len(get_neighbors(D, i, epsilon)) >= minpts):
            corepts.append(i)
        else:
            borderpts.append(i)

    return clusters, corepts, borderpts, noisepts

# Returns a list of a point's neighbors
def get_neighbors(D, P, epsilon):
    neighbors = []

    # Find all points within distance epsilon of point P
    for Pn in range(len(D)):
        if np.linalg.norm(D[P] - D[Pn]) <= epsilon:
            neighbors.append(Pn)

    return neighbors

#TODO: anyone
def compute_clustering_precision(true_labels, cluster_labels):
    # Function body left blank
    pass


# Test Case 1:
from sklearn.datasets import make_blobs
X,y = make_blobs(n_samples=300, centers=3, random_state=35)
clusters, corepts, borderpts, noisepts = dbscan_clustering(X, 10, 0.5)

testclusters = [0, 1, 0, 0, 0, 3, 1, 0, 0, 2, 1, 1, 3, 0, 1, 1, 0, 2, 2, 0, 2, 2, 2, 1, 3, 0, 3, 0, 0, 0, 3, 0, 0, 1, 1, 3, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 3, 3, 0, 0, 0, 2, 1, 2, 0, 0, 0, 2, 1, 2, 1, 0, 3, 0, 0, 1, 1, 0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 3, 0, 0, 0, 0, 1, 1, 1, 0, 3, 0, 1, 0, 2, 3, 3, 1, 1, 1, 0, 0, 0, 3, 1, 1, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0, 0, 2, 1, 2, 3, 0, 1, 2, 0, 0, 3, 0, 2, 0, 2, 2, 1, 0, 0, 0, 3, 2, 0, 3, 1, 0, 0, 1, 0, 2, 2, 3, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 3, 1, 0, 0, 2, 0, 3, 3, 2, 0, 1, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 1, 2, 1, 1, 0, 0, 2, 0, 0, 3, 3, 3, 3, 1, 0, 1, 0, 0, 0, 0, 0, 1, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 3, 0, 2, 3, 0, 1, 3, 0, 1, 0, 3, 2, 0, 2, 0, 0, 1, 0, 0, 0, 3, 1, 2, 3, 0, 3, 1, 3, 3, 0, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 1, 0, 2, 0, 0, 2]
testcorepts = [1, 6, 9, 10, 11, 12, 15, 17, 20, 21, 30, 35, 36, 38, 39, 51, 61, 69, 74, 75, 77, 79, 87, 88, 94, 95, 98, 103, 104, 112, 115, 116, 117, 119, 126, 141, 143, 147, 151, 155, 158, 161, 169, 170, 174, 175, 177, 180, 181, 184, 188, 191, 201, 205, 208, 211, 212, 214, 223, 224, 236, 237, 239, 242, 243, 245, 247, 248, 257, 258, 260, 262, 263, 270, 279, 287, 291, 296, 299]
testborderpts = [5, 14, 18, 22, 23, 24, 26, 33, 34, 46, 48, 49, 50, 55, 56, 57, 62, 63, 64, 66, 70, 76, 81, 86, 90, 92, 96, 97, 99, 105, 110, 114, 122, 123, 125, 129, 132, 133, 134, 135, 137, 138, 145, 146, 152, 154, 160, 162, 164, 186, 187, 190, 194, 202, 203, 204, 213, 215, 217, 226, 234, 240, 250, 253, 259, 264, 265, 267, 275, 277, 280, 282, 292, 294]
testnoisepts = [0, 2, 3, 4, 7, 8, 13, 16, 19, 25, 27, 28, 29, 31, 32, 37, 40, 41, 42, 43, 44, 45, 47, 52, 53, 54, 58, 59, 60, 65, 67, 68, 71, 72, 73, 78, 80, 82, 83, 84, 85, 89, 91, 93, 100, 101, 102, 106, 107, 108, 109, 111, 113, 118, 120, 121, 124, 127, 128, 130, 131, 136, 139, 140, 142, 144, 148, 149, 150, 153, 156, 157, 159, 163, 165, 166, 167, 168, 171, 172, 173, 176, 178, 179, 182, 183, 185, 189, 192, 193, 195, 196, 197, 198, 199, 200, 206, 207, 209, 210, 216, 218, 219, 220, 221, 222, 225, 227, 228, 229, 230, 231, 232, 233, 235, 238, 241, 244, 246, 249, 251, 252, 254, 255, 256, 261, 266, 268, 269, 271, 272, 273, 274, 276, 278, 281, 283, 284, 285, 286, 288, 289, 290, 293, 295, 297, 298]

print("\nTest Case 1:")
print("Clusters equal:", clusters == testclusters)
print("Core Points equal:", corepts == testcorepts)
print("Border Points equal:", borderpts == testborderpts)
print("Noise Points equal:", noisepts == testnoisepts)

# Test Case 2:
from sklearn.datasets import make_moons
X,y = make_moons(n_samples=200, noise=.06, random_state=4)
clusters, corepts, borderpts, noisepts = dbscan_clustering(X, 20, 0.4)

testclusters = [1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2]
testcorepts = [0, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 106, 107, 110, 111, 112, 113, 114, 116, 117, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 133, 134, 136, 137, 138, 140, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 158, 159, 161, 162, 163, 164, 165, 167, 168, 169, 170, 171, 172, 173, 174, 175, 177, 178, 179, 180, 181, 182, 183, 185, 187, 189, 191, 192, 193, 194, 196, 197, 198, 199]
testborderpts = [1, 4, 11, 21, 27, 36, 54, 62, 70, 75, 79, 97, 105, 108, 109, 115, 119, 132, 135, 139, 141, 155, 156, 157, 160, 166, 176, 184, 186, 188, 190, 195]
testnoisepts = []

print("\nTest Case 2:")
print("Clusters equal:", clusters == testclusters)
print("Core Points equal:", corepts == testcorepts)
print("Border Points equal:", borderpts == testborderpts)
print("Noise Points equal:", noisepts == testnoisepts)

# Test Case 3:
from sklearn.datasets import load_iris
X = load_iris()['data']
clusters, corepts, borderpts, noisepts = dbscan_clustering(X, 10, 0.5)

testclusters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
testcorepts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 19, 20, 21, 23, 25, 26, 27, 28, 29, 30, 31, 34, 35, 36, 37, 38, 39, 40, 42, 43, 45, 46, 47, 48, 49, 51, 54, 55, 61, 63, 67, 69, 71, 74, 78, 82, 83, 86, 88, 89, 91, 92, 94, 95, 96, 97, 99, 104, 111, 112, 116, 123, 126, 127, 138, 140, 147]
testborderpts = [13, 14, 18, 22, 24, 32, 33, 44, 50, 52, 53, 56, 58, 59, 62, 64, 65, 66, 70, 72, 73, 75, 76, 77, 79, 80, 81, 84, 85, 90, 101, 103, 110, 115, 120, 124, 128, 132, 133, 137, 139, 141, 142, 143, 144, 145, 146, 149]
testnoisepts = [15, 41, 57, 60, 68, 87, 93, 98, 100, 102, 105, 106, 107, 108, 109, 113, 114, 117, 118, 119, 121, 122, 125, 129, 130, 131, 134, 135, 136, 148]

print("\nTest Case 3:")
print("Clusters equal:", clusters == testclusters)
print("Core Points equal:", corepts == testcorepts)
print("Border Points equal:", borderpts == testborderpts)
print("Noise Points equal:", noisepts == testnoisepts)