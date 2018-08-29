import pandas as pd
import datetime as dt

# relative dates
today = dt.date.today()
pdt = pd.Timestamp(today.year, today.month, today.day, 18, 0, 0)
for d in [-1, -5, -10, -50, -100]:
    td = pd.Timedelta(days=d)
    print(td, pdt+td)

# date range
for d in pd.date_range('1/1/2018', '1/10/2018'):
    print(d)