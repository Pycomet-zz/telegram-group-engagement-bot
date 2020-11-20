import os
import telebot
import telegram
from telebot import types
import emoji
import time
import pickle
from flask import Flask, request
from instagram_private_api import Client
from igramscraper.instagram import Instagram
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

# Telegram variables
TOKEN = os.getenv("TOKEN")

# Instagram variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# client = Client(USERNAME, PASSWORD)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = telebot.TeleBot(TOKEN, threaded=True)


# Database variables
DB_URI=f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@cluster0.9tlz7.mongodb.net"

# Start Mongo Connect
mongo = MongoClient(DB_URI)

sessions_db = mongo.engagement_db.sessions
subscribers_db = mongo.engagement_db.subscribers

ADMIN_ID = os.getenv("ADMIN_ID")
GROUP_ID = os.getenv("GROUP_ID")

insta = Instagram()

force_reply = types.ReplyKeyboardRemove(selective=False)
