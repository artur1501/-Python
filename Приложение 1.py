import pandas as pd

data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]}

df = pd.DataFrame(data)

corr = df['x'].corr(df['y'])
print(corr)
