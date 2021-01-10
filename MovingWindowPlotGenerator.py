from DataCalculator import *
import matplotlib.pyplot as plt
from DataType import *


class MovingWindowPlotGenerator:

    def __init__(self) -> None:
        super().__init__()
        self.calc = DataCalculator()

    def build_title(self, data_type: DataType, window_size: int, oper):
        day = ' dni'
        if window_size == 1:
            day = ' dzień'
        return plot_titles[data_type] + ' (' + operation[oper] + '), ' + str(window_size) + day

    def build_plot(self, data_type: DataType, countries, window_size, callback, log, oper):
        data = self.calc.get_centered_moving_avg_by_type_and_country_name(data_type, countries, window_size, 1,
                                                                          callback)
        counter = ax = 0
        for single_data in data:
            title = self.build_title(data_type, window_size, oper)
            if counter == 0:
                ax = single_data.plot(x='date', y=[oper], label=[
                    country_pl[single_data.loc[single_data.index[0], 'Country/Region']]])
            else:
                single_data.plot(x='date', y=[oper], ax=ax, label=[
                    country_pl[single_data.loc[single_data.index[0], 'Country/Region']]])
            counter += 1

        if (log == True):
            ax.set_yscale('log')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title(title, y=1.08)
        plt.ylabel('liczba ' + axes_titles[data_type])
        plt.xlabel('Data')
        plt.xticks(rotation=90)
        plt.savefig(title + '.jpg', dpi=600, bbox_inches='tight')
        plt.close()