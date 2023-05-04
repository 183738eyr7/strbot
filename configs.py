from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','26516151'))
    API_HASH = getenv('API_HASH','898ef05eb836d4a0349909bfcf6fdd19')
    BOT_TOKEN = getenv('BOT_TOKEN','5800020398:AAEQ8dQj9ML47iTW7Zms4xIXhujT6ua2Ldw')

config = Config()
