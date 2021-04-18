import pickle
from pprint import pprint

import numpy as np
from scipy.cluster.hierarchy import fcluster

with open("texts.txt", "rb") as f:
    texts = pickle.load(f)
with open("subreddits.txt", "rb") as f:
    subreddits = pickle.load(f)
with open("cosDist.binaryfile", "rb") as f:
    cosDict = pickle.load(f)

numClust = 20
group = fcluster(cosDict, t=numClust, criterion='maxclust')
key, count = np.unique(group, return_counts=True)
for k,c in zip(key, count):
    print(k, c)

labels = list(group.tolist())
with open("result.txt", "a") as f:
    for i in range(1, numClust + 1):
        f.write("\n" + "Label {}, Count {}".format(i, count[i-1]))
        f.write("\n" + texts[labels.index(i)] + "\n")
        print("label {} done".format(i))

# try to do the same process with label 9