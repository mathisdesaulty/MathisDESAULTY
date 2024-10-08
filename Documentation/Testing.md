# Tests

The tests are present in different files:

- For ImageUser: [TestImageUser](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_image_user.py#L13) checks that the image binarisation function works correctly and that treshold also works. This is the simplest test class to understand because the binarisation function itself is not complex.

- For MathTool: [TestMathTool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_math_tool.py#L8) checks that all the maths functions execute correctly. Most of the functions take binarised images as parameters, so all the checks are made to ensure that they work properly, i.e. checking that they are of different sizes, that they are equal from the start of the comparison and a number of other things. In these tests we have tests with correct inputs and side cases to check that the code returns what we want when the input data is wrong. 

- For KNNClassifierMINST : [KNNClassifierMINST](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Object/k_nn_mnist.py#L10) checks that the K-NN class works properly. Most tests simply check whether the information is taken into account when the object is created. They can also be used to check whether the functions in this class are executed completely. Of course, this code uses all the other classes we talked about earlier, so it checks that all these classes work together as they should. For performance tests, there's the [performance(self, num_tests=100, distance_metric='hausdorff')](https://github.com/mathisdesaulty/MathisDESAULTY/blob/1718d8419386a99b03875ee3ab3af6696bec93a3/Object/k_nn_mnist.py#L170-L171) in the K-NN class, which allows you to find out how long the code takes by comparing the different distance functions, if you wish. 

All tests tend have 100% coverage of the entire class they are testing. In each of the functions, the docstring lets you know what the test does and checks most of the problematic or useful cases.

## Coverage of the 08/10/24

| Nom                              | Stmts | Miss | Cover |
|-----------------------------------|-------|------|-------|
| Notebooks\__init__.py             | 0     | 0    | 100%  |
| Object\__init__.py                | 0     | 0    | 100%  |
| Object\draw_interface.py          | 99    | 0    | 100%  |
| Object\image_user.py              | 12    | 0    | 100%  |
| Object\k_nn_mnist.py              | 78    | 0    | 100%  |
| Object\math_tool.py               | 92    | 0    | 100%  |
| Tests\__init__.py                 | 0     | 0    | 100%  |
| Tests\test_draw_interface.py      | 55    | 1    | 98%   |
| Tests\test_image_user.py          | 30    | 1    | 97%   |
| Tests\test_k_nn_mnist.py          | 154   | 33   | 79%   |
| Tests\test_math_tool.py           | 229   | 1    | 99%   |
| **TOTAL**                         | 749   | 36   | 95%   |
