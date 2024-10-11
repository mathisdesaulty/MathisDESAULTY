# Tests

## Coverage of the 09/10/24

| Nom                              | Stmts | Miss | Cover |
|-----------------------------------|-------|------|-------|
| Notebooks\__init__.py             | 0     | 0    | 100%  |
| Object\__init__.py                | 0     | 0    | 100%  |
| Object\draw_interface.py          | 99    | 84   | 15%   |
| Object\image_user.py              | 12    | 0    | 100%  |
| Object\k_nn_mnist.py              | 78    | 0    | 100%  |
| Object\math_tool.py               | 92    | 0    | 100%  |
| Tests\__init__.py                 | 0     | 0    | 100%  |
| Tests\test_draw_interface.py      | 8     | 1    | 88%   |
| Tests\test_image_user.py          | 30    | 1    | 97%   |
| Tests\test_k_nn_mnist.py          | 154   | 33   | 79%   |
| Tests\test_math_tool.py           | 229   | 1    | 99%   |
| **TOTAL**                         | 749   | 36   | 95%   |


All tests have 100% coverage of the entire class they are testing. In each of the functions, the docstring lets you know what the test does and checks most of the problematic or useful cases.

## What has been tested and how?

The tests are present in different files:

### For ImageUser: [TestImageUser](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_image_user.py#L13) 
- How it was tested :
    - The TestImageUser test class performs simple tests on binarisation, checking whether the image is correctly processed in relation to the defined thresholds.
    - The tests are straightforward and do not deal with complex cases, because the function itself is simple.
- Types of tests: 
    - Normal operation tests
    - Default case tests
    - Limit case tests
- Inputs:
    - Image in the form of n by m matrices
    - treshold value

### For MathTool: [TestMathTool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_math_tool.py#L8) 
- What was tested: The various mathematical functions that manipulate binarised images.
How it was tested:
    - TestMathTool checks that the mathematical functions work correctly on images of different sizes.
    - Valid input cases as well as ‘side cases’ (borderline cases or input errors) have been tested to ensure that the program reacts as expected, returning errors or expected values.
- Types of tests: 
    - Tests for correct output
    - Limit case tests
- Inputs:
    - Image in the form of n by m matrices
    - Value (number of neighbours, etc.)

### For KNNClassifierMINST : [TestKNNClassifierMINST](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Object/k_nn_mnist.py#L10) 
- What was tested: The proper functioning of the K-NN class and its interactions with other classes.
How it was tested:
    - TestKNNClassifierMINST checks that the data is correctly processed when the object is created and that the functions execute without errors.
    - For performance tests, the [performance(self, num_tests=100, distance_metric='hausdorff')](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Object/k_nn_mnist.py#L170) function measures the execution time of the various distances used in the K-NN algorithm (for example, the Hausdorff distance).
- Types of tests
    - Initialization validation tests
    - Functionality tests
    - Performance testing
    - Error management tests
    - Advanced tests 
    This is the class that formats all the elements together, so it needs to be fully tested.
- Inputs:
    - Image sets for prediction
    - Values (number of tests, number of images in the dataset, etc.)

### For DrawInterface: [TestDrawInterface](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Tests/test_draw_interface.py#L26) 

This part is in the file because i don't think these tests are really usefull and takes too long to test.


## How can the tests be repeated?

## Running the Tests

To run the tests, simply navigate to the root directory of the project and execute the following command:

```bash
python3 -m unittest
```

If you want to launch one in particular:

```bash
python3 -m unittest .\Tests\[name of the tests document]
```

All tests are of the form: test_[name of the document tested].py

## The presentation of the empirical testing results 

Les tests de performances ont surtout été fait pour comparer les différentes façon de faire la distance entre 2 images, on en compte 4: 

- [hausdorff_distance(image1, image2, neighbors_offset)](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Object/math_tool.py#L90)
- [hausdorff_distance_sum(image1, image2, neighbors_offset)](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Object/math_tool.py#L155)
- [distance_d22(image1, image2, neighbors_offset)](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Object/math_tool.py#L210)
- [distance_d23(image1, image2, neighbors_offset)](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Object/math_tool.py#L228)

Ces tests sont possibles à faire vous même en lançant main.py. 