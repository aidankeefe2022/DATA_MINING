import unittest
from part1_mini_p2 import *
import test_case_graphs
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_num_of_verts(self):
        self.assertEqual(num_of_verts(test_case_graphs.graph_0), 6)
        self.assertEqual(num_of_verts(test_case_graphs.graph_1), 5)
        self.assertEqual(num_of_verts(test_case_graphs.graph_2), 5)
        self.assertEqual(num_of_verts(test_case_graphs.graph_3), 9)
        self.assertEqual(num_of_verts(test_case_graphs.graph_4), 50)
        self.assertEqual(num_of_verts(test_case_graphs.graph_5), 7)
        self.assertEqual(num_of_verts(test_case_graphs.graph_6), 8)
        self.assertEqual(num_of_verts(test_case_graphs.graph_7), 200)
        self.assertEqual(num_of_verts(test_case_graphs.graph_8), 100)

    def test_degree_of_vertex(self):
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_1,2),2)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_2,2),3)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_3,2),3)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_3,3),4)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_3,6),3)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_4,25),2)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_5,4),6)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_6,3),2)
        self.assertEqual(degree_of_vertex(test_case_graphs.graph_7,27),10)

    def test_clustering_coefficient(self):
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_1,2),0.0)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_2,4), .333333333333333333)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_3,3),.333333333333333333)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_4,5),0.0)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_5,4),1.0)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_6,1),0.0)
        #self.assertEqual(Clustering_coefficient(test_case_graphs.graph_7,11),0.07142857142857142)
        self.assertEqual(Clustering_coefficient(test_case_graphs.graph_8,46),0.2857142857142857)

    def test_betweenness_centrality(self):
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,1), 0.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,2), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,3), 2.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,4), 2.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,5), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_0,6), 0.0)

        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_1,1), 1.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_1,2), 1.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_1,3), 1.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_1,4), 1.0)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_1,5), 1.0)

        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,0), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,1), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,2), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,3), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,4), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,5), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,6), 4.5)
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_6,7), 4.5)

        #if this fails it might be because graph 7 is messed up
        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_7,23), 873.7604441701953)

        self.assertEqual(Betweenness_centrality(test_case_graphs.graph_8,39),86.18112583907725)

    def test_adj_matrix(self):
        self.assertEqual(adjacency_matrix(test_case_graphs.graph_0), [[0, 1, 0, 0, 0, 0,],
                                                                             [1, 0, 1, 1, 0, 0,],
                                                                             [0, 1, 0, 0, 1, 0,],
                                                                             [0, 1, 0, 0, 1, 0,],
                                                                             [0, 0, 1, 1, 0, 1,],
                                                                             [0, 0, 0, 0, 1, 0,]])

        self.assertEqual(adjacency_matrix(test_case_graphs.graph_1),[[0, 1, 0, 0, 1,],
                                                                             [1, 0, 1, 0, 0,],
                                                                             [0, 1, 0, 1, 0,],
                                                                             [0, 0, 1, 0, 1,],
                                                                             [1, 0, 0, 1, 0,]])

        self.assertEqual(adjacency_matrix(test_case_graphs.graph_2), [[0, 1, 1, 0, 1,],
                                                                             [1, 0, 1, 1, 0,],
                                                                             [1, 1, 0, 1, 0,],
                                                                             [0, 1, 1, 0, 1,],
                                                                             [1, 0, 0, 1, 0,]])

        self.assertEqual(adjacency_matrix(test_case_graphs.graph_5), [[0, 1, 1, 1, 1, 1, 1,],
                                                                             [1, 0, 1, 1, 1, 1, 1,],
                                                                             [1, 1, 0, 1, 1, 1, 1,],
                                                                             [1, 1, 1, 0, 1, 1, 1,],
                                                                             [1, 1, 1, 1, 0, 1, 1,],
                                                                             [1, 1, 1, 1, 1, 0, 1,],
                                                                             [1, 1, 1, 1, 1, 1, 0,]])

        self.assertEqual(adjacency_matrix(test_case_graphs.graph_6), [[0, 1, 0, 0, 0, 0, 0, 1,],
                                                                             [1, 0, 1, 0, 0, 0, 0, 0,],
                                                                             [0, 1, 0, 1, 0, 0, 0, 0,],
                                                                             [0, 0, 1, 0, 1, 0, 0, 0,],
                                                                             [0, 0, 0, 1, 0, 1, 0, 0,],
                                                                             [0, 0, 0, 0, 1, 0, 1, 0,],
                                                                             [0, 0, 0, 0, 0, 1, 0, 1,],
                                                                             [1, 0, 0, 0, 0, 0, 1, 0,]])

    def test_average_shortest_path_length(self):
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_0), 1.8666666666666667)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_2), 1.3)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_3), 2.25)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_4), 17.0)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_5), 1.0)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_6), 2.2857142857142856)
        #self.assertEqual(average_shortest_path_length(test_case_graphs.graph_7), 2.6090452261306534)
        self.assertEqual(average_shortest_path_length(test_case_graphs.graph_8), 2.0785858585858588)
if __name__ == '__main__':
    unittest.main()

