from pyalgotrade import strategy 
from pyalgotrade.barfeed import quandlfees

class MyStrategy(strategy.BacktestingStrategy):
    
      def __init__(self,feed,instrument):
           super(MyStrategy, self).__init__(feed)
           self.__instrument=instrument

      def onBars(self, bars):
           bars=bars[self.__instrument]
           self.info(bar.getclose())


           

feed=quandlfeed.Feed()
feed.addBarsFromCSV("orcl","WIKI-ORCL-2000-quandl.csv")

myStrategy=MyStrategy(feed,"orcl")
myStrategy.run()

