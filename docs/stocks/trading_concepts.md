## Strategy
  - Entry indicator
    - Entry position.
    - When to enter the market
    - Best possible point to entry.
    - Test it is on historical data.
    - Initial trade is backtest.
  - Trade management 
    - Start when we open the trade
    - When to close it.
    - How to move 
    - How to deal with losing trade. 
    - Larget part of the work. 
    - The clousre is where fee.
    - How long it was open
    - Was it open overnight.
    - Commisions
  - Stategy 
    - Test indicator
    - Trade management. 
    - Trying to isolate the trading indicator. 
  - Design : find best indicator -> Trade management. 
   
### Data aqusion:

#### yfinance

```jsunicoderegexp
import yfinance as yf

# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a ticker object
ticker = yf.Ticker(ticker_symbol)

# Download historical data
#historical_data = ticker.history(start="1990-01-01", end="2022-12-31", interval='1d')
historical_data = ticker.history(period="1020d", interval='1h')

len(historical_data)


```

By min

```jsunicoderegexp
historical_data = ticker.history(period="15m", start="2023-07-01", end="2023-07-16")
```

### Support resistance

##### Read data

```jsunicoderegexp
import pandas as pd
df = pd.read_csv("EURUSD_Candlestick_1_Hour_BID_01.07.2020-15.07.2023.csv")
df.columns=['time', 'open', 'high', 'low', 'close', 'volume']
#Check if NA values are in data
df=df[df['volume']!=0]
df.reset_index(drop=True, inplace=True)
df.isna().sum()
df.head(10)
```

###### Pivot

```jsunicoderegexp
def pivotid(df1, l, n1, n2): #n1 n2 before and after candle l
    if l-n1 < 0 or l+n2 >= len(df1):
        return 0
    
    pividlow=1
    pividhigh=1
    for i in range(l-n1, l+n2+1):
        if(df1.low[l]>df1.low[i]):
            pividlow=0
        if(df1.high[l]<df1.high[i]):
            pividhigh=0
    if pividlow and pividhigh:
        return 3
    elif pividlow:
        return 1
    elif pividhigh:
        return 2
    else:
        return 0
    
df['pivot'] = df.apply(lambda x: pivotid(df, x.name,10,10), axis=1)

```

```jsunicoderegexp
mport numpy as np
def pointpos(x):
    if x['pivot']==1:
        return x['low']-1e-3
    elif x['pivot']==2:
        return x['high']+1e-3
    else:
        return np.nan

df['pointpos'] = df.apply(lambda row: pointpos(row), axis=1)
```

#### Support / Resistance

```jsunicoderegexp
def support(df1, l, n1, n2): #n1 n2 before and after candle l
    if ( df1.low[l-n1:l].min() < df1.low[l] or
        df1.low[l+1:l+n2+1].min() < df1.low[l] ):
        return 0

    candle_body = abs(df1.open[l]-df1.close[l])
    lower_wick = min(df1.open[l], df1.close[l])-df1.low[l]
    if (lower_wick > candle_body) and (lower_wick > wick_threshold): 
        return 1
    
    return 0

def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
    if ( df1.high[l-n1:l].max() > df1.high[l] or
       df1.high[l+1:l+n2+1].max() > df1.high[l] ):
        return 0
    
    candle_body = abs(df1.open[l]-df1.close[l])
    upper_wick = df1.high[l]-max(df1.open[l], df1.close[l])
    if (upper_wick > candle_body) and (upper_wick > wick_threshold) :
        return 1

    return 0
```

### Distance from support resistance

```jsunicoderegexp
def closeResistance(l,levels,lim, df):
    if len(levels)==0:
        return 0
    c1 = abs(df.high[l]-min(levels, key=lambda x:abs(x-df.high[l])))<=lim
    c2 = abs(max(df.open[l],df.close[l])-min(levels, key=lambda x:abs(x-df.high[l])))<=lim
    c3 = min(df.open[l],df.close[l])<min(levels, key=lambda x:abs(x-df.high[l]))
    c4 = df.low[l]<min(levels, key=lambda x:abs(x-df.high[l]))
    if( (c1 or c2) and c3 and c4 ):
        return min(levels, key=lambda x:abs(x-df.high[l]))
    else:
        return 0
    
def closeSupport(l,levels,lim, df):
    if len(levels)==0:
        return 0
    c1 = abs(df.low[l]-min(levels, key=lambda x:abs(x-df.low[l])))<=lim
    c2 = abs(min(df.open[l],df.close[l])-min(levels, key=lambda x:abs(x-df.low[l])))<=lim
    c3 = max(df.open[l],df.close[l])>min(levels, key=lambda x:abs(x-df.low[l]))
    c4 = df.high[l]>min(levels, key=lambda x:abs(x-df.low[l]))
    if( (c1 or c2) and c3 and c4 ):
        return min(levels, key=lambda x:abs(x-df.low[l]))
    else:
        return 0
        
def is_below_resistance(l, level_backCandles, level, df):
    return df.loc[l-level_backCandles:l-1, 'high'].max() < level

def is_above_support(l, level_backCandles, level, df):
    return df.loc[l-level_backCandles:l-1, 'low'].min() > level          
```

