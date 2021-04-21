import pickle

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import fcluster
from wordcloud import WordCloud


class Clustering():
    def __init__(self):
        with open("texts.txt", "rb") as f:
            self.texts = pickle.load(f)
        with open("subreddits.txt", "rb") as f:
            self.subreddits = pickle.load(f)
        with open("cosDist.binaryfile", "rb") as f:
            self.cosDict = pickle.load(f)

    def clustering(self, numClust, wantToSave):
        self.group = fcluster(self.cosDict, t=numClust, criterion='maxclust')
        self.keys, self.counts = np.unique(self.group, return_counts=True)
        for k, c in zip(self.keys, self.counts):
            print(k, c)
        if wantToSave:
            self.saveExampleOfEachCluster(numClust)

    def saveExampleOfEachCluster(self, numClust):
        labels = list(self.group.tolist())
        with open("result.txt", "w") as f:
            pass
        #     to clear previous result

        with open("result.txt", "a") as f:
            for i in range(1, numClust + 1):
                f.write("\n" + "Label {}, Count {}".format(i, self.counts[i - 1]))
                f.write("\n" + self.texts[labels.index(i)] + "\n")
                print("label {} done".format(i))

    def diplayWordClouds(self):
        for k in self.keys:
            # get list of index of key
            index_num = [n for n, v in enumerate(labels) if v == k]
            # if len(index_num) > 5:
            #     # avoid redundant accumulation
            #     index_num = index_num[:5]
            text = ""
            for i in index_num:
                text += self.texts[i]
            wc = WordCloud(max_words=30).generate(text)
            plt.imshow(wc, interpolation='bilinear')
            plt.axis("off")
            plt.show()


C = Clustering()
C.clustering(5, True)
C.diplayWordClouds()
