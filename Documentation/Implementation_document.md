# Implementation Document

## General structure of the program

Le programme est composé de deux packages: Object et Tests. 

### Tests
Tests lets you test all the classes we'll be talking about next. In this section, we have test classes produced with the unittest module, which makes it easy to run tests. For more information on tests, you can use the documentation [Testing](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Documentation/Testing.md#L1).

### Object

Object is a package containing all the elements needed for the final algorithm to function correctly, which are in [main.py](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/main.py#L5). Nous allons alors voir comment cela marche:

- [KNNClassifierMNIST](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/k_nn_mnist.py#L10) is a class for using the K-NN algorithm on the MNIST dataset. It includes functions for predicting a single element, several elements, getting feedback on all predictions, the first prediction only, or predicting with a pre-parameterised dataset. To function, this class needs two other classes:
    - [ImageUser](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/image_user.py#L10) is a class for taking images and binarising them so that they can be used in the K-NN algorithm. It has only one function, allowing images to be binarised according to the treshold given to it.
    - [MathTool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/math_tool.py#L6) is a class that allows you to do many things, and is the root of this project. This class contains all the distance functions, themselves in the form of several functions (neighbour calculations, etc.), between two images in the form of a binarised data matrix. In this class we have 5 distance functions: Hausdorff distance, Hausdorff distance modified with the sum, D22 distance, D23 distance and one last one, which is compulsory for the last two, D6 distance.


## The time and space complexities achieved

### K-NN with Hausdorff 

- The time complexity of Hausdorff distance for the worst case is O(n².m²) when all the points are positive, except that in our case, as we look each time at what the same point is positive in the other image, then we would have a completeness of O(n.m) operations. The worst case would then be every other square in each of the images with no neighbour checks. This would give us O(((n.m)/2)²). However, we are concentrating on long-term growth and we can therefore remove the constant. 
