import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28922900"))
    API_HASH = os.environ.get("API_HASH", "e37f179737359ad89876787260d66aef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6125180497:AAFKIFRT_RA16qzy5A2pgosOtlrnKN9u1zQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJsBu2NK3-f5Z67g9PXJaX3dB7jFIFv4-ZTcrk6bUloLR5x4pneGLOpLT1Dr7rH78CKSX5suJkXVMsP6GPnndcKbtrKEtYk8edGbH40w1gNpF-GUhhtbXaXTHYKBTG_raL8O9gp7zYX-Zr-EkBhzNY31rN4r9_HCQZ3A70Q6qUymTd7ZvMP0mdfHuORj1KXOZzBBYmu0PFRUGbOjJPjGlVJPEa7DdSLhgqh8hMQft9MCVdqFvUZm1P-yE00oCk7PEXJh7u1peFo6ojonYFKyYTaTCz3XqanYIugLgTLbt_uJ29nNBtNEygy33giaIIJLgQLPh5GSFlSfmdzqphw4s7A4ZpA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "diviplayer_bot")
    SUPPORT = os.environ.get("SUPPORT", "diviplayersupport") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "divichannell") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/76d66069edb87588dbdac.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/76d66069edb87588dbdac.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6081060370")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
