import numpy as np
from numpy.typing import NDArray


class KMeans:
    def __init__(self, n_clusters: int, tol: float = 1e-6, max_iters: int = 1000) -> None:
        self.n_clusters = n_clusters
        self.tol = tol
        self.centroids = np.array([])
        self.max_iters = max_iters

    def fit(self, X: NDArray):
        self.centroids = X[
            np.random.choice(X.shape[0], self.n_clusters, replace=False), :
        ]

        for j in range(self.max_iters):
            distances = self._compute_distances(X)
            labels = np.argmin(distances, axis=1)
            clusters = [
                X[labels == i]
                for i in range(self.n_clusters)
            ]
            next_centroids = np.array([
                cluster.mean(axis=(0))
                for cluster in clusters
            ])
            if np.all(np.abs(next_centroids - self.centroids) == 0):
                print(j)
                break
            self.centroids = next_centroids
        return self._silhouette(X)

    def predict(self, X: NDArray):
        distances = self._compute_distances(X)
        return np.argmin(distances, axis=1)

    def _compute_distances(self, X: NDArray):
        distances = np.zeros((X.shape[0], self.n_clusters))
        for i, centroid in enumerate(self.centroids):
            distances[:, i] = np.linalg.norm(X - centroid, axis=1)
        return distances

    def _silhouette(self, X: NDArray):
        distances = self._compute_distances(X)
        labels = np.argmin(distances, axis=1)
        clusters = [
            X[labels == i]
            for i in range(self.n_clusters)
        ]
        a = np.zeros((X.shape[0], 1))
        b = np.zeros((X.shape[0], self.n_clusters))
        for i in range(self.n_clusters):
            cluster_distance = np.column_stack(tuple([
                np.linalg.norm(X - x) for x in X
            ]))
            cluster_distance[cluster_distance == 0] = np.nan
            cluster_distance = np.nanmean(cluster_distance, axis=1)
            a[labels == i] = cluster_distance[labels == 1]
            b[labels != i, i] = cluster_distance[labels == 0]
            b[labels == i, i] = np.nan
        b = np.nanmin(b, axis=1)
        return (b - a) / np.column_stack((a, b)).max(axis=1)
