"""Unit testing for functions in fpho_setup
"""
import fpho_setup
import unittest
import random
import sys
import pandas as pd


class TestFphoSetup(unittest.TestCase):

    def test_import_fpho_data(self):
        df = fpho_setup.import_fpho_data(animal_ID='vole1',
                                         exp_date='2020-09-01',
                                         exp_desc="testing",
                                         input_filename='TestData/1FiberTesting.csv',
                                         output_filename='testing_unit.csv')

        test_green_iso = [1640.48859543818, 1640.90076030412,
                          1640.33053221289]
        self.assertEqual(df['f1GreenIso'].values[0], test_green_iso)

        test_green_green = [1511.23969587835, 1511.07482993197]
        self.assertEqual(df['f1GreenGreen'].values[0], test_green_green)
        
        test_red_iso = [1536.2730469085, 1536.54499614098,
                        1536.02771631936]
        self.assertEqual(df['f1RedIso'].values[0], test_red_iso)

    def test_import_fpho_data_errors(self):
        with self.assertRaises(SystemExit) as cm:
            fpho_setup.import_fpho_data(animal_ID='vole1',
                                        exp_date='2020-09-01',
                                        exp_desc="testing",
                                        input_filename='TestData/1Fighdk.csv',
                                        output_filename='testing_unit.csv')
        self.assertEqual(cm.exception.code, 1)

    def test_fit_exp(self):
        fit = fpho_setup.fit_exp([0, 0, 0, 0, 0], 1, 1, 1, 1)
        self.assertEqual(2.0, fit[0])
        self.assertEqual(2.0, fit[3])
        
        fit = fpho_setup.fit_exp([1, 5, 8, 10], 1, -1, 1, -1)
        self.assertEqual(0.7357588823428847, fit[0])
        self.assertEqual(9.079985952496971e-05, fit[3])

#    def test_raw_signal_trace_errors(self):
#        with self.assertRaises(SystemExit) as cm:
#            fpho_setup.raw_signal_trace(fpho_dataframe='bad_df.csv',
#                                        output_filename='testing_unit.png',
#                                        data_row_index=0)
#        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
