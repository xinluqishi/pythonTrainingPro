import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
# %matplotlib inline


df_obj = pd.DataFrame(np.random.randn(1000, 1),
                      index=pd.date_range('20170101', periods=1000),
                      columns=['data'])
df_obj['data'] = df_obj['data'].cumsum()
print(df_obj)



