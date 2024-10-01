"""
Unit tests for the ImageUser class.

This module contains test cases for the methods of the ImageUser class,
specifically the binarize_image method. The tests cover various scenarios
including normal operation, default thresholds, invalid inputs, and edge cases.
"""

import unittest
import numpy as np
from Object.image_user import ImageUser

class TestImageUser(unittest.TestCase):
    """
    Test cases for the ImageUser class.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        This method is called before every individual test case.
        """

    def test_binarize_image_correct_output(self):
        """
        Test that binarize_image produces the expected output for a given image and threshold.

        This test checks if the binarize_image method correctly binarizes an image
        when a specific threshold is provided.
        """
        image = np.array([[100, 150], [200, 50]])
        expected_output = [[False, True], [True, False]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

    def test_binarize_image_default_threshold(self):
        """
        Test that binarize_image correctly uses the default threshold of 128.

        This test verifies that the binarize_image method uses the default threshold
        value of 128 when no threshold is explicitly provided.
        """
        image = np.array([[100, 150], [200, 50]])
        expected_output = [[False, True], [True, False]]
        result = ImageUser.binarize_image(image)  # Default threshold of 128
        self.assertEqual(result, expected_output)

    def test_binarize_image_edge_cases(self):
        """
        Test edge cases for the binarize_image method.

        This test covers various edge cases including:
        - An empty image.
        - An image with all pixels above the threshold.
        - An image with all pixels below the threshold.
        """
        # Empty image
        image = np.array([[]])
        expected_output = [[]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

        # Image with all pixels above the threshold
        image = np.array([[255, 255], [255, 255]])
        expected_output = [[True, True], [True, True]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

        # Image with all pixels below the threshold
        image = np.array([[0, 0], [0, 0]])
        expected_output = [[False, False], [False, False]]
        result = ImageUser.binarize_image(image, threshold=128)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
