"""
Module for user image processing.

This module contains the ImageUser class with methods for processing and binarizing images.
"""

from typing import List
import numpy as np

class ImageUser:
    """
    Class to binarize images using a threshold.

    This class contains a method to convert a grayscale image to a binary image
    based on a specified threshold value.
    """

    def binarize_image(self, image: np.ndarray, threshold: int = 128) -> List[List[int]]:
        """
        Binarize the image based on the threshold value.

        Converts pixel values of the image to 1 if they are greater than or equal
        to the threshold, otherwise to 0.

        :param image: The image to binarize, provided as a NumPy array.
        :param threshold: Threshold value for binarization, default is 128.
        :return: The binarized image as a list of lists of integers.
        """
        # Check that the image is a NumPy array
        if not isinstance(image, np.ndarray):
            raise TypeError("The image must be a NumPy array.")

        # Get the dimensions of the image
        rows, cols = image.shape

        # Initialize the binarized image
        binarized_image = [[0 for _ in range(cols)] for _ in range(rows)]

        # Binarize the image
        for i in range(rows):
            for j in range(cols):
                if image[i][j] >= threshold:
                    binarized_image[i][j] = 1
                else:
                    binarized_image[i][j] = 0

        return binarized_image