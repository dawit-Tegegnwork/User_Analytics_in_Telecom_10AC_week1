import unittest
import pandas as pd
from src.eda import top_handsets, handset_manufacturers, top_handsets_for_manufacturer

class TestEDA(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("data/preprocessed_data.csv")

    def test_top_handsets(self):
        self.assertEqual(len(top_handsets(self.df)), 10)

    def test_handset_manufacturers(self):
        self.assertEqual(len(handset_manufacturers(self.df)), 3)

    def test_top_handsets_for_manufacturer(self):
        for manufacturer in handset_manufacturers(self.df).index:
            top_handsets = top_handsets_for_manufacturer(self.df, manufacturer)
            self.assertEqual(len(top_handsets), 5)

if __name__ == '__main__':
    unittest.main()