### Score
```jsunicoderegexp


def check_candle_signal(l, n1, n2, backCandles, df):
    ss = []
    rr = []
    for subrow in range(l-backCandles, l-n2):
        if support(df, subrow, n1, n2):
            ss.append(df.low[subrow])
        if resistance(df, subrow, n1, n2):
            rr.append(df.high[subrow])
    
    ss.sort() #keep lowest support when popping a level
    for i in range(1,len(ss)):
        if(i>=len(ss)):
            break
        if abs(ss[i]-ss[i-1])<=0.0001: # merging close distance levels
            ss.pop(i)

    rr.sort(reverse=True) # keep highest resistance when popping one
    for i in range(1,len(rr)):
        if(i>=len(rr)):
            break
        if abs(rr[i]-rr[i-1])<=0.0001: # merging close distance levels
            rr.pop(i)

    #----------------------------------------------------------------------
    # joined levels
    rrss = rr+ss
    rrss.sort()
    for i in range(1,len(rrss)):
        if(i>=len(rrss)):
            break
        if abs(rrss[i]-rrss[i-1])<=0.0001: # merging close distance levels
            rrss.pop(i)
    cR = closeResistance(l, rrss, 150e-5, df)
    cS = closeSupport(l, rrss, 150e-5, df)
    #----------------------------------------------------------------------

    # cR = closeResistance(l, rr, 150e-5, df)
    # cS = closeSupport(l, ss, 150e-5, df)
    # could we consider the average RSI for the trend momentum?
    if (cR and is_below_resistance(l,6,cR, df) and df.RSI[l-1:l].min()<45 ):#and df.RSI[l]>65
        return 1
    elif(cS and is_above_support(l,6,cS,df) and df.RSI[l-1:l].max()>55 ):#and df.RSI[l]<35
        return 2
    else:
        return 0



```

```jsunicoderegexp
from tqdm import tqdm

n1 = 8
n2 = 6
backCandles = 140

signal = [0 for i in range(len(df))]

for row in tqdm(range(backCandles+n1, len(df)-n2)):
    signal[row] = check_candle_signal(row, n1, n2, backCandles, df)

df["signal"] = signal

```

```jsunicoderegexp
import numpy as np
def pointpos(x):
    if x['signal']==1:
        return x['high']+1e-4
    elif x['signal']==2:
        return x['low']-1e-4
    else:
        return np.nan

df['pointpos'] = df.apply(lambda row: pointpos(row), axis=1)
```


```jsunicoderegexp
dfpl = df[100:300]
import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['open'],
                high=dfpl['high'],
                low=dfpl['low'],
                close=dfpl['close'])])

fig.update_layout(
    autosize=False,
    width=1000,
    height=800, 
    paper_bgcolor='black',
    plot_bgcolor='black')
fig.update_xaxes(gridcolor='black')
fig.update_yaxes(gridcolor='black')
fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
                marker=dict(size=8, color="MediumPurple"),
                name="Signal")
fig.show()
```

```jsunicoderegexp
def check_candle_signal_plot(l, n1, n2, backCandles, df, proximity):
    ss = []
    rr = []
    for subrow in range(l-backCandles, l-n2):
        if support(df, subrow, n1, n2):
            ss.append(df.low[subrow])
        if resistance(df, subrow, n1, n2):
            rr.append(df.high[subrow])
    
    ss.sort() #keep lowest support when popping a level
    i = 0
    while i < len(ss)-1:
        if abs(ss[i]-ss[i+1]) <= proximity:
            # ss[i] = (ss[i]+ss[i+1])/2
            # del ss[i+1]
            del ss[i+1]
        else:
            i+=1

    rr.sort(reverse=True) # keep highest resistance when popping one
    i = 0
    while i < len(rr)-1:
        if abs(rr[i]-rr[i+1]) <= proximity:
            #rr[i] = (rr[i]+rr[i+1])/2
            #del rr[i+1]
            del rr[i]
        else:
            i+=1

    dfpl=df[l-backCandles-n1:l+n2+50]
    fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['open'],
                high=dfpl['high'],
                low=dfpl['low'],
                close=dfpl['close'])])

    c=0
    while (1):
        if(c>len(ss)-1 ):
            break
        fig.add_shape(type='line', x0=l-backCandles-n1, y0=ss[c],
                    x1=l,
                    y1=ss[c],
                    line=dict(color="MediumPurple",width=2), name="Support"
                    )
        c+=1

    c=0
    while (1):
        if(c>len(rr)-1 ):
            break
        fig.add_shape(type='line', x0=l-backCandles-n1, y0=rr[c],
                    x1=l,
                    y1=rr[c],
                    line=dict(color="Red",width=2), name="Resistance"
                    )
        c+=1    

    # fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
    #             marker=dict(size=5, color="MediumPurple"),
    #             name="Signal")

    fig.update_layout(
    autosize=False,
    width=1000,
    height=800,)
    
    fig.show()
 
 
    #----------------------------------------------------------------------
    cR = closeResistance(l, rr, 150e-5, dfpl)
    cS = closeSupport(l, ss, 150e-5, dfpl)
    #print(cR, is_below_resistance(l,6,cR, dfpl))
    if (cR and is_below_resistance(l,6,cR, dfpl) ):#and df.RSI[l]>65
        return 1
    elif(cS and is_above_support(l,6,cS,dfpl) ):#and df.RSI[l]<35
        return 2
    else:
        return 0
```


