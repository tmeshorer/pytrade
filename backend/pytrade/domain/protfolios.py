# This package manage protfolios

class Protfolio:
    def __init__(self):
        self.positions = {} # holds the portfolio positions
        self.cash   = 0


    def short(self):
        '''Total amount of positions in short'''
        pass

    def long(self):
        '''Total amount of positions in long'''
        pass

    def deposit(self,amount):
        """add cash"""
        self.cash += amount


    def profit(self):
        """compute current profilt for the portfolio"""

    def optimize(self):
        """optimize the porfolio, suggest another portfolio with the same risk level"""

    def add_position(self,position):
        """add a position to the porfolio"""

    def close_position(self,position):
        """remove a position from the portoflio"""
