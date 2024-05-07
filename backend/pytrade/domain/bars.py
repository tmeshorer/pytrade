####################################################################
# Bars
####################################################################
from typing import List

from pytrade.domain.bar import Bar


class Bars:
    def __init__(self,bars):
        self.bars:List[Bar]=bars

    def lows(self)->List[float]:
        result = List[float]()
        for x in self.bars:
            result.append(x.low)
        return result

    def highs(self)->List[float]:
        result = List[float]()
        for x in self.bars:
            result.append(x.high)
        return result

    def volumes(self)->List[float]:
        result = List[float]()
        for x in self.bars:
            result.append(x.volume)
        return result

    def big_black(self):
        return [x for x in self.bars if x.is_big(self.bars) and x.is_black()]

    def big_white(self):
        return [x for x in self.bars if x.is_big(self.bars) and x.is_white()]

    def failed_bear_breakout(self):
        return [x for x in self.bars if x.bear_failed_to_break(self.bars)]

    def failed_bull_breakout(self):
        return [x for x in self.bars if x.bear_failed_to_break(self.bars)]

    def black_bars(self):
        return [x for x in self.bars if x.is_black()]

    def white_bars(self):
        return  [x for x in self.bars if x.is_white()]

    def doji_bars(self):
        return [x for x in self.bars if x.is_white()]


    def distance_to_support(self,price,hlines):
        pass

    def distance_to_major_support(price, float64, hlines):
        return 10

    def distance_to_res(price, hlines):
        return 10.0

    def distance_to_major_res(price, lines):
        return 10.0

    def distance_to_20_EMA(self):
        return 10.0

    def distance_to_50_ma(self):
        return 10.0

    def distance_to_20_MA(self):
        return 10.0


    def avg_white_body(self):
        return 10.0

    def avg_black_body(self):
        pass

    def char_life_cycle(self):
        return 10.0


    def is_higher_high(self,bars, tolrance):
        h1 = self.first_high_pivot_point(bars)
        h2 = self.second_high_pivot_point(bars)
        if h1 != None and h2 != None :
            if (h1.Price - h2.Price) > tolrance:
                return True
        return False


    def is_lower_high(self,candles, tolrance):
        h1 = self.first_high_pivot_point(candles)
        h2 = self.second_high_pivot_point(candles)
        if h1 != None and h2 != None:
            if (h2.Price - h1.Price) > tolrance :
                return True


        return False

    def first_high_pivot_point(self,candles)->Bar:
        pass

    def second_high_pivot_point(self,candles)->Bar:
        pass

    def first_low_pivot_point(self,candles)->Bar:
        pass

    def second_low_pivot_point(self,candles)->Bar:
        pass

    def is_double_top(self,candels:List[Bar], tolrance):
        h1 = self.first_high_pivot_point(candels)
        h2 = self.second_high_pivot_point(candels)
        if h1 != None and h2 != None:
            if (h2.close - h1.Price) < tolrance:
                return True
        return False


    def is_higher_low(self,candles, tolrance):
        h1 = self.first_low_pivot_point(candles)
        h2 = self.second_low_pivot_point(candles)
        if h1 != None and h2 != None:
            if (h1.Price - h2.Price) > tolrance:
                return True
        return False


    def is_lower_low(self,candles, tolrance):
        h1 = self.first_low_pivot_point(candles)
        h2 = self.second_low_pivot_point(candles)
        if h1 != None and h2 != None:
            if (h2.Price - h1.Price) > tolrance:
                return True
        return False



    def is_double_buttom(self,candles, tolrance):
        h1 = self.first_low_pivot_point(candles)
        h2 = self.second_low_pivot_point(candles)
        if h1 != None and h2 != None:
            if (h2.Price - h1.Price) < tolrance:
                return True
        return False


    def is_trading_up(self,candles, tolrance):
        return self.is_higher_low(candles, tolrance) and self.is_higher_high(candles, tolrance)

    def is_trading_low(self,candles, tolrance):
        return self.is_lower_low(candles, tolrance) and self.is_trading_low(candles, tolrance)


