from pprint import pprint

import pandas as pd


import requests.auth
client_auth = requests.auth.HTTPBasicAuth('rcZ8hipjewj8Rg', 'R8y2HYAWUdYDtwjw6hWZu8FLVC9-dw')
post_data = {"grant_type": "password", "username": "Right_Drop_2757", "password": "hanover1!"}
headers = {"User-Agent": "Crawler by Right_Drop_2757"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
oneTimeToken = response.json()
# Format of oneTimeToken
# {'access_token': '857777483916-PlCXgi72SRbL4hcyikaJY4y4Mr2_rg',
# 'token_type': 'bearer',
# 'expires_in': 3600,
# 'scope': '*'}

headers = {"Authorization": "bearer " + oneTimeToken["access_token"], "User-Agent": "Crawler by Right_Drop_2757"}
response = requests.get("https://oauth.reddit.com/r/compsci", headers=headers, params={"limit": 100})
df = pd.DataFrame()  # initialize dataframe
for post in response.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)
    pprint(post['data']['selftext'])

print(len(df))


