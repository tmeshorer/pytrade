from pydantic import BaseModel, Field


class Bar(BaseModel):
    sym: str = Field(examples=["META"])
    open:float = Field()

    def __init__(self,sym,high,low,open,close,volume,adj_close):
        self.sym = sym
        self.open = open
        self.close = close
        self.high = high
        self.low  = low
        self.volume = volume
        self.adj_close = adj_close
        self.pivot_point = None

    def height(self):
        return self.high - self.low

    def body(self):
        return abs(self.close - self.open)

    def upper_shadow(self):
        body_high = max(self.open,self.close)
        return self.high - body_high

    def lower_shadow(self):
        body_low = min(self.open, self.close)
        return body_low - self.low

    def upper_shadow_precent(self):
        return self.upper_shadow() * 100 / self.height()

    def body_precent(self):
        return self.body() * 100 / self.height()

    def lower_shadow_precent(self):
        return self.lower_shadow() * 100 / self.height()

    def is_big(self,bars:[]):
        heights = []
        for v in bars:
            heights.append(v.height())

        mean_height = (heights)
        return self.height() > 2*mean_height

    def bull_full_control(self,bars):
        return self.is_white() and self.body_precent() > 90 and self.is_big(bars)

    def bear_full_control(self,bars):
        return self.is_black() and self.body_precent() > 90 and self.is_big(bars)

    def bear_failed_to_break(self,bars):
        return self.lower_shadow_precent() > 40

    def bull_failed_to_break(self,bars):
        return self.upper_shadow_precent() > 40

    def balanced(self):
        shadow_ratio = self.upper_shadow_precent() / self.lower_shadow_precent()
        return shadow_ratio < 1.2 and shadow_ratio > 0.8 and self.body_precent() < 20

    def bull_partial_control(self):
        return self.is_white() and self.upper_shadow_precent() < 10 and self.body_precent() > 30

    def bear_partial_control(self):
        return self.is_black() and self.lower_shadow_precent() < 10 and self.body_precent() > 30
    def is_white(self):
        return self.close > self.open
    def is_black(self):
        return not self.is_black()

    def is_doji(self):
        return self.body_precent() < 5

    def is_pivot_high(self):
        return self.pivot_point != None and self.pivot_point.support

    def is_pivot_low(self):
        return self.pivot_point != None and self.pivot_point.support

    def is_pivot(self):
        return self.is_pivot_high() or self.is_pivot_low()
