import numpy as np

# Загрузить данные в массив numpy
data = np.array([[1, 395.62],
                 [2, 394.48],
                 [3, 395.73],
                 [4, 396.52],
                 [5, 396.57],
                 [6, 396.63],
                 [7, 396.64],
                 [8, 395.57],
                 [9, 395.84],
                 [10, 395.96],
                 [11, 395.25],
                 [12, 394.9],
                 [13, 394.84],
                 [14, 394.66],
                 [15, 394.41],
                 [16, 393.46],
                 [17, 393.51],
                 [18, 393.3],
                 [19, 393.11],
                 [20, 392.91]])

# Разделить данные на две переменные
days = data[:, 0]
currency_rates = data[:, 1]

# Вычислить коэффициенты линейной регрессии с помощью метода slope-intercept
x_mean = np.mean(days)
y_mean = np.mean(currency_rates)

beta_1 = np.sum((days - x_mean) * (currency_rates - y_mean)) / np.sum((days - x_mean)**2)
beta_0 = y_mean - beta_1 * x_mean

# Предположить значение курса валют на 21-ой день
predict_day = 21
predict_currency_rate = beta_0 + beta_1 * predict_day

print('Predicted currency rate for day 21:', predict_currency_rate)

