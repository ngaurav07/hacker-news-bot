import os
# from dotenv import load_dotenv
from linkedin import LinkedIn
from hackernews import HackerNews
from json_manager import check_if_id_in_json, read_json, append_json

# load_dotenv()

# get linkedin access_token

linkedInAccessToken = ''
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
