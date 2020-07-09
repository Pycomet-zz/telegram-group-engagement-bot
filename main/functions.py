from config import *


class Action(object):

    def __init__(self, username, url):
        self.user = username
        self.insta_id = ''
        self.url = url
        self.media_id = ''

        self.likes = 0 # Marking the posts the user has liked
        self.comments = 0 # Marking the posts the user has commented on


    def get_user_id(self):
        "Returns The User Instagram's ID"

        data = client.username_info(self.user)
        self.insta_id = data['user']['pk']


    def get_media_id(self):
        "Returns The Target Media ID"
        code = self.url.strip("/").split("/")[-1]

        ## Check user feed for post relating to this code
        data = client.user_feed(self.insta_id).get('items')

        results = [post['id'] for post in data if post['code'] == code]
        self.media_id = results[0] if len(results) != 0 else None
        return self.media_id

    def get_list(self):
        "Gets the curent list for checking"
        file = open('list.json', 'rb')
        data = pickle.load(file)
        file.close()
        return data

    def check_likes(self):
        "Check the list if the user has liked them"
        data = self.get_list()
        pass

    def check_comments(self):
        "Checks the list if the user has commented on them"
        data = self.get_list()
        pass
