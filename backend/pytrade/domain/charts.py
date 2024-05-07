from typing import List

from pytrade.domain.bar import Bar


class Chart:
    def __init__(self,sym,freq):
        self.sym = sym
        self.freq = freq
        self.bars = []

    def add(self,b:Bar):
        self.bars.append(b)

    def detect_buy_signal(self):
       # Ask the chart to
       # look at itself and detrime buy/sell signal
       pass

    def detect_sell_signal(self):
        pass