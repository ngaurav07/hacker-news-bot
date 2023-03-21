import logging
import json
import requests

class LinkedIn():
    def __init__(self, access_token):
        self.access_token = access_token
        self.post_url = 'https://api.linkedin.com/rest/posts'
        self.headers = { "Authorization" : 'Bearer '+self.access_token, "LinkedIn-Version": "202206"}
    def get_access_token():
        pass
    def post_person_profile(self,person_id,message,url):
        data = {
                "author": "urn:li:person:{}".format(person_id),
                "commentary": "{}".format(message),
                "visibility": "PUBLIC",
                "contentLandingPage":"{}".format(url),
                "distribution": {
                    "feedDistribution": "MAIN_FEED",
                    "targetEntities": [],
                    "thirdPartyDistributionChannels": []
                },
                "content": {
                "article": {
                    "source": "{}".format(url),
                    "title": "{}".format(message),
                    "description": "{}".format(message)
                }
                },
                "lifecycleState": "PUBLISHED",
                "isReshareDisabledByAuthor": False
        }
        response = requests.post(self.post_url,data=json.dumps(data), headers= self.headers)
        return response.status_code
    def post_organization_profile(self,organization_id):
        pass