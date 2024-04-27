import unittest
import pandas as pd
from src.satisfaction_analysis import (
    compute_engagement_score,
    compute_experience_score,
    compute_satisfaction_score
)

class TestSatisfactionAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5],
            'feature1': [10, 20, 15, 25, 30],
            'feature2': [100, 150, 120, 180, 200],
        })
        self.engagement_clusters = pd.DataFrame({
            'cluster': [0, 1],
            'feature1': [10, 25],
            'feature2': [100, 180]
        })
        self.experience_clusters = pd.DataFrame({
            'cluster': [0, 1],
            'feature1': [15, 30],
            'feature2': [120, 200]
        })

    def test_compute_engagement_score(self):
        # Test the computation of engagement scores
        result = compute_engagement_score(self.data, self.engagement_clusters)
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))

    def test_compute_experience_score(self):
        # Test the computation of experience scores
        result = compute_experience_score(self.data, self.experience_clusters)
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))

    def test_compute_satisfaction_score(self):
        # Test the computation of satisfaction scores
        engagement_scores = compute_engagement_score(self.data, self.engagement_clusters)
        experience_scores = compute_experience_score(self.data, self.experience_clusters)
        result = compute_satisfaction_score(engagement_scores, experience_scores)
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(self.data))

if __name__ == '__main__':
    unittest.main()