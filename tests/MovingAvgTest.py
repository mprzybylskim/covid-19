import unittest

from DataCalculator import *


class MovingAvgTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.csv = CsvHandler()
        self.dc = DataCalculator()

    def test_avg(self):
        data = self.dc.get_centered_moving_avg_by_type_and_country_name(DataType.CONFIRMED, 'Poland', 7, 1, get_mean_by_size_and_window_step)
        country = data[0]
        value = country.loc[country['date'] == '2020-11-01']['mean'].values[0]
        self.assertEqual(value, 378933.14285714284)

    def test_zero(self):
        data = self.dc.get_centered_moving_avg_by_type_and_country_name(DataType.CONFIRMED, 'Poland', 7, 1, get_mean_by_size_and_window_step)
        country = data[0]
        value = country.loc[country['date'] == '2020-02-03']['mean'].values[0]
        self.assertEqual(value, 0.0)

    def test_out_of_range(self):
        data = self.dc.get_centered_moving_avg_by_type_and_country_name(DataType.CONFIRMED, 'Poland', 7, 1, get_mean_by_size_and_window_step)
        country = data[0]
        with self.assertRaises(IndexError):
            country.loc[country['date'] == '3020-03-03']['mean'].values[0]


unittest.main()