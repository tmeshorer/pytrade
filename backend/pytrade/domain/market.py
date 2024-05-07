# This package handle order execution.

class MarketData:
    def __init__(self,name):
        self.name = name

    def connect(self):
        pass

    def close(self):
        pass



class Instrument:
    def __init__(self,sym,exc,charts):
        self.sym = sym
        self.exchange = exc
        self.charts = charts

    def register(self):
        """register with the exchange"""

    def on_new_bar(self):
        """update the charts and look for a signal"""

class Exchange:
    def __init__(self,name):
        self.instruments = {}


    def add_instrument(self,i:Instrument):
        self.instruments[i.sym] = i

    def execute(self,order):
        """execute an order in the exchange """
        pass

    def on_new_bar(self,Bar):
        """on new bar, update the instruments"""


class Order:
    def __init__(self,sym,order_type,prot):
        pass

    def place(self):
      """place the order"""


    def cancel(self):
        """place the order"""

    def done(self):
        """place the order"""

