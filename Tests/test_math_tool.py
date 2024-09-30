"""
Unit tests for the MathTool class.
"""

import unittest
from Object.math_tool import MathTool

class TestMathTool(unittest.TestCase):
    """
    Test cases for the MathTool class.
    """
    def setUp(self):
        """
        Method executed before each test.
        """

    def test_calculate_one_way_distance_correct_output(self):
        """
        Test that calculate_one_way_distance produces the expected output for specific data.
        """
        coords1 = [[0, 0], [1, 1]]
        coords2 = [[1, 0], [0, 1]]
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_one_way_distance(coords1, coords2, image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_calculate_one_way_distance_edge_cases(self):
        """
        Test edge cases for calculate_one_way_distance.
        """
        # Identical points
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_one_way_distance(coords1, coords2, image1, image2)
        self.assertEqual(result, expected_output)

    def test_hausdorff_distance_correct_output(self):
        """
        Test that hausdorff_distance produces the expected output for specific data.
        """
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1  # Maximum distance between non-matching points
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_hausdorff_distance_edge_cases(self):
        """
        Test edge cases for hausdorff_distance.
        """
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        expected_output = float('inf')
        result = MathTool.hausdorff_distance(image1, image2)

        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2)

        self.assertEqual(result, expected_output)

    def test_calculate_sum_of_distances_correct_output(self):
        """
        Test that calculate_sum_of_distances produces the expected output for specific data.
        """
        coords1 = [[0, 0], [1, 1]]
        coords2 = [[1, 0], [0, 1]]
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 2  # Each point has a minimum distance of 1
        result = MathTool.calculate_sum_of_distances(coords1, coords2, image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_calculate_sum_of_distances_edge_cases(self):
        """
        Test edge cases for calculate_sum_of_distances.
        """
        # Identical points
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_sum_of_distances(coords1, coords2, image1, image2)
        self.assertEqual(result, expected_output)

    def test_hausdorff_distance_sum_correct_output(self):
        """
        Test that hausdorff_distance_sum produces the expected output for specific data.
        """
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 4  # Sum of minimum distances
        result = MathTool.hausdorff_distance_sum(image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_hausdorff_distance_sum_edge_cases(self):
        """
        Test edge cases for hausdorff_distance_sum.
        """
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        expected_output = 0
        result = MathTool.hausdorff_distance_sum(image1, image2)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        expected_output = float('inf')
        result = MathTool.hausdorff_distance_sum(image1, image2)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        expected_output = 0
        result = MathTool.hausdorff_distance_sum(image1, image2)
        self.assertEqual(result, expected_output)

    def test_neighboors_positive(self):
        """
        Test the neighboors_positive method.
        """
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        coords1 = (0, 0)
        self.assertTrue(MathTool.neighboors_positive(coords1, image1, image2))
        coords1 = (1, 1)
        self.assertTrue(MathTool.neighboors_positive(coords1, image1, image2))
        image1 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        image2 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        coords1 = (0, 0)
        self.assertFalse(MathTool.neighboors_positive(coords1, image1, image2))

    def test_same_value(self):
        """
        Test the same_value method.
        """
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        coords1 = (0, 0)
        self.assertFalse(MathTool.same_value(coords1, image1, image2))
        coords1 = (1, 1)
        self.assertFalse(MathTool.same_value(coords1, image1, image2))
        image2 = [[1, 0], [0, 1]]
        self.assertTrue(MathTool.same_value(coords1, image1, image2))

if __name__ == '__main__':
    unittest.main()
