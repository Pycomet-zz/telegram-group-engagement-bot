from config import *


class Subscriber(object):

    def __init__(self, tg_id, username):
        self.user_id = tg_id
        self.user_handle = username

    def activate(self):
        "Adds user to data storage"
        pass


    def deactivate(self):
        "removes user to data storage"
        pass


    def is_active(self):
        "checks activation status"
        pass

    def get_subscribers():
        pass