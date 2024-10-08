# Tests

The tests are present in different files:

- For ImageUser: [TestImageUser](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_image_user.py#L13)
- For MathTool: [TestMathTool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Tests/test_math_tool.py#L8)
- For KNNClassifierMINST : [KNNClassifierMINST](https://github.com/mathisdesaulty/MathisDESAULTY/blob/b7c0243883b0e6971cedae4c70a3e1989d6b2ff6/Object/k_nn_mnist.py#L10)

All tests tend to have 100% coverage of the entire class they are testing (In progress). In each of the functions, the docstring lets you know what the test does and checks most of the problematic or useful cases.

## Coverage of the 07/10/24

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
