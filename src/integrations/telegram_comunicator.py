from telebot import TeleBot

from config.env import env_variables

API_TOKEN = env_variables['API_TOKEN']
bot = TeleBot(API_TOKEN)