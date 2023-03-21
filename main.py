import os
# from dotenv import load_dotenv
from linkedin import LinkedIn

# load_dotenv()

# get linkedin access_token

linkedInAccessToken = ''
print(linkedInAccessToken)
linked = LinkedIn(linkedInAccessToken)
print(linked.post_person_profile(''))

# from utils.linkedin import Linkedin
# # Authenticate using any Linkedin account credentials
# api = Linkedin('ngaurav456@gmail.com', 'L3khn2th124')
# print("hello")
# # GET a profile
# data = getTopStories(500)
# print(data)
# for d in data:
#     if(check_if_id_in_json(saveFileName, d)):
#         break
#     story_json = getItem(d)
#     if(story_json):
#         title, url = '', ''
#         print(story_json)
#         if('url' in story_json):
#             url = story_json['url']
#             title = story_json['title']
#             profile = api.post_feed_profile(title,url)
#             # profile = api.post_feed_organization(title,url,'90687023')
#             append_json(saveFileName, d)
