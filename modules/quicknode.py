
import requests, os

BASE = "https://api.quicknode.com/prices"
KEY = os.getenv("QUICKNODE_KEY")

def get_quicknode_price(sym):
    try:
        r=requests.get(f"{BASE}/{sym}-USD?apikey={KEY}",timeout=10)
        return r.json().get("price")
    except:
        return None
