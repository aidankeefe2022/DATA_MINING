from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# fetch dataset
dry_bean = fetch_ucirepo(id=602)

# data (as pandas dataframes)
X = dry_bean.data.features
y = dry_bean.data.targets
headers = dry_bean.data.headers

print(headers.values)

def Question_1():
    pca = PCA(n_components=2)
    pca_transform = pca.fit_transform(X)
    plt.scatter(pca_transform[:, 0], pca_transform[:, 1])
    plt.savefig('Q1_pca.png')

def Question_2():
    pca = PCA()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca_transform = pca.fit_transform(X_scaled)
    pca_transform = pd.DataFrame(pca_transform, columns=headers.values[0:16])
    var = pca_transform.var()
    var.plot.bar()
    plt.xlabel('Principal components')
    plt.ylabel('Variance')
    plt.show()

# Question_1()
Question_2()
