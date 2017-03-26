import pandas as pd
import numpy as np


# range_obj = range(10, 20)
# print(range_obj)
ser_obj = pd.Series(range(10, 20))
# print(type(ser_obj))
# print(ser_obj.index)
# print(ser_obj.values)
# print(ser_obj.head(4))

dict_date = {'a': 1.,
             'b': pd.Timestamp('20170304'),
             'c': pd.Series(1, index=list(range(4)), dtype='float32'),
             'd': np.array([3] * 4, dtype='int32'),
             'e': pd.Categorical(["Python", "Java", "C++", "c#"]),
             'f': 'ChinaHadoop'
             }
obj_dict = pd.DataFrame(dict_date)
# print(pd.DataFrame(dict_date).head())
# print(obj_dict['a'])

obj_dict['g'] = obj_dict['d'] + 4
# print(obj_dict.head())

# del(obj_dict['g'])
# print(obj_dict.head())

# obj_dict.index[0] = 2
# print(obj_dict.index)

ser_obj = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
# print(ser_obj.head())
# print(ser_obj['a':'b'])
# print(ser_obj)
# print(ser_obj.iloc[0:1])

s1 = pd.Series(range(10, 20), index=range(10))
s2 = pd.Series(range(20, 25), index=range(5))

# print(s1)
# print(s2+s1)
# print(s1.add(s2, fill_value=-1))

# df = pd.DataFrame(np.random.randn(5, 4), columns=['a', 'b', 'c', 'd'])
# print(df)
# print(df.abs())
# f = lambda x: x.max()
# print(df.apply(f, axis=1))
# print(df.describe())
df = pd.Series(np.random.randn(12), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd'],
                                               [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]])
# print(type(df1.index))
print(df.swaplevel().sortlevel())
# print(df1.index)
print(df.swaplevel())




