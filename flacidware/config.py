import os 
from dotenv import load_dotenv 


load_dotnev() 

class Config():
    btoken = os.getenv("BOT_TOKEN")
    aid = os.getenv("API_ID")
    aih = os.getenv("API_HASH") 
    my = os.getenv("MY_ID")
    cid = os.getenv("CHAT_ID") 
    ccid = os.getenv("CHANNEL_CHATID")
    cname = os.getenv("CHANNEL_NAME")
    mongo = os.getenv("MONGO_STR")
    audio = os.getenv("AUDIO_THUMBNAIL")
    video = os.getenv("VIDEO_THUMBNAIL")



