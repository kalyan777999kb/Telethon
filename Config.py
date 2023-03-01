import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28964664"))
    API_HASH = os.environ.get("API_HASH", "425269d29ce9fb5524cdeb52b36319b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047283966:AAGUcHm7hh7jeKDapdl3Fpu7jlpXGIflwMw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQG59zgAP0VCeyU8PHpzscMTI3fQkyZZJamI0Z5rdhr1lM-WJuhMmJa_BW6_Sxh44WAyiqg-nuDjOnQuKn2l155DeOeYuo9ppb_NIB9D0-SVW_07TgG9hsRmSD2IH7wJdg7zv11JOKrVEZsd_4wSxKhsuFJb2J2LmLYnjef8DulnzsleA2hoXBC9dvwVNdpcrvsF7shPY5UD_InoFjA6tLbFxzTtqmbHZJIGdxLZvF6LNsY3IxLm0YCchHMWc02QgJthqA0MBpoJykyBwidoriTS-AyM_08GGZal4jcRyTie-4WV_dGfl0oHZEJwiRGm1_Fetm2ZIRJ66OsjEO3vL9NWqyDr_gAAAAFcbw-uAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Anu_musicrobot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/telugu_friends_hub") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/SoulSpeakss") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/76d66069edb87588dbdac.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/76d66069edb87588dbdac.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5845749678")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', " True") # Change it to "True"
