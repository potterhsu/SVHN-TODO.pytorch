import os
from unittest import TestCase


class TestAccuracy(TestCase):

    def test_accuracy(self):
        path_to_results_dir = '../results'
        path_to_accuracy_txt = os.path.join(path_to_results_dir, 'accuracy.txt')
        self.assertTrue(os.path.isfile(path_to_accuracy_txt))

        with open(path_to_accuracy_txt, 'r') as fp:
            accuracy = fp.readline()

        accuracy = float(accuracy)
        self.assertGreaterEqual(accuracy, 0.9)
