# CS229Project
**REDDIT**

A)
  Reddit api documentation
  https://www.reddit.com/dev/api/

  JSON format 

B) resouce 
  https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
  


Clients must authenticate with **OAuth2**
Clients connecting via OAuth2 may make up to 60 requests per minute. Monitor the following response headers to ensure that you're not exceeding the limits:

Project Topic: Unsupervised Clustering of Reddit Communities

Task: Retrieve reddit posts for a selection of subreddits (e.g., related to computer science, data science, machine learning); treating the posts in each subreddit like a "document", perform automatic clustering of the subreddits to identify those that are most similar.

Subtasks:
1. Identify a set of subreddits (around 20)
2. Retrieve enough posts to give at least 10,000 words for each subreddit. (excluding quoted posts); store the data for each in a separate file
3. Cleaning the data (natural language processing)
4. Do automatic clustering

For both 3 and 4 you will use available tools.


/r/gamedev
/r/engineering
/r/ubuntu
/r/cscareerquestions
/r/EngineeringStudents
/r/askengineers

Coding
/r/learnprogramming
/r/compsci
/r/java
/r/javascript
/r/coding
/r/machinelearning
/r/howtohack
/r/cpp
/r/artificial

Python
/r/python



/r/technology
  /r/futurology
/r/gamedev
/r/design
/r/engineering
/r/compsci
/r/tech
/r/hacking
/r/networking
/r/infographics
  /r/php
/r/virtualreality
/r/opensource


HOWTO
Run files in the following order
RedditFetcher.py -> Vectorizing.py -> Clustering.py
Note: for the sake of convenience, classes are separated and never called consecutively.
