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
    def calculate_one_way_distance(coords1, coords2, image1, image2) -> float:
        """
        Calculates the one-way distance between two sets of coordinates.
        Optimized to skip points that have the same value in both images at the same location.
        """
        max_min_dist = 0
        neighbors_offset = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),(0, 0), (0, 1),
                            (1, -1), (1, 0), (1, 1)]
        for point1 in coords1:
            # Extract the corresponding coordinates in both images
            x1, y1 = point1
            min_dist = np.inf
            # If the same coordinates in both images have the same value, skip the calculation
            if image1[x1, y1] == image2[x1, y1]:
                min_dist = 0
            else: 
                find = False
                for x, y in neighbors_offset:
                    x2, y2 = x1 + x, y1 + y
                    if (
                        image2.shape[0] > x2
                        and image2.shape[1] > y2
                        and image2[x2, y2] == image1[x1, y1]
                    ):
                        find = True
                        min_dist = 1
                        break
                if find:
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
        # Convert image1 and image2 to numpy arrays
        npimage1 = np.array(image1)
        npimage2 = np.array(image2)
        # Check if either image is empty
        if npimage1.size == 0 or npimage2.size == 0:
            if npimage1.size != npimage2.size:
                return float('inf')
            return 0
        # Get coordinates of True (or 1) values in the images
        coords1 = np.argwhere(npimage1 == 1)
        coords2 = np.argwhere(npimage2 == 1)
        # Calculate Hausdorff distance in both directions
        distance1 = MathTool.calculate_one_way_distance(coords1, coords2, npimage1, npimage2)
        distance2 = MathTool.calculate_one_way_distance(coords2, coords1, npimage2, npimage1)
        return float(max(distance1, distance2))