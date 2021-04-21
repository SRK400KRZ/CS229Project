import json
import pickle

from scipy.cluster.hierarchy import linkage
from sklearn.feature_extraction.text import TfidfVectorizer


class Vectorizing:
    def __init__(self):
        with open('data.json') as f:
            self.data = json.load(f)
        # dict_keys(['selftext', 'subreddit', 'title'])
        # from data.json, craete two lists: textBodies[] and subreddit[]
        self.createLists()

    def createLists(self):
        self.texts = []
        self.subreddits = []
        textsValues = list(self.data["selftext"].values())
        subredditsValues = list(self.data["subreddit"].values())
        print("len before", len(textsValues), len(subredditsValues))
        for i in range(len(textsValues)):
            if textsValues[i] != "":
                self.texts.append(textsValues[i])
                self.subreddits.append(subredditsValues[i])
        print("len after", len(self.texts), len(self.subreddits))
        print("complete dict to corresponding lists")

    def saveTextsAndSubreddits(self):
        with open("texts.txt", "wb") as f:
            pickle.dump(self.texts, f)
        with open("subreddits.txt", "wb") as f:
            pickle.dump(self.subreddits, f)

    def vectorize(self):
        vectorizer = TfidfVectorizer(stop_words="english")
        vecs = vectorizer.fit_transform(self.texts)
        v = vecs.toarray()
        print("vectorizing done")

        # calculate distances *takes much time
        z = linkage(v, metric='cosine')
        print("linkage done")

        with open("cosDist.binaryfile", "wb") as f:
            pickle.dump(z, f)


V = Vectorizing()
V.createLists()
V.saveTextsAndSubreddits()
V.vectorize()
