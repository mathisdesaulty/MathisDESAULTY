"""
This module provides the MathTool class with methods for distance calculations
between images.
"""

class MathTool:
    """
    This class provides mathematical tools for distance calculations.
    """
    @staticmethod
    def generate_neighbors_offsets(n):
        """
        Generate a list of neighbor offsets for a given number of circles.

        Parameters:
        - n (int): The number of circles of neighbors to generate.

        Returns:
        - list of tuples: A list of (x, y) offsets for the neighbors,
          sorted from the farthest to the nearest.
        """
        neighbors_offset = []
        for i in range(-n, n + 1):
            for j in range(-n, n + 1):
                neighbors_offset.append((i, j))

        # Sort the offsets by distance from the origin (0, 0), farthest to nearest
        neighbors_offset.sort(key=lambda offset: (offset[0] ** 2 + offset[1] ** 2), reverse=False)
        return neighbors_offset

    @staticmethod
    def neighbors_positive(coords1, image1, image2, neighbors_offset):
        """
        Check if the given coordinates have positive neighbors in the provided images.

        Parameters:
        - coords1 (tuple): The coordinates (x, y) to check for positive neighbors.
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - tuple: (bool, tuple): True if positive neighbors are found, False otherwise.
          The tuple contains the offset of the positive neighbor.
        """
        find = False
        x1, y1 = coords1
        for x, y in neighbors_offset:
            x2, y2 = x1 + x, y1 + y
            if (0 <= x2 < len(image2)
                and 0 <= y2 < len(image2[0])
                and image1[x1][y1] == 1 and image2[x2][y2] == 1):
                find = True
                return (find, (x, y))
        return (find, (0, 0))

    @staticmethod
    def calculate_one_way_distance(coords1, coords2, image1, image2, neighbors_offset) -> float:
        """
        Calculates the one-way distance between two sets of coordinates.
        Optimized to skip points that have the same value in both images at the same location.

        Parameters:
        - coords1 (list of tuples): Coordinates from the first image.
        - coords2 (list of tuples): Coordinates from the second image.
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated one-way distance.
        """
        max_min_dist = 0
        for point1 in coords1:
            min_dist = float('inf')
            if image2[point1[0]][point1[1]] == 1:
                min_dist = 0
            else:
                neighbors = MathTool.neighbors_positive(point1, image1, image2, neighbors_offset)
                if neighbors[0]:
                    min_dist = neighbors[1][0] ** 2 + neighbors[1][1] ** 2
                else:
                    for point2 in coords2:
                        squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
                        min_dist = min(min_dist, squared_diff)
            max_min_dist = max(max_min_dist, min_dist)
        return max_min_dist

    @staticmethod
    def hausdorff_distance(image1, image2, neighbors_offset) -> float:
        """
        Calculates the Hausdorff distance between two images.

        Parameters:
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated Hausdorff distance.
        """
        # Check if either image is empty
        if not image1 or not image2 or image1 == image2:
            return 0
        if len(image1) != len(image2) or len(image1[0]) != len(image2[0]):
            return float('inf')
        # Get coordinates of True (or 1) values in the images
        coords1 = [
            (i, j) for i in range(len(image1)) for j in range(len(image1[0])) if image1[i][j] == 1]
        coords2 = [
            (i, j) for i in range(len(image2)) for j in range(len(image2[0])) if image2[i][j] == 1]
        # Calculate Hausdorff distance in both directions
        distance1 = MathTool.calculate_one_way_distance(
            coords1, coords2, image1, image2, neighbors_offset)
        distance2 = MathTool.calculate_one_way_distance(
            coords1=coords2, coords2=coords1, image1=image2, 
            image2=image1, neighbors_offset=neighbors_offset)
        return max(distance1, distance2)  # Maximum of both directions

    @staticmethod
    def calculate_sum_of_distances(coords1, coords2, image1, image2, neighbors_offset) -> float:
        """
        Calculates the sum of Euclidean distances between two sets of coordinates.
        Optimized to skip points that have the same value in both images at the same location
        or have positive neighbors.

        Parameters:
        - coords1 (list of tuples): Coordinates from the first image.
        - coords2 (list of tuples): Coordinates from the second image.
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated sum of distances.
        """
        total_distance = 0
        for point1 in coords1:
            min_dist = float('inf')
            if image2[point1[0]][point1[1]] == True:
                min_dist = 0
            else:
                neighbors = MathTool.neighbors_positive(point1, image1, image2, neighbors_offset)
                if neighbors[0]:
                    min_dist = (neighbors[1][0] ** 2 + neighbors[1][1] ** 2) ** 0.5
                else:
                    for point2 in coords2:
                        squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
                        euclidean_dist = squared_diff ** 0.5  # Euclidean distance with square root
                        min_dist = min(min_dist, euclidean_dist)
            total_distance += min_dist
        return total_distance

    @staticmethod
    def hausdorff_distance_sum(image1, image2, neighbors_offset) -> float:
        """
        Calculates the sum of Hausdorff distances (using Euclidean distance) between two images.

        Parameters:
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated sum of Hausdorff distances.
        """
        # Check if either image is empty
        if not image1 or not image2 or image1 == image2:
            return 0
        if len(image1) != len(image2) or len(image1[0]) != len(image2[0]):
            return float('inf')
        # Get coordinates of True (or 1) values in the images
        coords1 = [
            (i, j) for i in range(len(image1)) for j in range(len(image1[0])) if image1[i][j] == 1]
        coords2 = [
            (i, j) for i in range(len(image2)) for j in range(len(image2[0])) if image2[i][j] == 1]
        # Calculate the sum of Hausdorff distances in both directions
        sum_distance = MathTool.calculate_sum_of_distances(
            coords1, coords2, image1, image2, neighbors_offset)
        sum_distance += MathTool.calculate_sum_of_distances(
            coords1=coords2, coords2=coords1, image1=image2,image2=image1, 
            neighbors_offset=neighbors_offset)
        return sum_distance  # Sum of both directions

    @staticmethod
    def distance_d6(image1, image2, neighbors_offset) -> float:
        """
        Calculates the distance between two images using the d6 metric.

        Parameters:
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated d6 distance.
        """
        if not image1 or not image2 or image1 == image2:
            return 0
        points1 = [
            (i, j) for i in range(len(image1)) for j in range(len(image1[0])) if image1[i][j] == 1]
        points2 = [
            (i, j) for i in range(len(image2)) for j in range(len(image2[0])) if image2[i][j] == 1]
        if len(points1) == 0 or len(points2) == 0:
            return float('inf')
        distance = MathTool.calculate_sum_of_distances(points1, points2, image1, image2, neighbors_offset)
        return distance / len(points1)

    @staticmethod
    def distance_d22(image1, image2, neighbors_offset):
        """
        Calculates the distance between two images using the d22 metric.

        Parameters:
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated d22 distance.
        """
        distance1 = MathTool.distance_d6(image1, image2, neighbors_offset)
        distance2 = MathTool.distance_d6(
            image1=image2, image2=image1, neighbors_offset=neighbors_offset)
        return max(distance1, distance2)

    @staticmethod
    def distance_d23(image1, image2, neighbors_offset):
        """
        Calculates the distance between two images using the d23 metric.

        Parameters:
        - image1 (list of lists): The first image.
        - image2 (list of lists): The second image.
        - neighbors_offset (list of tuples): List of neighbor offsets.

        Returns:
        - float: The calculated d23 distance.
        """
        
        distance1 = MathTool.distance_d6(image1, image2, neighbors_offset)
        distance2 = MathTool.distance_d6(
            image1=image2, image2=image1, neighbors_offset=neighbors_offset)
        return (distance1 + distance2) / 2
