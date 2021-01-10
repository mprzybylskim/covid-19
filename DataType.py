from enum import Enum


class DataType(Enum):
    CONFIRMED = 1
    DEATHS = 2
    RECOVERED = 3
    ACTIVE = 4

column_titles = {
            DataType.CONFIRMED: 'Confirmed',
            DataType.DEATHS: 'Deaths',
            DataType.ACTIVE: 'Active',
            DataType.RECOVERED: 'Recovered'
        }
plot_titles = {
            DataType.CONFIRMED: 'Potwierdzone przypadki',
            DataType.DEATHS: 'Śmierci',
            DataType.ACTIVE: 'Aktywne przypadki',
            DataType.RECOVERED: 'Ozdrowienia'
        }

axes_titles = {
            DataType.CONFIRMED: 'potwierdzonych przypadków',
            DataType.DEATHS: 'śmierci',
            DataType.ACTIVE: 'aktywnych przypadków',
            DataType.RECOVERED: 'ozdrowień'
        }

country_pl = {
    'Poland': 'Polska',
    'Germany': 'Niemcy',
    'Italy': 'Włochy'
}

operation = {
    'min': 'minimum',
    'max': 'maksimum',
    'mean': 'średnia',
    'median': 'mediana',
}