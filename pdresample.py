import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

date_rng = pd.date_range('20170303', periods=100, freq='D')
# print(date_rng)

ser_obj = pd.Series(range(len(date_rng)), index=date_rng)
# print(range(len(date_rng)))
# print(ser_obj.head(10))

date_sum_sample = ser_obj.resample('5D').ohlc()
# print(date_sum_sample)

# print(ser_obj.groupby(lambda x: x.weekday).sum())

"""
df = pd.DataFrame(np.random.randn(5, 3),
                  index=pd.date_range('20170101', periods=5, freq='W-MON'),
                  columns=['S1', 'S2', 'S3'])
print(df.resample('D').asfreq())
"""

df = pd.DataFrame(np.random.randn(1000),
                  index=pd.date_range('20170101', periods=1000))
r_obj = df.rolling(window=5)
# print(df.head(10))
# print(r_obj.mean().head(10))

plt.figure(figsize=(15, 5))

df.plot(style='r--')
df.rolling(window=10).mean().plot(style='b')

