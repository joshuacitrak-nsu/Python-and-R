import pandas as pd
import unittest

# Load the mtcars data set
df_mt_cars = pd.read_csv('https://bit.ly/get-mtcars-data')
df_mt_cars = (df_mt_cars[(df_mt_cars['am'] == 1) & (df_mt_cars['cyl'] == 6)]
                .drop('Unnamed: 0', axis = 1)
                .reset_index(drop = True))

class TestMTCarsDataFrame(unittest.TestCase):

    def test_has_correct_number_of_rows(self):
        self.assertEqual(len(df_mt_cars), 3)

    def test_has_correct_columns(self):
        expected_cols = ["mpg", "cyl", "disp", "hp", "drat", "wt", \
                        "qsec", "vs", "am", "gear", "carb"]
        self.assertListEqual(list(df_mt_cars.columns), expected_cols)

    def test_is_filtered_correctly(self):
        expected_mpg = [21.0, 21.0, 19.7]
        expected_cyl = [6, 6, 6]
        expected_hp = [110, 110, 175]
        expected_wt = [2.620, 2.875, 2.770]

        (self.assertTrue(df_mt_cars[['mpg', 'cyl', 'hp', 'wt']]
            .equals(pd.DataFrame({
                'mpg': expected_mpg, 
                'cyl': expected_cyl, 
                'hp': expected_hp, 
                'wt': expected_wt}))))

if __name__ == '__main__':
    unittest.main()
