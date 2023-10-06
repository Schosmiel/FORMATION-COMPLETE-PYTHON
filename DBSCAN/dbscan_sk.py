from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Générer des données en forme de lune
data, _ = make_moons(n_samples=500, noise=0.05)

# Créer un objet DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)

# Effectuer la mise en cluster
cluster = dbscan.fit_predict(data)

# Tracer les points en fonction des clusters
plt.scatter(data[:, 0], data[:, 1], c=cluster, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()
