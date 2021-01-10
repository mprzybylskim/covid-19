from cmath import sqrt
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

from CsvHandler import CsvHandler
from DataType import *


class PredictionGenerator:
    fetcher = CsvHandler()

    def predict_data(self, train, test, p, d, q, country, title, rmses):
        model = ARIMA(train, order=(p, d, q))
        fitted = model.fit()
        fc = fitted.forecast(len(test), alpha=0.05)

        datelist_train = pd.date_range(datetime(2020, 1, 22, 0, 0), periods=len(train)).tolist()
        datelist_test = pd.date_range(datetime(2020, 1, 22, 0, 0) + timedelta(days=len(train)),
                                      periods=len(test)).tolist()

        train_s = pd.Series(train, index=datelist_train)
        test_s = pd.Series(test, index=datelist_test)
        fc_series = pd.Series(fc, index=datelist_test)

        plt.plot(train_s, label='zbiór treningowy')
        plt.plot(test_s, label='przebieg referencyjny')
        plt.plot(fc_series, label='przebieg prognozowany')

        fig_title = '{} - ARIMA ({}, {}, {})'.format(country_pl[country], p, d, q)
        plt.title(fig_title)

        plt.ylabel('liczba ' + title.lower())
        plt.xlabel('Data')
        plt.legend(loc='upper left', fontsize=8)

        plt.savefig(fig_title + '.jpg', dpi=600,
                    bbox_inches='tight')
        plt.close()

        mse = mean_squared_error(test, fc)
        rmse = sqrt(mse)
        rmses.append(('{}, {}, {}'.format(p, d, q), rmse))
        return rmse