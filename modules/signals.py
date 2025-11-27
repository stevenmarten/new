
import numpy as np

def compute_signals(asset, tm, lookback):
    momentum = tm.get("momentum",{}).get("score",50)
    vol = tm.get("volatility",{}).get("score",50)
    grade = tm.get("grade",50)

    fusion = 0.5*momentum + 0.3*grade - 0.2*vol
    signal = "LONG" if fusion>55 else "NEUTRAL" if fusion>45 else "SHORT"

    return {"fusion_score":fusion,"signal":signal}
