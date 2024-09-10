"""
This module contains the MathTool class with methods for calculating distances
between sets of coordinates and Hausdorff distance between binary images.
"""

import numpy as np

class MathTool:
    """
    This class provides mathematical tools for distance calculations.
    """

    @staticmethod
    def calculate_one_way_distance(coords1, coords2) -> float:
        """
        Calculates the one-way distance between two sets of coordinates.
        """
        max_min_dist = 0
        for point1 in coords1:
            min_dist = np.inf
            for point2 in coords2:
                difference = point1 - point2
                squared_diff = difference ** 2
                sum_squared_diff = np.sum(squared_diff)
                dist = np.sqrt(sum_squared_diff)
                min_dist = min(min_dist, dist)
            max_min_dist = max(max_min_dist, min_dist)
        return max_min_dist

    @staticmethod
    def hausdorff_distance(image1, image2) -> float:
        """
        Calculates the Hausdorff distance between two images.
        """
        coords1 = np.argwhere(image1 == 1)
        coords2 = np.argwhere(image2 == 1)
        # Calculate Hausdorff distance in both directions
        distance1 = MathTool.calculate_one_way_distance(coords1, coords2)
        distance2 = MathTool.calculate_one_way_distance(coords2, coords1)
        return float(max(distance1, distance2))
