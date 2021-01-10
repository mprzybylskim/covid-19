import locale

import pandas as pd

from DataType import DataType

urls = {
    DataType.CONFIRMED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    DataType.DEATHS: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    DataType.RECOVERED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
}

column_titles = {
    DataType.CONFIRMED: "Confirmed",
    DataType.DEATHS: "Deaths",
    DataType.RECOVERED: "Recovered",
    DataType.ACTIVE: "Active"
}


def read_url(data_type: DataType):

    data = pd.read_csv(urls[data_type])
    data.drop(['Lat', 'Long', 'Province/State'], axis='columns', inplace=True)
    data = data.groupby('Country/Region', as_index=False).sum()
    return data


def save(results: pd.DataFrame, file_name: str):
    results.to_csv(file_name, index=False, sep='\t')


class CsvHandler:

    def __init__(self) -> None:
        self.conf_cases = self.build_table(DataType.CONFIRMED)
        self.deaths = self.build_table(DataType.DEATHS)
        self.recovered = self.build_table(DataType.RECOVERED)
        self.active_cases = self.calc_active_cases()

    def build_table(self, data_type: DataType):
        raw_table = read_url(data_type)
        table = raw_table.melt(
            id_vars=['Country/Region'],
            value_vars=raw_table.columns[4:],
            var_name='date',
            value_name=column_titles[data_type]
        )
        locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
        table['date'] = pd.to_datetime(table['date'])
        return table

    def calc_active_cases(self):
        act_cases = self.conf_cases.copy()
        act_cases['Confirmed'] = act_cases['Confirmed'] - self.deaths['Deaths'] - self.recovered['Recovered']
        act_cases.columns = ['Country/Region', 'date', column_titles[DataType.ACTIVE]]
        return act_cases

    def get_conf_cases(self):
        return self.conf_cases

    def get_deaths(self):
        return self.deaths

    def get_recovered(self):
        return self.recovered

    def get_active_cases(self):
        return self.active_cases

    def get_data_by_type_and_country_name_and_date(self, data_type: DataType, country_name: str, start_date: str,
                                                   end_date: str):
        data = self.get_data_by_type_and_country_name(data_type, country_name)
        mask = (data['date'] >= start_date) & (data['date'] <= end_date)
        return data.loc[mask]

    def get_data_by_type_and_country_name(self, data_type: DataType, country_name: str):
        data = self.get_table(data_type)
        country_list = data['Country/Region'].to_numpy()
        corrected_name = ''
        for country in country_list:
            if country_name in country:
                corrected_name = country
                break
        data['date'] = data['date'].apply(lambda x: str(x)[:10])
        return data.loc[data['Country/Region'] == corrected_name]

    def get_table(self, data_type: DataType):
        tables = {
            DataType.CONFIRMED: self.get_conf_cases(),
            DataType.DEATHS: self.get_deaths(),
            DataType.RECOVERED: self.get_recovered(),
            DataType.ACTIVE: self.get_active_cases()
        }
        return tables.get(data_type)