#### Backtesting

```jsunicoderegexp
from backtesting import Strategy
from backtesting import Backtest

dfopt = df[-10000:-5000]
def SIGNAL():
    return dfopt.TotalSignal

class MyStrat(Strategy):
    mysize = 3000
    slcoef = 1.1
    TPSLRatio = 1.5
    
    def init(self):
        super().init()
        self.signal1 = self.I(SIGNAL)

    def next(self):
        super().next()
        slatr = self.slcoef*self.data.ATR[-1]
        TPSLRatio = self.TPSLRatio
       
        if self.signal1==2 and len(self.trades)==0:
            sl1 = self.data.Close[-1] - slatr
            tp1 = self.data.Close[-1] + slatr*TPSLRatio
            self.buy(sl=sl1, tp=tp1, size=self.mysize)
        
        elif self.signal1==1 and len(self.trades)==0:         
            sl1 = self.data.Close[-1] + slatr
            tp1 = self.data.Close[-1] - slatr*TPSLRatio
            self.sell(sl=sl1, tp=tp1, size=self.mysize)

bt = Backtest(dfopt, MyStrat, cash=250, margin=1/30)
stats, heatmap = bt.optimize(slcoef=[i/10 for i in range(10, 26)],
                    TPSLRatio=[i/10 for i in range(10, 26)],
                    maximize='Return [%]', max_tries=300,
                        random_state=0,
                        return_heatmap=True)
stats
```

### Heatmap

```jsunicoderegexp
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Convert multiindex series to dataframe
heatmap_df = heatmap.unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_df, annot=True, cmap='viridis', fmt='.0f')
plt.show()
```

# Channel detection
```jsunicoderegexp
def isPivot(candle, window):
    """
    function that detects if a candle is a pivot/fractal point
    args: candle index, window before and after candle to test if pivot
    returns: 1 if pivot high, 2 if pivot low, 3 if both and 0 default
    """
    if candle-window < 0 or candle+window >= len(df):
        return 0
    
    pivotHigh = 1
    pivotLow = 2
    for i in range(candle-window, candle+window+1):
        if df.iloc[candle].Low > df.iloc[i].Low:
            pivotLow=0
        if df.iloc[candle].High < df.iloc[i].High:
            pivotHigh=0
    if (pivotHigh and pivotLow):
        return 3
    elif pivotHigh:
        return pivotHigh
    elif pivotLow:
        return pivotLow
    else:
        return 0

```

```jsunicoderegexp
window=3
df['isPivot'] = df.apply(lambda x: isPivot(x.name,window), axis=1)
```

```jsunicoderegexp
def collect_channel(candle, backcandles, window):
    localdf = df[candle-backcandles-window:candle-window]
    #localdf['isPivot'] = localdf.apply(lambda x: isPivot(x.name,window), axis=1)
    highs = localdf[localdf['isPivot']==1].High.values
    idxhighs = localdf[localdf['isPivot']==1].High.index
    lows = localdf[localdf['isPivot']==2].Low.values
    idxlows = localdf[localdf['isPivot']==2].Low.index
    
    if len(lows)>=3 and len(highs)>=3:
        sl_lows, interc_lows, r_value_l, _, _ = stats.linregress(idxlows,lows)
        sl_highs, interc_highs, r_value_h, _, _ = stats.linregress(idxhighs,highs)
    
        return(sl_lows, interc_lows, sl_highs, interc_highs, r_value_l**2, r_value_h**2)
    else:
        return(0,0,0,0,0,0)
```

