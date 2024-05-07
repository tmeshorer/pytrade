## Concept
- Execute Order
- Buy Order / Sell Order
- Order have : Price / Qty / Symbol/Time
- Stock, Bond, Option, Future, Inherit from Financial Instrument.
- Measure of financial risk. 
## Process:
  - Connecting with external system:
    - Financial Information: News , Historical Data
    - Financial Market - Excahgne
  - Pretrade Analysis [ Alpha Model / Risk Model / Cost Model]
    - Alpha Model - Predict future behivor of financal instrument
    - Risk model - Predict risk exeposure
    - Transaction model - predict risk assosicated with cost.
  - Trading Signal [ Protoflio Construction Model]
    - Portofilio - Which financial instrucment and what quantity.
  - Trade Execution [ Execution Model]
    - Trading strategy
    - Venue
    - Order Type
  - Post trade Analysis

### Pretrade Analysis

- News / Financal data about an *Asset*
- Company valuation.
- Forcast assert price based on twitter.
- Trading signal generation.
- Order Execution - Place *Order* in *Exchange*
- Trade Security - Equity, Bond, Currency
- Trading signal component:
  - Select the stock to construct and determine the weight of each stock.
  - *Protfolio* Composition

### Pretrade Analsis

- Fundemnatal Analsis
  - Country Intrest rate, GDP.
  - Current asset price differ from fair value
  - Use ML to predict assert price from ratio.
- Technical Analsysis
  - Identify a new Trend. Enter signal when a trend start, Exist signal when trend end
  - Trend line, support and resistance.
- Quantitive Analsis
  - Treat asset price as random, use stat to describe the randomness.
  - Signal when current asset price differ from asset value - stat arbitrage.

# Trade signal generation
- Signal : Price / Qtr / Stop loss value. 
- Agument with specific values for actual trade.
- Can be replayed in order to simulate perofrmance. 
- Trade signal must provide strategy to close the trade.
- Generate Entry strategy, e.g. start of a trend.
- Exit Strategy - E.g. price above resistance. Use stop loss order.
- Take voltaility into account.

# Trade execution
- Order must be submitted to the trading venue.
- market order to limit order - select order type.
- Determine where to submit the order to.
- 
