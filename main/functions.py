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
        output = results[0] if len(results) != 0 else None
        self.media_id = output.split("_")[0]
        return self.media_id

    def get_list(self):
        "Gets the curent list for checking"
        file = open("main/list.json", 'rb')
        try:
            data = pickle.load(file)
        except EOFError as e:
            data = []
        file.close()
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
            comments = [i['user_id'] for i in query_set]
            for user in comments:
                if self.insta_id == user:
                    self.comments += 1
                else:
                    pass


    def get_status(self):
        "Returns the user status of number of likes"

        #Get the susbcribers
        file = open("main/subscribers.json", "rb")
        subscribers = pickle.load(file)
        file.close()

        if self.likes == 15 and self.comments == 15:
            return True

        elif self.user in subscribers:
            return True

        else:
            return f"You liked {self.likes} pictures and {self.comments} comments"

    def add_to_list(self):
        "Adds the user data to the list"
        
        #List manipulation
        current_list = self.get_list()
        
        if len(current_list) >= 15:
            current_list.remove(current_list[0])
        
        elif current_list[-1].get("media_id") == self.media_id:
            pass
        
        else:
            user = {
                'id': current_list[-1]['id'] + 1,
                'media_id': self.media_id,
                'media_url': self.url
            }
            current_list.append(user)

        file = open("main/list.json", "wb")
        pickle.dump(current_list, file)
        file.close()
        






class Subscriber(object):
    def __init__(self):
        self.file = ''

    def get_subscribers(self):
        "Return The List of subscribers"
        self.file = open("main/subscribers.json", "rb")
        try:
            data = pickle.load(self.file)
        except EOFError as e:
            data = []    
        self.file.close
        return list(data)

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
            self.file = open("main/subscribers.json", "wb")
            users.append(user)
            pickle.dump(users, self.file)
            self.file.close()
            return bot.send_message(
                int(ADMIN_ID),
                f"<b>{user} Subscription activated!</b>",
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
            self.file = open("main/subscribers.json", "wb")
            users.remove(user)
            pickle.dump(users, self.file)
            self.file.close()
            return bot.send_message(
                int(ADMIN_ID),
                f"<b>{user} Subscription deactivated!</b>",
                parse_mode=telegram.ParseMode.HTML,
                )



