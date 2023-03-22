import os
# from dotenv import load_dotenv
from linkedin import LinkedIn
from facebook import FaceBook
from hackernews import HackerNews
from json_manager import check_if_id_in_json, read_json, append_json

# load_dotenv()

# get linkedin access_token
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
linkedInAccessToken = ''
facebookAccessToken = ''
linked = LinkedIn(linkedInAccessToken)
facebook = FaceBook(facebookAccessToken)
saveFileName = os.path.join(ROOT_DIR,'user_test.json')
hackerNews = HackerNews(saveFileName)

data = hackerNews.getTopStories(5)

for d in data:
    if(check_if_id_in_json(saveFileName,d)):
        pass
    else:
        story_json = hackerNews.getItem(d)
        if(story_json):
            title, url = '', ''
            if('url' in story_json):
                url = story_json['url']
                title = story_json['title']
                res_linkedin = linked.post_person_profile('whuBxeR1s6',title,url)
                res_facebook = facebook.post_organization_profile(title,url)
                if(res_linkedin == 201 and res_facebook):
                    append_json(saveFileName, d)
