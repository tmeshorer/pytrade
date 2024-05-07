from abc import ABC, abstractmethod
from typing import List

from ib_insync import *

class MarketObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, bars) -> None:
        """
        Receive update from subject.
        """
        pass



class InteractiveBroker:

    def __init__(self):
        self.ib = IB()
        self.listeners = []
        self._observers: List[MarketObserver] = []

    """
        List of subscribers. In real life, the list of subscribers can be stored
        more comprehensively (categorized by event type, etc.).
        """

    def attach(self, observer: MarketObserver) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: MarketObserver) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self,bars) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(bars)

    def connect_to_paper_trading(self):
        self.ib.connect("127.0.0.1",7497,clientId=9)

    def place_sell_limit_order(self,sym:str,qty:float,lmt_price:float):
       contract = Stock(sym)
       contract = self.ib.qualifyContracts(contract)[0]
       ord = LimitOrder(action='SELL',totalQuantity=qty,lmtPrice=lmt_price)
       self.ib.placeOrder(contract,ord)

    def place_buy_limit_order(self, sym: str, qty: float, lmt_price: float):
        contract = Stock(sym)
        contract = self.ib.qualifyContracts(contract)[0]
        ord = LimitOrder(action='BUY', totalQuantity=qty, lmtPrice=lmt_price)
        self.ib.placeOrder(contract, ord)

    def place_sell_limit_order(self, sym: str, qty: float, lmt_price: float):
        contract = Stock(sym)
        contract = self.ib.qualifyContracts(contract)[0]
        ord = LimitOrder(action='SELL', totalQuantity=qty, lmtPrice=lmt_price)
        self.ib.placeOrder(contract, ord)

    def place_buy_market_order(self, sym: str, qty: float, lmt_price: float):
        contract = Stock(sym)
        contract = self.ib.qualifyContracts(contract)[0]
        ord = MarketOrder(action='BUY', totalQuantity=qty, lmtPrice=lmt_price)
        self.ib.placeOrder(contract, ord)

    def place_sell_market_order(self,sym:str,qty:float,stop_price:float):
       contract = Stock(sym)
       contract = self.ib.qualifyContracts(contract)[0]
       ord = MarketOrder(action='SELL',totalQuantity=qty,stopPrice=stop_price)
       self.ib.placeOrder(contract,ord)

    def place_buy_stop_order(self, sym: str, qty: float, stop_price: float):
        contract = Stock(sym)
        contract = self.ib.qualifyContracts(contract)[0]
        ord = StopOrder(action='BUY', totalQuantity=qty, stopPrice=stop_price)
        self.ib.placeOrder(contract, ord)

    def place_stock_combo_order(self,sym,lmt:float,stop:float):
        c = Stock(sym)
        parent = Order(orderId=471,action="BUY",orderType="LMT",totalQuantity=1,lmtPrice=1.0977)

        takeProfit = Order()
        takeProfit.orderId = parent.orderId + 1
        takeProfit = "SELL" if parent.action == "BUY" else "BUY"
        takeProfit.orderType = "LMT"
        takeProfit.lmtPrice = 1.0979
        takeProfit.parentId = parent.orderId
        takeProfit.transmit = False

        stopLoss = Order()
        stopLoss.orderId = parent.orderId + 1
        stopLoss = "SELL" if parent.action == "BUY" else "BUY"
        stopLoss.orderType = "STOP"
        stopLoss.auxPrice = stop
        takeProfit.parentId = parent.orderId
        takeProfit.transmit = False

        ords = [parent,takeProfit,stopLoss]
        for o in ords:
            trade = self.ib.placeOrder(c,o)

    def place_forex_trade(self,currency):
        contract = Forex('EURUSD')
        q_c = self.ib.qualifyContracts(contract)

    def get_historical_stock_data(self,sym:str):
        contract = Stock(sym)
        bars = self.ib.reqHistoricalData(contract,endDateTime='',durationStr='30 D',barSizeSetting='1 hour')
        df = util.df(bars)
        return df

    def get_historical_forex_data(self,sym:str):
        contract = Forex(sym)
        bars = self.ib.reqHistoricalData(contract,endDateTime='',durationStr='30 D',barSizeSetting='1 hour',useRTH=True)
        df = util.df(bars)
        return df

    def listen_real_time_stock_data(self,sym):
        contract = Stock(sym)
        bars = self.ib.reqRealTimeBars(contract,5,"MIDPOINT",False)
        bars.updateEvent += self.onBarUpdate(bars)
        self.ib.run()

    def onBarUpdate(self,bars,hasNewBar):
        self.notify(bars)



