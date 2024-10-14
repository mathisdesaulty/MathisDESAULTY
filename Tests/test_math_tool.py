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
        neighbors_offset = MathTool.generate_neighbors_offsets(1)
        coords1 = [[0, 0], [1, 1]]
        coords2 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_one_way_distance(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)
        neighbors_offset = MathTool.generate_neighbors_offsets(1)
        image2 = [[1, 0], [0, 0]]
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        expected_output = 0
        result = MathTool.calculate_one_way_distance(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)
        neighbors_offset = MathTool.generate_neighbors_offsets(0)
        image2 = [[0, 0], [0, 1]]
        coords1 = [[0, 0]]
        coords2 = [[1, 1]]
        expected_output = 2
        result = MathTool.calculate_one_way_distance(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_calculate_one_way_distance_edge_cases(self):
        """
        Test edge cases for calculate_one_way_distance.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(1)
        # Identical points
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_one_way_distance(
            coords1, coords2, image2, neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_hausdorff_distance_correct_output(self):
        """
        Test that hausdorff_distance produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        points1 = [[0, 0], [1, 1]]
        points2 = [[1, 0], [0, 1]]
        expected_output = 1  # Maximum distance between non-matching points
        result = MathTool.hausdorff_distance(image1, image2,points1,points2,neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_hausdorff_distance_edge_cases(self):
        """
        Test edge cases for hausdorff_distance.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        points1 = [[]]
        points2 = [[]]
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2,points1,points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[]]  # Empty image
        expected_output = float('inf')
        result = MathTool.hausdorff_distance(image1, image2,points1,points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2, points1,points2,neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_calculate_sum_of_distances_correct_output(self):
        """
        Test that calculate_sum_of_distances produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        coords1 = [[0, 0], [1, 1]]
        coords2 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 2  # Each point has a minimum distance of 1
        result = MathTool.calculate_sum_of_distances(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)
        neighbors_offset = MathTool.generate_neighbors_offsets(0)
        coords1 = [[0, 0], [1, 1]]
        coords2 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 2  # Each point has a minimum distance of 1
        result = MathTool.calculate_sum_of_distances(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)
        neighbors_offset = MathTool.generate_neighbors_offsets(0)
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        image2 = [[1, 0], [0, 0]]
        expected_output = 0
        result = MathTool.calculate_sum_of_distances(
            coords1, coords2, image2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_calculate_sum_of_distances_edge_cases(self):
        """
        Test edge cases for calculate_sum_of_distances.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Identical points
        coords1 = [[0, 0]]
        coords2 = [[0, 0]]
        image2 = [[0, 1], [1, 0]]
        expected_output = 1
        result = MathTool.calculate_sum_of_distances(
            coords1, coords2, image2, neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_hausdorff_distance_sum_correct_output(self):
        """
        Test that hausdorff_distance_sum produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        points1 = [[0, 0], [1, 1]]
        points2 = [[1, 0], [0, 1]]
        expected_output = 4  # Sum of minimum distances
        result = MathTool.hausdorff_distance_sum(image1, image2,points1,points2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_hausdorff_distance_sum_edge_cases(self):
        """
        Test edge cases for hausdorff_distance_sum.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        points1 = [[]]
        points2 = [[]]
        expected_output = 0
        result = MathTool.hausdorff_distance_sum(image1, image2,points1,points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[]]
        expected_output = float('inf')
        result = MathTool.hausdorff_distance_sum(image1, image2,points1,points2,neighbors_offset)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        expected_output = 0
        result = MathTool.hausdorff_distance_sum(image1, image2,points1,points2, neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_neighbors_positive(self):
        """
        Test the neighbors_positive method.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image2 = [[0, 1], [1, 0]]
        coords1 = (0, 0)
        expected_output = (True, 1.0)
        self.assertEqual(
            MathTool.neighbors_positive(coords1, image2, neighbors_offset), expected_output)
        coords1 = (1, 1)
        expected_output = (True, 1.0)
        self.assertEqual(
            MathTool.neighbors_positive(coords1, image2, neighbors_offset), expected_output)
        image2 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        coords1 = (0, 0)
        expected_output = (True, 8**0.5 )
        self.assertEqual(
            MathTool.neighbors_positive(coords1, image2, neighbors_offset), expected_output)
        image2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        coords1 = (0, 0)
        expected_output = (False, 0.0)
        self.assertEqual(
            MathTool.neighbors_positive(coords1, image2, neighbors_offset), expected_output)

    def test_generate_neighbors_offsets(self):
        """
        Test the generate_neighbors_offsets method.
        """
        # Test with n = 1
        n = 1
        expected_output = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 0), (0, 1),
                           (1, -1), (1, 0), (1, 1)]
        expected_output.sort(key=lambda offset: (offset[0]**2 + offset[1]**2), reverse=False)
        dico = {}
        for i in expected_output:
            dico[i] = (i[0]**2 + i[1]**2)**0.5
        result = MathTool.generate_neighbors_offsets(n)
        self.assertEqual(result, dico)

        # Test with n = 0
        n = 0
        expected_output = {(0, 0): 0.0}
        result = MathTool.generate_neighbors_offsets(n)
        self.assertEqual(result, expected_output)

        # Test with n = 2
        n = 2
        expected_output = [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
                           (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                           (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
                           (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
                           (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]
        expected_output.sort(key=lambda offset: (offset[0]**2 + offset[1]**2), reverse=False)
        dico = {}
        for i in expected_output:
            dico[i] = (i[0]**2 + i[1]**2)**0.5
        result = MathTool.generate_neighbors_offsets(n)
        self.assertEqual(result, dico)

    def test_distance_d6_correct_output(self):
        """
        Test that distance_d6 produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        points1 = [[0, 0], [1, 1]]
        points2 = [[1, 0], [0, 1]]
        expected_output = 1  # Average minimum distance
        result = MathTool.distance_d6(image1, image2, points1, points2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_distance_d6_edge_cases(self):
        """
        Test edge cases for distance_d6.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        points1 = [[]]
        points2 = [[]]
        expected_output = 0
        result = MathTool.distance_d6(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        points1 = [[i, j] for i in range(len(image1))
                   for j in range(len(image1[0])) if image1[i][j] == 1]
        points2 = [[]]
        expected_output = float('inf')
        result = MathTool.distance_d6(image1,image2,points1,points2,neighbors_offset)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        expected_output = 0
        result = MathTool.distance_d6(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_distance_d22_correct_output(self):
        """
        Test that distance_d22 produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        points1 = [[0, 0], [1, 1]]
        points2 = [[1, 0], [0, 1]]
        expected_output = 1  # Maximum of average minimum distances
        result = MathTool.distance_d22(image1, image2, points1, points2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_distance_d22_edge_cases(self):
        """
        Test edge cases for distance_d22.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        points1 = [[]]
        points2 = [[]]
        expected_output = 0
        result = MathTool.distance_d22(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        points1 = [[i, j] for i in range(len(image1))
                   for j in range(len(image1[0])) if image1[i][j] == 1]
        points2 = [[]]
        expected_output = float('inf')
        result = MathTool.distance_d22(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        expected_output = 0
        result = MathTool.distance_d22(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

    def test_distance_d23_correct_output(self):
        """
        Test that distance_d23 produces the expected output for specific data.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        image1 = [[1, 0], [0, 1]]
        image2 = [[0, 1], [1, 0]]
        points1 = [[0, 0], [1, 1]]
        points2 = [[1, 0], [0, 1]]
        expected_output = 1  # Average of average minimum distances
        result = MathTool.distance_d23(image1, image2, points1, points2, neighbors_offset)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_distance_d23_edge_cases(self):
        """
        Test edge cases for distance_d23.
        """
        neighbors_offset = MathTool.generate_neighbors_offsets(4)
        # Both images are empty
        image1 = [[]]
        image2 = [[]]
        points1 = [[]]
        points2 = [[]]
        expected_output = 0
        result = MathTool.distance_d23(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = [[1, 1], [1, 1]]
        image2 = [[]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[]]
        expected_output = float('inf')
        result = MathTool.distance_d23(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = [[1, 1], [1, 1]]
        image2 = [[1, 1], [1, 1]]
        points1 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        points2 = [[0, 0], [1, 1], [0, 1], [1, 0]]
        expected_output = 0
        result = MathTool.distance_d23(image1, image2, points1, points2, neighbors_offset)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
