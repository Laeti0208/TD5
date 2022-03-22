import pandas as pd 
d_buy={'Buy' : pd.Series([(10,10),(5,10),(2,11)])}

df_buy=pd.DataFrame(d_buy)
print(df_buy)

d_sell={'Sell' : pd.Series([(120,12),(1,10),(10,10)])}

df_sell=pd.DataFrame(d_sell)
print(df_sell)