```jsunicoderegexp
def collect_channel(candle, backcandles, window):
    localdf = df[candle-backcandles-window:candle-window]
    #localdf['isPivot'] = localdf.apply(lambda x: isPivot(x.name,window), axis=1)
    highs = localdf[localdf['isPivot']==1].High.values
    idxhighs = localdf[localdf['isPivot']==1].High.index
    lows = localdf[localdf['isPivot']==2].Low.values
    idxlows = localdf[localdf['isPivot']==2].Low.index
    
    if len(lows)>=3 and len(highs)>=3:
        sl_lows, interc_lows, r_value_l, _, _ = stats.linregress(idxlows,lows)
        sl_highs, interc_highs, r_value_h, _, _ = stats.linregress(idxhighs,highs)
    
        return(sl_lows, interc_lows, sl_highs, interc_highs, r_value_l**2, r_value_h**2)
    else:
        return(0,0,0,0,0,0)
```

```jsunicoderegexp
def isBreakOut(candle, backcandles, window):
    if (candle-backcandles-window)<0:
        return 0
    
    sl_lows, interc_lows, sl_highs, interc_highs, r_sq_l, r_sq_h = df.iloc[candle].Channel
    
    prev_idx = candle-1
    prev_high = df.iloc[candle-1].High
    prev_low = df.iloc[candle-1].Low
    prev_close = df.iloc[candle-1].Close
    
    curr_idx = candle
    curr_high = df.iloc[candle].High
    curr_low = df.iloc[candle].Low
    curr_close = df.iloc[candle].Close
    curr_open = df.iloc[candle].Open

    if ( prev_high > (sl_lows*prev_idx + interc_lows) and
        prev_close < (sl_lows*prev_idx + interc_lows) and
        curr_open < (sl_lows*curr_idx + interc_lows) and
        curr_close < (sl_lows*prev_idx + interc_lows)): #and r_sq_l > 0.9
        return 1
    
    elif ( prev_low < (sl_highs*prev_idx + interc_highs) and
        prev_close > (sl_highs*prev_idx + interc_highs) and
        curr_open > (sl_highs*curr_idx + interc_highs) and
        curr_close > (sl_highs*prev_idx + interc_highs)): #and r_sq_h > 0.9
        return 2
    
    else:
        return 0
```
### Detect flag
```jsunicoderegexp
from scipy.stats import linregress

def detect_flag(candle, backcandles, window, plot_flag=False):
    """
    Attention! window should always be greater than the pivot window! to avoid look ahead bias
    """
    localdf = df[candle-backcandles-window:candle-window]  
    highs = localdf[localdf['pivot'] == 2].high.tail(3).values
    idxhighs = localdf[localdf['pivot'] == 2].high.tail(3).index
    lows = localdf[localdf['pivot'] == 1].low.tail(3).values
    idxlows = localdf[localdf['pivot'] == 1].low.tail(3).index

    if len(highs) == 3 and len(lows) == 3:
        order_condition = ( 
            (idxlows[0] < idxhighs[0] 
            < idxlows[1] < idxhighs[1] 
            < idxlows[2] < idxhighs[2]) 
            or 
            (idxhighs[0] < idxlows[0] 
             < idxhighs[1] < idxlows[1] 
             < idxhighs[2] < idxlows[2]) )
        
        slmin, intercmin, rmin, _, _ = linregress(idxlows, lows)
        slmax, intercmax, rmax, _, _ = linregress(idxhighs, highs)

        if (order_condition 
            and (rmax*rmax)>=0.9 
            and (rmin*rmin)>=0.9 
            and slmin>=0.0001 
            and slmax<=-0.0001):
            #and ((abs(slmin)-abs(slmax))/abs(slmax)) < 0.05):

            if plot_flag:
                fig = go.Figure(data=[go.Candlestick(x=localdf.index,
                open=localdf['open'],
                high=localdf['high'],
                low=localdf['low'],
                close=localdf['close'])])

                fig.add_scatter(x=localdf.index, y=localdf['pointpos'], mode="markers",
                marker=dict(size=10, color="MediumPurple"),
                name="pivot")
                fig.add_trace(go.Scatter(x=idxlows, y=slmin*idxlows + intercmin, mode='lines', name='min slope'))
                fig.add_trace(go.Scatter(x=idxhighs, y=slmax*idxhighs + intercmax, mode='lines', name='max slope'))
                fig.update_layout(
                xaxis_rangeslider_visible=False,
                plot_bgcolor='white', # change the background to white
                xaxis=dict(showgrid=True, gridcolor='white'), # change the x-axis grid to white
                yaxis=dict(showgrid=True, gridcolor='white') # change the y-axis grid to white
                )
                fig.show()

            return 1
    
    return 0

```

### Data cleaning

```jsunicoderegexp
data[data["volumne"]]
```

