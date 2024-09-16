from Object.math_tool import MathTool
import numpy as np

mt = MathTool()
image1 = np.array([[1, 1], [1, 1]])
image2 = np.array([[1, 1], [1, 1]])

print(mt.hausdorff_distance(image1,image2))