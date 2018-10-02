import sys
import os
import datetime as dt
import numpy as np
import pandas as pd
# from pandas_datareader import pdr, wb
# import scipy as sp

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 82)
pd.set_option('precision', 3)
pd.set_option('display.width', 5000)
pd.set_option("display.max_colwidth", 120)

from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
# % matplotlib inline
import seaborn as sns
sns.set(context='paper',
    style='darkgrid',
    rc={'figure.facecolor':'white'},
    font_scale=1.2)