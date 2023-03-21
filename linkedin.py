import logging
import requests

class LinkedIn():
    def __init__(self, access_token):
        self.access_token = access_token
        self.post_url = 'https://api.linkedin.com/rest/posts'
    def get_access_token():
        pass
    def post_person_profile(self,person_id):
        data = {
                "author": "urn:li:person:whuBxeR1s6",
                "commentary": "test article post",
                    "visibility": "PUBLIC",
                    "distribution": {
                    "feedDistribution": "MAIN_FEED",
                    "targetEntities": [],
                    "thirdPartyDistributionChannels": []
                    },
                    "content": {
                        "article": {
                            "source": "https://petals.ml/",
                            "thumbnail": "urn:li:image:C49klciosC89",
                            "title": "prod test title two",
                            "description": "test description"
                        }
                    },
                    "lifecycleState": "PUBLISHED",
                    "isReshareDisabledByAuthor": False
                }
        response = requests.post(self.post_url,data=data)
        return response.status_code
    def post_organization_profile(self,organization_id):
        pass