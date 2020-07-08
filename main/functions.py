from config import *


class Action(object):

    def __init__(self, username, url):
        user = username
        insta_id = ''
        url = url


    def get_user_id(self):
        "Returns The User Instagram's ID"

        data = client.username_info(self.username)
        self.insta_id = data['user']['pk']


    def get_media_id(self):
        "Returns The Target Media ID"
        code = self.url.strip("/").split("/")[-1]

        ## Check user feed for post relating to this code
        data = client.user_feed(self.insta_id, **kwargs).get('items')

        for post in data:
            if post['code'] == str(code):
                self.post_id == post['id']
                return self.post_id
        return None       



    def check_likes(self):
        "Check the list if the user has liked them"
        pass

    def check_comments(self):
        "Checks the list if the user has commented on them"
        pass
