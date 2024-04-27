import unittest
import pandas as pd
from src.experience_analysis import (
    aggregate_experience_metrics,
    compute_top_values,
    cluster_users_by_experience,
)

class TestExperienceAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'msisdn': [1, 2, 3, 4, 5],
            'tcp_retransmission': [10, 20, 15, 25, 30],
            'rtt': [100, 150, 120, 180, 200],
            'throughput': [1000, 2000, 1500, 2500, 3000],
            'handset_type': ['A', 'B', 'A', 'C', 'B']
        })

    def test_aggregate_experience_metrics(self):
        # Test the aggregation of experience metrics
        expected_result = pd.DataFrame({
            'msisdn': [1, 2, 3, 4, 5],
            'avg_tcp_retransmission': [10, 20, 15, 25, 30],
            'avg_rtt': [100, 150, 120, 180, 200],
            'avg_throughput': [1000, 2000, 1500, 2500, 3000],
            'handset_type': ['A', 'B', 'A', 'C', 'B']
        })
        result = aggregate_experience_metrics(self.data)
        self.assertTrue(result.equals(expected_result))

    def test_compute_top_values(self):
        # Test the computation of top, bottom, and most frequent values
        result = compute_top_values(self.data)
        self.assertIsInstance(result, dict)
        self.assertIn('top_tcp', result)
        self.assertIn('bottom_tcp', result)
        self.assertIn('most_frequent_tcp', result)
        self.assertIn('top_rtt', result)
        self.assertIn('bottom_rtt', result)
        self.assertIn('most_frequent_rtt', result)
        self.assertIn('top_throughput', result)
        self.assertIn('bottom_throughput', result)
        self.assertIn('most_frequent_throughput', result)

    def test_cluster_users_by_experience(self):
        # Test the clustering of users by experience
        result =