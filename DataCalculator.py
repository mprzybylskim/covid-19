from CsvHandler import CsvHandler
from DataType import DataType


def process_data_for_centered_moving_average_plot(data, window_size: int):
    return data.iloc[0, 1:].rolling(window=window_size).mean()


def clean_data_and_apply_step(data, window_step: int):
    return data.dropna(inplace=False)[::window_step]


def get_mean_by_size_and_window_step(data, window_size: int, window_step: int):
    data = data.copy()
    data["mean"] = data.iloc[:, -1].rolling(window=window_size, center=True).mean()
    return clean_data_and_apply_step(data, window_step)


def get_median_by_size_and_window_step(data, window_size: int, window_step: int):
    data = data.copy()
    data["median"] = data.iloc[:, -1].rolling(window=window_size, center=True).median()
    return clean_data_and_apply_step(data, window_step)


def get_min_by_size_and_window_step(data, window_size: int, window_step: int):
    data = data.copy()
    data["min"] = data.iloc[:, -1].rolling(window=window_size, center=True).min()
    return clean_data_and_apply_step(data, window_step)


def get_max_by_size_and_window_step(data, window_size: int, window_step: int):
    data = data.copy()
    data["max"] = data.iloc[:, -1].rolling(window=window_size, center=True).max()
    return clean_data_and_apply_step(data, window_step)

class DataCalculator:
    fetcher = CsvHandler()

    def get_data_by_type_and_country_name(self, data_type: DataType, country_names):
        by_date = []
        if type(country_names) == str:
            country_names = [country_names]

        for x in range(0, len(country_names)):
            by_date.append(
                self.fetcher.get_data_by_type_and_country_name(
                    data_type, country_names[x]
                )
            )
        return by_date

    def get_centered_moving_avg_by_type_and_country_name(
        self,
        data_type: DataType,
        country_names,
        window_size: int,
        window_step: int,
        callback,
    ):
        by_date = []
        if type(country_names) == str:
            country_names = [country_names]

        for x in range(0, len(country_names)):
            by_date.append(
                callback(
                    self.fetcher.get_data_by_type_and_country_name(
                        data_type, country_names[x]
                    ),
                    window_size,
                    window_step,
                )
            )
        return by_date