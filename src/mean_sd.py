'''
Sandbox for learning  datapanels and 
Created on Nov 2, 2017

oops:
https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro-deprecate-panel

But maybe we don't need them
@author: djames
'''
import pandas as pd
from pandas_merge import dpp

# some values to work with
vectors = pd.DataFrame({"P1": "enabled",
                    "P2":  ["on", "on", "off", "off"],
                    "P3": ["on", "off", "on", "off"],
                    })

result1 = pd.Series([1, 2, 3, 4])
result2 = pd.Series([2, 2, 5, 4])
result3 = pd.Series([3, 1, 5, 4])
result4 = pd.Series([4, 2, 4, 4])

# build some frames
df1 = vectors.copy()
df1["R1"] = result1
df2 = vectors.copy()
df2["R2"] = result2
df3 = vectors.copy()
df3["R3"] = result3
df4 = vectors.copy()
df4["R4"] = result4

def result_columns(df):
    heads = df.columns.tolist()
    result = [ head for head in heads if 'R' in head]
    return result

# make panel ( oops )

if __name__ == '__main__':
    dpp(vectors)
#     dpp(result1)
#     dpp(result2)
#     dpp(df1)
#     dpp(df2)
    merged = df1.merge(df2).merge(df3).merge(df4)
    dpp(merged)
    merged["mean"] = merged.mean(axis=1)
    merged["SD"] = merged.std(axis=1)
    dpp(merged)
    print(merged.columns, merged.columns.tolist())

    results = merged.loc[:, lambda df:['R1','R2','R3', 'R4']]
    
    dpp (results)
    print(result_columns(merged))
    
    results2 = merged.loc[:, result_columns]
    print(results2)