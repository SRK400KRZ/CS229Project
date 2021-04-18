import json
import time

import pandas as pd
import requests.auth


class RedditFetcher:
    def __init__(self, subreddits):
        self.subreddits = subreddits

    def fetchDataFromReddit(self):
        responses = []
        for subreddit in self.subreddits:
            client_auth = requests.auth.HTTPBasicAuth('rcZ8hipjewj8Rg', 'R8y2HYAWUdYDtwjw6hWZu8FLVC9-dw')
            post_data = {"grant_type": "password", "username": "Right_Drop_2757", "password": "hanover1!"}
            headers = {"User-Agent": "Crawler by Right_Drop_2757"}
            response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                     headers=headers)
            oneTimeToken = response.json()
            # Format of oneTimeToken
            # {'access_token': '857777483916-PlCXgi72SRbL4hcyikaJY4y4Mr2_rg',
            # 'token_type': 'bearer',
            # 'expires_in': 3600,
            # 'scope': '*'}

            headers = {"Authorization": "bearer " + oneTimeToken["access_token"],
                       "User-Agent": "Crawler by Right_Drop_2757"}
            response = requests.get("https://oauth.reddit.com/r/" + subreddit, headers=headers, params={"limit": 100})
            responses.append(response)
            print(subreddit, "fetched")
            time.sleep(1)
        return responses

    def makeJSONfromResponses(self, responses):
        df = pd.DataFrame()  # initialize dataframe
        for response in responses:
            try:
                for post in response.json()['data']['children']:
                    subrredit = post["data"]["subreddit"]
                    df = df.append({
                        'subreddit': post['data']['subreddit'],
                        'title': post['data']['title'],
                        'selftext': post['data']['selftext'],
                    }, ignore_index=True)
                print(subrredit, "DataFrame'D")
            except json.JSONDecodeError:
                print("*** decode error occurred")
            data = df.to_dict()
            with open("./data.json", mode='w') as f:
                json.dump(data, f, indent=4)
            print("  saved")

subrredits = ["gamedev", "engineering","ubuntu", "cscareerquestions", "EngineeringStudents", "askengineers"
              "learnprogramming", "compsci", "java", "javascript", "coding", "machinelearning",
              "howtohack", "cpp", "artificial", "python", "technology", "futurology", "gamedev",
             "design", "engineering", "compsci", "tech", "hacking", "networking", "infographics",
             "php", "virtualreality", "opensource"]
RF =  RedditFetcher(subrredits)
RF.makeJSONfromResponses(RF.fetchDataFromReddit())