from config import *


class Storage(object):

    def __init__(self, tg_id, username):
        user_id = tg_id
        user_handle = username

    def check_store(self):
        "Checks if user is stored already"
        pass

    def add_to_store(self):
        "Write user data to database"
        pass

    def add_new_link(self):
        "Add Link Received from this instance user"
        pass