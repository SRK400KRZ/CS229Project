import json
import numpy as np

# from data.json, craete two lists: textBodies[] and subreddit[]
from sklearn.cluster import KMeans

with open('data.json') as f:
    data = json.load(f)
# dict_keys(['selftext', 'subreddit', 'title'])

print(type(data["selftext"]["139"]), data["selftext"]["139"])
texts = []
subreddits = []
textsValues = list(data["selftext"].values())
subredditsValues = list(data["subreddit"].values())
print("len before", len(textsValues), len(subredditsValues))
for i in range(len(textsValues)):
    if textsValues[i] != "":
        texts.append(textsValues[i])
        subreddits.append(subredditsValues[i])

print("len after", len(texts), len(subreddits))
print("complete dict to corresponding lists")

nptexts = np.array(texts)
pred = KMeans(n_clusters=10).fit_predict(nptexts)
print(pred)