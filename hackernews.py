import requests
from json_manager import check_if_id_in_json, read_json, append_json

class HackerNews():

    def __init__(self, save_json_path):
        self.saveFileName = save_json_path
        self.hackerNewsApi= 'https://hacker-news.firebaseio.com/v0'
        self.newStroriesApi='/newstories.json'
        self.topStoriesApi ='/topstories.json'
        self.hackerNewsJobApi = 'jobstories.json'
        self.getItemApi = '/item/'

    def getItem(self,itemNumber):
        response = requests.get(self.hackerNewsApi+self.getItemApi+'{}.json'.format(itemNumber))
        if response.status_code == 200:
            return response.json()

    def getTopStories(self,maxNumbers):
        response = requests.get(self.hackerNewsApi+self.topStoriesApi)
        # Check if the request was successful (HTTP status code 200 indicates success)
        if response.status_code == 200:
            # Get the response content as a JSON object
            json_data = response.json()
            # Process the JSON data as needed
            return json_data[:maxNumbers]
        else:
            # Print an error message if the request was unsuccessful
            print('Error:', response.status_code)

