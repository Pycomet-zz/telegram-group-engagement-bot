from config import *
from datetime import datetime


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

        # ## Check user feed for post relating to this code
        # data = client.user_feed(self.insta_id).get('items')

        # results = [post['id'] for post in data if post['code'] == code]
        # output = results[0] if len(results) != 0 else None
        
        # self.media_id = output.split("_")[0] if output is not None else None
        # return self.media_id

        ##################################################
        try:
            data = insta.get_medias_by_code(code)
        except:
            # authentication supported
            time.sleep(3)
            insta.with_credentials(USERNAME, PASSWORD)
            insta.login()
            data = insta.get_medias_by_code(code)

        self.media_id = data.identifier if data is not None else None
        return self.media_id


    def get_list(self):
        "Fetch current list from database"
        data = [i for i in sessions_db.find()][-10:] #return the last 10 links
        return data



    def check_likes(self):
        "Check the list if the user has liked them"
        data = self.get_list()
        for link in data:    
            query_set = client.media_likers(media_id=link['media_id']).get("users")
            likers = [i['pk'] for i in query_set]
            for user in likers:
                if self.insta_id == user:
                    self.likes += 1
                else:
                    pass


    def check_comments(self):
        "Checks the list if the user has commented on them"
        data = self.get_list()
        for link in data:    
            query_set = client.media_comments(media_id=link['media_id']).get("comments")
            comments = [i['user_id'] for i in query_set if query_set != None]
            for user in comments:
                if self.insta_id == user:
                    self.comments += 1
                else:
                    pass


    def get_status(self):
        "Returns the user status of number of likes"

        #Get the susbcribers
        subscribers = Subscriber().get_subscribers()

        if self.user in subscribers:
            return True
        
        elif self.likes >= 10 or self.comments >= 10:
            return True

        else:
            # return True
            return f"You liked {self.likes} pictures and {self.comments} comments"

        
    def add_to_list(self):
        "Send new post to database"
        current_list = self.get_list()

        media_ids = [i['media_id'] for i in current_list]
        new_post = {
            'media_id': self.media_id,
            'media_url': self.url,
            'time_posted': datetime.utcnow()
        }

        if self.media_id not in media_ids:
            result = sessions_db.insert_one(new_post).inserted_id
            print(result)
        
        else:
            pass







class Subscriber(object):

    def get_subscribers(self):
        "Fetch Documents from database"
        data = [i['username'] for i in subscribers_db.find()]
        return data

    def add_subscriber(self, user):
        "Add new subscriber to the database"
        new_post = {
            'username': user,
        }
        result = subscribers_db.insert_one(new_post).inserted_id
        return result

    def remove_subscriber(self, user):
        "Remove subscriber from database"
        criteria = {
            'username': user
        }
        subscribers_db.delete_one(criteria)


    def activate(self, user_obj):
        "Adds user handle to data storage"
        user = user_obj.text
        users = self.get_subscribers()

        if user in users:
            return bot.send_message(
                int(ADMIN_ID),
                "Already a subscriber."
                )
        else:
            result = self.add_subscriber(user)
            return bot.send_message(
                int(ADMIN_ID),
                f"<b>{user} Subscription activated! - {result}</b>",
                parse_mode=telegram.ParseMode.HTML,
                )


    def deactivate(self, user_obj):
        "removes user handle to data storage"
        user = user_obj.text
        users = self.get_subscribers()

        if user not in users:
            return bot.send_message(
                int(ADMIN_ID),
                "This user is not a subscriber"
                )
        else:
            self.delete_subscriber(user)
            return bot.send_message(
                int(ADMIN_ID),
                f"<b>{user} Subscription deactivated!</b>",
                parse_mode=telegram.ParseMode.HTML,
                )



