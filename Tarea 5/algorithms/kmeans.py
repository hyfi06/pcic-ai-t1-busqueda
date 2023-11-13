import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, n_clusters: int, tol: float = 1e-6, max_iters: int = 1000) -> None:
        self.n_clusters = n_clusters
        self.tol = tol
        self.centroids = np.array([])
        self.max_iters = max_iters

    def fit(self, X: NDArray):
        """
        Se realiza el entrenamiento para encontrar los centros de los clusters. Se regresa el índice de Silhouette de cada elemento de entrenamiento.
        """
        # inicializamos los centros de manera aleatoria
        self.centroids = X[
            np.random.choice(X.shape[0], self.n_clusters, replace=False), :
        ]

        # iteramos el proceso hasta el máximo de iteraciones
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
                print(f"Iteraciones:{j}")
                break
            self.centroids = next_centroids
        return self._silhouette(X)

    def predict(self, X: NDArray):
        """
        Regresa un arreglo de etiquetas
        """
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
            cluster_distance = np.zeros((X.shape[0], clusters[i].shape[0]))

            for j, x in enumerate(clusters[i]):
                cluster_distance[:, j] = np.linalg.norm(X - x, axis=1)
                cluster_distance[cluster_distance[:, j] == 0, j] = np.nan
            cluster_distance = np.nanmean(cluster_distance, axis=1)
            a[labels == i] = cluster_distance[
                labels == i].reshape((sum(labels == i), 1))
            b[labels != i, i] = cluster_distance[labels != i]
            b[labels == i, i] = np.nan
        b = np.nanmin(b, axis=1).reshape((X.shape[0], 1))
        max_a_b = np.column_stack((a, b)).max(axis=1).reshape((X.shape[0], 1))
        return ((b - a) / max_a_b).reshape((X.shape[0],))


def graph_silhouette(labels, silhouette_vals, n_clusters):
    plt.figure(figsize=(7, 5))

    # Rellenar el gráfico
    y_lower, y_upper = 0, 0
    yticks = []
    for i in range(n_clusters):
        cluster = silhouette_vals[labels == i]
        cluster.sort()
        y_upper += len(cluster)
        color = plt.cm.Spectral(float(i) / n_clusters)
        plt.barh(
            range(y_lower, y_upper),
            cluster,
            edgecolor='none',
            height=1,
            color=color
        )
        yticks.append((y_lower + y_upper) / 2)
        y_lower += len(cluster)

    # Etiquetas y títulos
    plt.xlabel('Índice de Silhouette')
    plt.ylabel('Cluster')
    plt.yticks(yticks, np.unique(labels))
    silhouette_mean = np.mean(silhouette_vals)
    plt.axvline(silhouette_mean, color="red",
                linestyle="--")  # Línea de la media
    plt.title(f'Valores de Silhouette por Cluster (mean: {silhouette_mean})')
    plt.tight_layout()

    # Mostrar gráfico
    plt.show()


def graph_clusters(X, labels):
    dimensions = X.shape[1]
    n_clusters= len(np.unique(labels))
    fig, axs = plt.subplots(
        dimensions,
        dimensions,
        figsize=(11, 8)
    )
    for i in range(dimensions):
        for j in range(dimensions):
            for k in np.unique(labels):
                color = plt.cm.Spectral(float(k) / n_clusters)
                axs[i,j].scatter(
                    X[labels == k,i],
                    X[labels == k,j],
                    label=f'Etiqueta {k}',
                    color=color
                )
    # Ajustar el layout para prevenir la superposición de títulos
    plt.tight_layout()

    # Mostrar la figura
    plt.show()
