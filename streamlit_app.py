
import streamlit as st
import pandas as pd
from modules.quicknode import get_quicknode_price
from modules.tokenmetrics import get_tm_summary
from modules.signals import compute_signals
from modules.backtester import run_backtest

st.set_page_config(page_title="Fusion Quant Terminal", layout="wide")
st.title("Fusion Quant Terminal")

assets = st.sidebar.multiselect("Assets", ["BTC","ETH","SOL","CRO","WLFI"], ["BTC","ETH"])
lookback = st.sidebar.slider("Lookback Days", 7, 200, 60)

rows=[]
for a in assets:
    price = get_quicknode_price(a)
    tm = get_tm_summary(a)
    sig = compute_signals(a, tm, lookback)
    rows.append({"Asset":a,"Price":price,"Fusion Score":sig["fusion_score"],"Signal":sig["signal"]})

df=pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

st.header("Backtest")
if st.button("Run Backtest"):
    bt = run_backtest(df)
    st.line_chart(bt["equity"])
