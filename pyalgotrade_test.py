# -*-coding=utf-8-*-
__author__ = 'Rocky'
from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma
class MyStrategy(strategy.BacktestingStrategy):

    def __init__(self,feed,instrument):
        strategy.BacktestingStrategy.__init__(self,feed)
        self.__instrument=instrument
        self.__sma=ma.SMA(feed[instrument].getCloseDataSeries(),5)
        #后面是选择多少天作为平均线
    def onBars(self, bars):
        bar=bars[self.__instrument]
        #self.info(bar.getClose())
        self.info("%s %s" %(    bar.getClose(),self.__sma[-1]))

#只是简单地显示
def testcase1():
    feed=yahoofeed.Feed()
    feed.addBarsFromCSV('orcl','orcl-2000.csv')
    myStrategy=MyStrategy(feed,'orcl')
    myStrategy.run()

#进行买卖
class Sell_Case(strategy.BacktestingStrategy):
    def __init__(self,feed,instrument,smaPeriod):
        strategy.BacktestingStrategy.__init__(self,feed,1000)
        self.__position=None
        self.__instrument=instrument
        self.setUseAdjustedValues(True)
        self.__sma=ma.SMA(feed[instrument].getPriceDataSeries(),smaPeriod)

    def onEnterOk(self, position):
        execInfo=position.getEntryOrder().getExecutionInfo()
        self.info("BUY at %f" %execInfo.getPrice())

    def onEnterCanceled(self, position):
        self.__position=None

    def onExitOk(self, position):
        execInfo=position.getExitOrder().getExecutionInfo()
        self.info("SELL at %f" %execInfo.getPrice())
        self.__position=None

    def onExitCanceled(self, position):
        self.__position.exitMarket()

    def onBars(self, bars):
        if self.__sma[-1] is None:
            return

        bar=bars[self.__instrument]
        if  self.__position is None:
            if bar.getPrice()> self.__sma[-1]:
                self.__position=self.enterLong(self.__instrument,10,True)
        elif bar.getPrice() <self.__sma[-1] and not self.__position.exitActive():
            self.__position.exitMarket()



def testcase2():
    feed=yahoofeed.Feed()
    feed.addBarsFromCSV('nvda','nvda-2016.csv')
    myStrategy=Sell_Case(feed,'nvda',15)
    myStrategy.run()
    print "Final portfolio %f" %myStrategy.getBroker().getEquity()

#testcase1()
testcase2()