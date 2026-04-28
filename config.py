import os
import sys
from dotenv import load_dotenv
load_dotenv()

# FinnHub
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# Cluade
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# price_move_sig.py
POS_PERCENT_THRESHOLD = 2
NEG_PERCENT_THRESHOLD = -2

# web_search.py
MODEL = "claude-opus-4-6"
MAX_TOKENS = 1046

# line_bot/handler.py - Line SDK
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", None)
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

if not LINE_CHANNEL_SECRET:
    print("Spcify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if not LINE_CHANNEL_ACCESS_TOKEN:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)