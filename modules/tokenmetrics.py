
import requests, os
KEY=os.getenv("TOKENMETRICS_KEY")
BASE="https://api.tokenmetrics.com/v3"

def get_tm_summary(sym):
    try:
        h={"Authorization":f"Bearer {KEY}"}
        r=requests.get(f"{BASE}/assets/{sym}/summary",headers=h,timeout=10)
        d=r.json()
        return d
    except:
        return {}
