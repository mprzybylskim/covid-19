from CsvHandler import CsvHandler
from DataType import *
from PredictionGenerator import PredictionGenerator

import matplotlib.pyplot as plt
import seaborn as sns;

class ExperimentPlotGenerator:
    pg = PredictionGenerator()

    def plot_heatmap(self, data, hm_rows: int, hm_columns: int, data_type: DataType):
        rmses = []
        notP_whenP1 = notP_whenP2 = notP_whenP3 = notP_whenP4 = notP_whenP5 = [[0 for i in range(hm_columns)] for j in
                                                                               range(hm_columns)]
        notD_whenD0 = notD_whenD1 = notD_whenD2 = [[0 for i in range(hm_columns)] for j in range(hm_rows - 1)]
        notQ_whenQ0 = notQ_whenQ1 = notQ_whenQ2 = [[0 for i in range(hm_columns)] for j in range(hm_rows - 1)]



        country = data['Country/Region'].values[0]

        for p in range(1, hm_rows):
            for d in range(hm_columns):
                for q in range(hm_columns):
                    X = data.rename(columns={column_titles[data_type]: 'value'})
                    size = int(len(X) * 0.75)
                    train, test = X[0:size], X[size:len(X)]
                    pred = self.pg.predict_data(train.value.values, test.value.values, p, d, q, country, str(axes_titles[data_type]), rmses)
                    result = int(pred.real)

                    if p == 1:
                        notP_whenP1[d][q] = result
                    if p == 2:
                        notP_whenP2[d][q] = result
                    if p == 3:
                        notP_whenP3[d][q] = result
                    if p == 4:
                        notP_whenP4[d][q] = result
                    if p == 5:
                        notP_whenP5[d][q] = result
                    if d == 0:
                        notD_whenD0[p - 1][q] = result
                    if d == 1:
                        notD_whenD1[p - 1][q] = result
                    if d == 2:
                        notD_whenD2[p - 1][q] = result
                    if q == 0:
                        notQ_whenQ0[p - 1][d] = result
                    if q == 1:
                        notQ_whenQ1[p - 1][d] = result
                    if q == 2:
                        notQ_whenQ2[p - 1][d] = result

        self.plot_single_heatmap(notP_whenP1,
                                 ('{} - {} (ARIMA) - RMSE dla (D, Q), P={}'.format(plot_titles[data_type], country_pl[country], 1)),
                                 'parametr Q', 'parametr D')  # P=1
        self.plot_single_heatmap(notP_whenP2,
                                 ('{} - {} (ARIMA) - RMSE dla (D, Q), P={}'.format(plot_titles[data_type], country_pl[country], 2)),
                                 'parametr Q', 'parametr D')  # P=2
        self.plot_single_heatmap(notP_whenP3,
                                 ('{} - {} (ARIMA) - RMSE dla (D, Q), P={}'.format(plot_titles[data_type], country_pl[country], 3)),
                                 'parametr Q', 'parametr D')  # P=3
        self.plot_single_heatmap(notP_whenP4,
                                 ('{} - {} (ARIMA) - RMSE dla (D, Q), P={}'.format(plot_titles[data_type], country_pl[country], 4)),
                                 'parametr Q', 'parametr D')  # P=4
        self.plot_single_heatmap(notP_whenP5,
                                 ('{} - {} (ARIMA) - RMSE dla (D, Q), P={}'.format(plot_titles[data_type], country_pl[country], 5)),
                                 'parametr Q', 'parametr D')  # P=5
        self.plot_single_heatmap(notD_whenD0,
                                 ('{} - {} (ARIMA) - RMSE dla (P, Q), D={}'.format(plot_titles[data_type], country_pl[country], 0)),
                                 'parametr Q', 'parametr P')  # D=0
        self.plot_single_heatmap(notD_whenD1,
                                 ('{} - {} (ARIMA) - RMSE dla (P, Q), D={}'.format(plot_titles[data_type], country_pl[country], 1)),
                                 'parametr Q', 'parametr P')  # D=1
        self.plot_single_heatmap(notD_whenD2,
                                 ('{} - {} (ARIMA) - RMSE dla (P, Q), D={}'.format(plot_titles[data_type], country_pl[country], 2)),
                                 'parametr Q', 'parametr P')  # D=2
        self.plot_single_heatmap(notQ_whenQ0,
                                 ('{} - {} (ARIMA) - RMSE dla (P, D), Q={}'.format(plot_titles[data_type], country_pl[country], 0)),
                                 'parametr D', 'parametr P')  # Q=0
        self.plot_single_heatmap(notQ_whenQ1,
                                 ('{} - {} (ARIMA) - RMSE dla (P, D), Q={}'.format(plot_titles[data_type], country_pl[country], 1)),
                                 'parametr D', 'parametr P')  # Q=1
        self.plot_single_heatmap(notQ_whenQ2,
                                 ('{} - {} (ARIMA) - RMSE dla (P, D), Q={}'.format(plot_titles[data_type], country_pl[country], 2)),
                                 'parametr D', 'parametr P')  # Q=2

    def plot_single_heatmap(self, data, title, labelx, labely):
        ax = sns.heatmap(data, annot=True, fmt=".1e", cmap=sns.cm.rocket)
        ax.invert_yaxis()
        plt.title(title)
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.savefig(
            'rmse/' + title + '.jpg',
            dpi=600,
            bbox_inches='tight')
        plt.close()

    def plot_bar_graph(self, countries, tr_size, p, d, q, data_type: DataType):
        csv = CsvHandler()
        final = []
        a = b = 0
        for country in countries:
            result = []
            for tr in tr_size:
                series = csv.get_data_by_type_and_country_name(data_type, country).iloc[:, 1:]
                X = series.rename(columns={column_titles[data_type]: 'value'})
                size = int(len(X) * tr)
                train, test = X[0:size], X[size:len(X)]

                pred = self.pg.predict_data(train.value.values, test.value.values, p, d, q, country,
                                            str(axes_titles[data_type]), [])
                pred_real = int(pred.real)
                result.append(pred_real)
            final.append(result)

        fig = plt.figure()
        ax = fig.add_axes([1, 1, 1, 1])

        for country in countries:
            ax.bar([a, a + 2.5, a + 5.0], final[b], width=0.25, label=country_pl[country])
            a = a + 0.3
            b = b + 1
        title = "{} - ARIMA ({}, {}, {}) - RMSE dla różnych rozmiarów zbiorów".format(plot_titles[data_type], p, d, q)
        plt.title(title, y=1.08)
        plt.xlabel('Rozmiar zbioru treningowego')
        plt.ylabel('RMSE')
        plt.legend()
        i = ((len(countries) - 1) * 0.3) / 2
        plt.xticks([0 + i, 2.5 + i, 5 + i], ['{}%'.format(int(tr_size[0]*100)), '{}%'.format(int(tr_size[1]*100)), '{}%'.format(int(tr_size[2]*100))])

        plt.savefig(
            'rmse2/' + title + '.jpg',
            dpi=300,
            bbox_inches='tight')
        plt.close()