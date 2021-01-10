import unittest

from CsvHandler import *


class ReadingTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.csv = CsvHandler()

    def test_reading(self):
        data = self.csv.get_data_by_type_and_country_name(DataType.CONFIRMED, 'Poland')
        case1 = data.loc[data['date'] == '2020-05-01']['Confirmed'].values[0]
        case2 = data.loc[data['date'] == '2020-08-01']['Confirmed'].values[0]
        case3 = data.loc[data['date'] == '2020-11-01']['Confirmed'].values[0]
        self.assertEqual(case1, 13105)
        self.assertEqual(case2, 46346)
        self.assertEqual(case3, 379902)

    def test_not_reading(self):
        data = self.csv.get_data_by_type_and_country_name(DataType.CONFIRMED, 'Poland')
        with self.assertRaises(IndexError):
            data.loc[data['date'] == '2020-13-01']['Confirmed'].values[0]

unittest.main()