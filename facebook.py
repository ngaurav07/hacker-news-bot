import logging
import json
import requests

class FaceBook():
    def __init__(self, access_token):
        self.access_token = access_token
        self.post_url = "https://graph.facebook.com/v16.0/119366477752277/feed"
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
    def post_organization_profile(self,message,url):
        organization_url = ''
        if(url):
            organization_url = self.post_url+"?message={}&link={}&access_token={}".format(message,url,self.access_token)
        else:
            organization_url = self.post_url+"?message={}&access_token={}".format(message,self.access_token)
        response = requests.post(organization_url)
        return response.status_code