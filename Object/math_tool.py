"""
This module provides the MathTool class with methods for distance calculations
between images.
"""

class MathTool:
    """
    This class provides mathematical tools for distance calculations.
    """

    @staticmethod
    def neighboors_positive(coords1, image1, image2):
        """
        Check if the given coordinates have positive neighbors in the provided images.
        Parameters:
        - coords1 (tuple): The coordinates (x, y) to check for positive neighbors.
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        Returns:
        - find (bool): True if positive neighbors are found, False otherwise.
        """
        neighbors_offset = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1), (0, 0), (0, 1),
                            (1, -1), (1, 0), (1, 1)]
        find = False
        x1, y1 = coords1
        for x, y in neighbors_offset:
            x2, y2 = x1 + x, y1 + y
            if (0 <= x2 < len(image2)
                and 0 <= y2 < len(image2[0])
                and image1[x1][y1] == 1 and image2[x2][y2] == 1):
                find = True
                return find
        return find

    @staticmethod
    def same_value(coords1, image1, image2):
        """
        Check if the pixel values at the given coordinates in two images are the same.
        Args:
        - coords1 (tuple): The coordinates (x, y) to check.
        - image1 (list of lists): First image.
        - image2 (list of lists): Second image.
        Returns:
        - bool: True if the pixel values are the same in both images, False otherwise.
        """
        return image1[coords1[0]][coords1[1]] == image2[coords1[0]][coords1[1]]

    @staticmethod
    def calculate_one_way_distance(coords1, coords2, image1, image2) -> float:
        """
        Calculates the one-way distance between two sets of coordinates.
        Optimized to skip points that have the same value in both images at the same location.
        """
        max_min_dist = 0
        for point1 in coords1:
            min_dist = float('inf')
            if MathTool.same_value(point1, image1, image2):
                min_dist = 0
            else:
                if MathTool.neighboors_positive(point1, image1, image2):
                    min_dist = 1
                else:
                    for point2 in coords2:
                        squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
                        min_dist = min(min_dist, squared_diff)
            max_min_dist = max(max_min_dist, min_dist)
        return max_min_dist

    @staticmethod
    def hausdorff_distance(image1, image2) -> float:
        """
        Calculates the Hausdorff distance between two images.
        """
        # Check if either image is empty
        if not image1 or not image2 or image1 == image2: 
            return 0
        if len(image1) != len(image2) or len(image1[0]) != len(image2[0]):
            return float('inf')
        
        # Get coordinates of True (or 1) values in the images
        coords1 = [(i, j) for i in range(len(image1)) for j in range(len(image1[0])) if image1[i][j] == 1]
        coords2 = [(i, j) for i in range(len(image2)) for j in range(len(image2[0])) if image2[i][j] == 1]
        # Calculate Hausdorff distance in both directions
        distance1 = MathTool.calculate_one_way_distance(coords1, coords2, image1, image2)
        distance2 = MathTool.calculate_one_way_distance(coords2, coords1, image2, image1)
        return max(distance1, distance2)  # Maximum of both directions

    @staticmethod
    def calculate_sum_of_distances(coords1, coords2, image1, image2) -> float:
        """
        Calculates the sum of Euclidean distances between two sets of coordinates.
        Optimized to skip points that have the same value in both images at the same location
        or have positive neighbors.
        """
        total_distance = 0
        for point1 in coords1:
            min_dist = float('inf')
            if MathTool.same_value(point1, image1, image2):
                min_dist = 0
            elif MathTool.neighboors_positive(point1, image1, image2):
                min_dist = 1
            else:
                for point2 in coords2:
                    squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
                    euclidean_dist = squared_diff ** 0.5  # Euclidean distance with square root
                    min_dist = min(min_dist, euclidean_dist)
            total_distance += min_dist
        return total_distance

    @staticmethod
    def hausdorff_distance_sum(image1, image2) -> float:
        """
        Calculates the sum of Hausdorff distances (using Euclidean distance) between two images.
        """
        # Check if either image is empty
        if not image1 or not image2 or image1 == image2: 
            return 0
        if len(image1) != len(image2) or len(image1[0]) != len(image2[0]):
            return float('inf')
        # Get coordinates of True (or 1) values in the images
        coords1 = [(i, j) for i in range(len(image1)) for j in range(len(image1[0])) if image1[i][j] == 1]
        coords2 = [(i, j) for i in range(len(image2)) for j in range(len(image2[0])) if image2[i][j] == 1]
        # Calculate the sum of Hausdorff distances in both directions
        sum_distance = MathTool.calculate_sum_of_distances(coords1, coords2, image1, image2)
        sum_distance += MathTool.calculate_sum_of_distances(coords2, coords1, image2, image1)
        return sum_distance  # Sum of both directions
