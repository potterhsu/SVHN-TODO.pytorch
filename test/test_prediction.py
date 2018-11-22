import os
from unittest import TestCase


class TestPrediction(TestCase):

    def test_prediction(self):
        path_to_results_dir = '../results'
        path_to_15_prediction_txt = os.path.join(path_to_results_dir, '15.png-prediction.txt')
        path_to_62_prediction_txt = os.path.join(path_to_results_dir, '62.png-prediction.txt')
        self.assertTrue(os.path.isfile(path_to_15_prediction_txt))
        self.assertTrue(os.path.isfile(path_to_62_prediction_txt))

        with open(path_to_15_prediction_txt, 'r') as fp:
            prediction = fp.readline()
            self.assertEqual(prediction, '15')

        with open(path_to_62_prediction_txt, 'r') as fp:
            prediction = fp.readline()
            self.assertEqual('62', prediction)
