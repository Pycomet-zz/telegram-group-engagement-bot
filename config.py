import os
import telebot
from telebot import types
import emoji
from flask import Flask, request


# Telegram variables
TOKEN = os.getenv("TOKEN")



# Instagram variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


import importdir
importdir.do("main/handlers", globals())
importdir.do("main/functions", globals())
