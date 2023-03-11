import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6288009731:AAG6Ue2bwm0oONNx2OEOqebtmE_XeSTGidQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzwBu5JPTn2yTFpJWk2NYc3I_vJ5JUKpLLKje8wxLDe5t64hPZy7ATlxm8Hn66i_L-qFEps4aoY_eJwalD8Za1NbCZLtRUXynHdpE8ogCoZ-QkM4-Wo9aZENQ8d_rcBOVsIWEY3RIvi0nnztxetBa2Pgi20pGoFKQIZlBNSpKbE-h3729E8_b8NJtY_y2GQ8g9i5wDq4GwLZjVwhNGxOg5SfhR9YCCm3JVXYY07WIAxQXxew0Tut4pUtsMzCyzFj2bgnvQIjnrzO3dLOXeS2gMJ3uHPC9-nN-UCLEB_r79DGiU1cI5h0gN61xzaJQU4fsZx4HC__NTQthEbFEdI6Co1nlhM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
