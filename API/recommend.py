import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import joblib

new_df1 = pd.read_csv('new_Arts.csv')
ratings_matrix = new_df1.pivot_table(values='rating', index='UserID', columns='ProductID', fill_value=0)
ratings_matrix.head()
X = ratings_matrix.T
X1 = X

SVD = TruncatedSVD(n_components=10)
decomposed_matrix = SVD.fit_transform(X)

correlation_matrix = np.corrcoef(decomposed_matrix)

def result(i):
    A={}
    Product_names = list(X.index)
    product_ID = Product_names.index(i)
    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.65])
    Recommend.remove(i) 
    
    for i, j in zip(range(1,11), Recommend[0:10]):
        A[i] = new_df1['Title'].loc[new_df1['ProductID'] == j].iloc[0]
    return A
