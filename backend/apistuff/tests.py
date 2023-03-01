from random import choice, random
from django.test import TestCase
from sklearn.naive_bayes import GaussianNB
from .training import get_train_test_split, get_samples, fit_model
from .processor import round_points, bucket_coord_points, get_zeroed_array, fill_zeroed_array, flatten_filled_array


class TestTrain(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.samples = [
            {'processed': [choice([0,1]) for _ in range(100)], 'category': choice(["O","X"])} 
            for _ in range(10)
        ]
        super().setUpClass()

    def test_get_train_test_split(self):
        train_samples, test_samples = get_train_test_split(self.samples)
        self.assertEqual(len(train_samples), 8)
        self.assertEqual(len(test_samples), 2)

    def test_get_samples(self):
        train_samples, test_samples = get_train_test_split(self.samples)
        X, Y, test_x, test_y = get_samples(train_samples, test_samples)
        self.assertIsInstance(X[0], list)
        self.assertIsInstance(Y[0], str)
        self.assertIsInstance(test_x[0], list)
        self.assertIsInstance(test_y[0], str)

    def test_fit_model(self):
        train_samples, test_samples = get_train_test_split(self.samples)
        X, Y, _, _ = get_samples(train_samples, test_samples)
        model = fit_model(X,Y)
        self.assertIsInstance(model, GaussianNB)


class TestSampleProcessor(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.raw_line_data  = [
            [{"x": random() * 100, "y": random() * 100} for _ in range(20)]
            for _ in range(2)
        ]
        super().setUpClass()

    def test_round_points(self): 
        rounded_points = round_points(self.raw_line_data)
        self.assertIsInstance(rounded_points, list)
        self.assertIsInstance(rounded_points[0], list)
        self.assertEqual(len(rounded_points[0]), 2)
        self.assertIsInstance(rounded_points[0][0], int)

    def test_bucket_coord_points(self):
        rounded_points = round_points(self.raw_line_data)
        bucketed_points = bucket_coord_points(rounded_points)
        are_single_digits = all(
            x for y in 
            map(
                lambda c: map(lambda p : p <= 10, c), 
                [list(c) for c in bucketed_points]
            ) 
            for x in y
            )
        self.assertTrue(are_single_digits)

    def test_get_zeroed_array(self):
        flattened = [x for y in get_zeroed_array() for x in y]
        self.assertEqual(len(flattened), 100)

    def test_fill_zeroed_array(self):
        rounded_points = round_points(self.raw_line_data)
        bucketed_points = bucket_coord_points(rounded_points)
        zeroed_array = get_zeroed_array()
        filled_array = fill_zeroed_array(zeroed_array, bucketed_points)
        self.assertIsInstance(filled_array, list)
        self.assertIsInstance(filled_array[0], list)
        self.assertIsInstance(filled_array[0][0], list)
        self.assertIsInstance(filled_array[0][0][0], int)

    def test_flatten_filled_array(self):
        rounded_points = round_points(self.raw_line_data)
        bucketed_points = bucket_coord_points(rounded_points)
        zeroed_array = get_zeroed_array()
        filled_array = fill_zeroed_array(zeroed_array, bucketed_points)
        flattened_filled_array = flatten_filled_array(filled_array)
        self.assertIsInstance(flattened_filled_array, list)
        self.assertIsInstance(flattened_filled_array[0], int)
        self.assertTrue(all(map(lambda x: x in [0,1], flattened_filled_array)))


