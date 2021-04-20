import pickle

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import fcluster
from wordcloud import WordCloud

with open("texts.txt", "rb") as f:
    texts = pickle.load(f)
with open("subreddits.txt", "rb") as f:
    subreddits = pickle.load(f)
with open("cosDist.binaryfile", "rb") as f:
    cosDict = pickle.load(f)

numClust = 5
group = fcluster(cosDict, t=numClust, criterion='maxclust')
key, count = np.unique(group, return_counts=True)
for k, c in zip(key, count):
    print(k, c)

labels = list(group.tolist())
with open("result.txt", "w") as f:
    pass
#     to clear previous result

with open("result.txt", "a") as f:
    for i in range(1, numClust + 1):
        f.write("\n" + "Label {}, Count {}".format(i, count[i - 1]))
        f.write("\n" + texts[labels.index(i)] + "\n")
        print("label {} done".format(i))

for k in key:
    # get list of index of key
    index_num = [n for n, v in enumerate(labels) if v == k]
    # if len(index_num) > 5:
    #     # avoid redundant accumulation
    #     index_num = index_num[:5]
    text = ""
    for i in index_num:
        text += texts[i]
    wc = WordCloud(max_words=30).generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
