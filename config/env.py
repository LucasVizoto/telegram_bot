from dotenv import load_dotenv
from os import getenv

load_dotenv()

env_variables = {
    'CHAT_ID': getenv('CHAT_ID'),
    'BOT_NAME': getenv('BOT_NAME'),
    'BOT_TOKEN':getenv('BOT_TOKEN'),
    'GOOGLE_API_KEY': getenv('GOOGLE_API_KEY'),
    'GOOGLE_MODEL': getenv('GOOGLE_MODEL')
}
