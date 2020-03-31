from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering

datas = open('air_bnb.tsv').read().splitlines()
ATTR = datas[0].split()

c = np.array([(0, 0)])
for _ in datas[1:]:
	PRICE = _.split('\t')[ATTR.index('price')]
	REVIEW = _.split('\t')[ATTR.index('reviews_per_month')]

	if not PRICE or not REVIEW:
		continue

	c = np.vstack((c, (
			float(PRICE),
			float(REVIEW)
	)))

Agg = AgglomerativeClustering(n_clusters = 3)
Agg.fit(c)
Agg.labels_

print c

plt.scatter(c[:, 0], c[:, 1],c=Agg.labels_,cmap='rainbow')
plt.title('RBnB Clustering')
plt.xlabel('price')
plt.ylabel('reviews_per_month')
plt.show()
