import zipline as zp

class BuyApple(zp.TradingAlgorithm):
    trace = False

    def __init__(self, trace=False):
        BuyApple.trace = trace
        super(BuyApple, self).__init__()

    def initialize(context):
        if BuyApple.trace: print("---> initialize")
        if BuyApple.trace: print(context)
        if BuyApple.trace: print("<--- initialize")

    def handle_data(self, context):
        if BuyApple.trace: print("---> handle_data")
        if BuyApple.trace: print(context)
        self.order("AAPL", 1)
        if BuyApple.trace: print("<-- handle_data")

import zipline.utils.factory as zpf
data = zpf.load_from_yahoo(stocks=['AAPL'],
                          indexes={},
                          start=datetime(1990, 1, 1),
                          end=datetime(2014, 1, 1),
                          adjusted=False)
data.plot(figsize=(12,8));

result = BuyApple().run(data['2000-01-03':'2000-01-07'])
result.iloc[0].orders
result.iloc[1].orders
result[['starting_cash', 'ending_cash', 'ending_value']]
pvalue = result.ending_cash + result.ending_value
pvalue
result.portfolio_value

result_for_2000 = BuyApple().run(data['2000'])
result_for_2000.portfolio_value.plot(figsize=(12,8));
result = BuyApple().run(data['2000':'2004']).portfolio_value