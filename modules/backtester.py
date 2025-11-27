
import pandas as pd

def run_backtest(df):
    eq = pd.Series([100])
    # placeholder simple model
    for i in range(1,31):
        eq.loc[i]=eq.loc[i-1]*1.001
    return {"equity":eq}
