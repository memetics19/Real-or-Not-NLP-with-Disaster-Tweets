"""Test for contradiction of the actual test """

import pandas as pd 
import unittest


class DataCleaning(unittest.TestCase):
    """ test for the contradiction of the data cleaning"""

    def setUp(self):
        """setup the test model"""
        data = pd.read_csv('data/train.csv')


        return df
    
    def drop_missing_values_test(self,data):
        """" test for the missing values """
        missing_columns = df.is_null()

        self.assertAlmostEquals(self.data)


if __name__ == '__main__':
    unittest.main()