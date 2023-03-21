import os
# from dotenv import load_dotenv
from linkedin import LinkedIn
from hackernews import HackerNews
from json_manager import check_if_id_in_json, read_json, append_json

# load_dotenv()

# get linkedin access_token

linkedInAccessToken = 'AQUfasD8EMTLG5TKsr6156wMSWlQtzciR9zZ0rk3IcAGtwCcuYMlhRwH6bm17kjhZCaxzBxzJJKd0iC4qPd30YvaRedBGxfMg-evYedZA2soL0QMBKcT2_fJAJz8LbU9tELvXjHDGxM_3KTZJyYMVfEmneVqGXvRsCgkglO5iQ31bRu2kZj0pF01xjJmH47iLSrQY2jxqaiQ4FO1fi5cfCJWvAysnTt0uQcdnVXXh_iJNWEhypn3pcAv48JmG-J72E-HdHjdTGYXYsTQAqKC_m68b9rLqnU2eUgS3sZWNal_udZr94XS3Ky3UzDyDqt46omuyz0XQ4Uvi53agop5xR7JFmKQcQ'
linked = LinkedIn(linkedInAccessToken)
saveFileName = 'user_test.json'
hackerNews = HackerNews(saveFileName)

data = hackerNews.getTopStories(500)

for d in data:
    if(check_if_id_in_json(saveFileName,d)):
        break
    story_json = hackerNews.getItem(d)
    if(story_json):
        title, url = '', ''
        if('url' in story_json):
            url = story_json['url']
            title = story_json['title']
            res = linked.post_person_profile('whuBxeR1s6',title,url)
            if(res == 201):
                append_json(saveFileName, d)
