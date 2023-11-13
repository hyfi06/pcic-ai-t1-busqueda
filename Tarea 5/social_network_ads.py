import pandas as pd
import numpy as np
from numpy.typing import NDArray

from algorithms.kmeans import KMeans, graph_silhouette, graph_clusters


def split_data(df):
    train_size = int(len(df) * 0.7)

    # Generar una lista aleatoria de índices y dividirlos en entrenamiento y prueba
    indices = np.random.permutation(df.index)
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]

    # Crear los DataFrames de entrenamiento y prueba
    train_df = df.loc[train_indices]
    test_df = df.loc[test_indices]
    return train_df, test_df


def load_dataset(std: bool = False):
    """
    Carga los el CSV. Cuando std = True, regresa los datos estandarizados.
    """
    file_name = "Social_Network_Ads.csv"
    df = pd.read_csv(file_name)
    df['Gender'] = pd.factorize(df['Gender'])[0]
    return (df - df.mean()) / df.std() if std else df


def main():
    data = load_dataset()
    print(data)
    train, test = split_data(data)
    train = train.values[:, 1:]
    n_clusters = 2
    km = KMeans(n_clusters)
    silhouette: NDArray = km.fit(train)
    labels_train = km.predict(train)
    print(km.centroids)
    X = data.values[:, 1:]
    labels = km.predict(X)
    graph_silhouette(labels_train, silhouette, n_clusters)
    graph_clusters(X, labels)


if __name__ == '__main__':
    main()
