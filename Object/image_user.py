"""
Module for user image processing.

This module contains the ImageUser class with methods for processing and binarizing images.
"""

from typing import List
# import numpy as np

class ImageUser:
    """
    Class to binarize images using a threshold.

    This class contains methods for processing and binarizing images.
    """

    @staticmethod
    def binarize_image(image: List[List[int]], threshold: int = 128) -> List[List[bool]]:
        """
        Binarize the image based on the threshold value.

        Converts pixel values of the image to 1 if they are greater than or equal
        to the threshold, otherwise to 0.

        :param image: The image to binarize, provided as a 2d List.
        :param threshold: Threshold value for binarization, default is 128.
        :return: The binarized image as a list of lists of booleans.
        """

        # Get the dimensions of the image
        rows, cols = len(image), len(image[0])

        # Initialize the binarized image
        binarized_image = [[False for _ in range(cols)] for _ in range(rows)]

        # Binarize the image
        for i in range(rows):
            for j in range(cols):
                if image[i][j] >= threshold:
                    binarized_image[i][j] = True
                else:
                    binarized_image[i][j] = False

        return binarized_image
