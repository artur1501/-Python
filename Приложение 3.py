import statsmodels.api as sm
import pandas as pd

data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]}

df = pd.DataFrame(data)

X = df['x']
y = df['y']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())
