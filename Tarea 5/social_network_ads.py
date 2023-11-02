import pandas as pd
import numpy as np

from algorithms.kmeans import KMeans


def load_dataset():
    file_name = "Social_Network_Ads.csv"
    df = pd.read_csv(file_name)
    df['Gender'] = pd.factorize(df['Gender'])[0]
    return df


def main():
    data = load_dataset()
    km = KMeans(2)
    X = data.values[:, 1:-1]
    silhouette = km.fit(X)
    print(km.centroids)
    print(silhouette)
    print(km.predict(X))
    print(pd.DataFrame({
        'Pedict': km.predict(X),
        'Real': data['Purchased']
    }))


if __name__ == '__main__':
    main()
