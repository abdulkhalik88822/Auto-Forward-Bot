from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH","138001c981e1dbb5b9b2218a6bf66f03")
      API_ID = int(getenv("API_ID","29665277"))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001105967819").replace("\n", " ").split(' '))
