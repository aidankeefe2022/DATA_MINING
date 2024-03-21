import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import copy
def matrix_vector(mat, vec):
    return np.matmul(mat, vec)

def create_graph(dataframe):
    dataframe.plot.scatter(x="X1", y="X2")
    plt.savefig('graph.png')

def create_linear_transformation(data, matrix):
        new_data = copy.deepcopy(data)
        for i in range(len(data[:,0])):
            new_vector = np.array([data[i][0], data[i][1]])
            to_add = matrix @ new_vector
            new_data[i][0] = to_add[0]
            new_data[i][1] = to_add[1]
        #create_plot_both(new_data, data, "transposed")
        return new_data

def create_plot_both(a,b,mean):

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(a[:,0],a[:,1], s=10, c='b', marker="s", label='origanal')
    ax1.scatter(b[:,0], b[:,1], s=10, c='r', marker="o", label=mean)
    plt.legend(loc='upper left')
    plt.show()

def mult_var_mean(list_of_data):
    mean_list = []
    for data in list_of_data:
        mean_list.append(np.mean(data, axis=0))

    return mean_list

def mean_ceneter_data(data):
    df = pd.DataFrame(data)
    df_centered = df.apply(lambda x: x-x.mean(), axis=0)
    return df_centered.to_numpy()

def create_covariance_matrix(data):
    print( np.cov(data))

def standard_scaler(data):
    Z_score = StandardScaler()
    return Z_score.fit_transform(data)



Q2_dataframe = pd.DataFrame(np.array([[1,1,3,-1,-1,1,2,2], [1.5,2,4,-1,1,-2,2,3]])).transpose()
Q2_dataframe.columns = ["X1", "X2"]
create_graph(Q2_dataframe)

np_array_of_Q2 = np.array([[1,1,3,-1,-1,1,2,2], [1.5,2,4,-1,1,-2,2,3]]).transpose()
val1 = np.sqrt(3)/2
np_matrix_of_Q2 = np.array([[val1, 1/2],[-1/2,val1]])
lt_data = create_linear_transformation(np_array_of_Q2, np_matrix_of_Q2)
mc_data = mean_ceneter_data(np_array_of_Q2)
create_plot_both(np_array_of_Q2, mc_data, "mean-centered")
create_covariance_matrix(np_array_of_Q2.transpose())
create_covariance_matrix(mc_data.transpose())
create_covariance_matrix(standard_scaler(np_array_of_Q2.transpose()))