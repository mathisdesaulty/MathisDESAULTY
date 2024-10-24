# Implementation Document

## General structure of the program

The programme consists of two packages: Object et Tests. 

### Tests
Tests lets you test all the classes we'll be talking about next. In this section, we have test classes produced with the unittest module, which makes it easy to run tests. For more information on tests, you can use the documentation [Testing](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Documentation/Testing.md#L1).

### Object

Object is a package containing all the elements needed for the final algorithm to function correctly, which are in [main.py](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/main.py#L5). Let's see how it works:

- [KNNClassifierMNIST](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/k_nn_mnist.py#L10) is a class for using the K-NN algorithm on the MNIST dataset. It includes functions for predicting a single element, several elements, getting feedback on all predictions, the first prediction only, or predicting with a pre-parameterised dataset. To function, this class needs two other classes:
    - [ImageUser](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/image_user.py#L10) is a class for taking images and binarising them so that they can be used in the K-NN algorithm. It has only one function, allowing images to be binarised according to the treshold given to it.
    - [MathTool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/314fcff79ede4a74cac797ddd7f575dbe885dae6/Object/math_tool.py#L6) is a class that allows you to do many things, and is the root of this project. This class contains all the distance functions, themselves in the form of several functions (neighbour calculations, etc.), between two images in the form of a binarised data matrix. In this class we have 5 distance functions: Hausdorff distance, Hausdorff distance modified with the sum, D22 distance, D23 distance and one last one, which is compulsory for the last two, D6 distance.


## The time and space complexities achieved

### K-NN with Hausdorff and Hausdorff sum

- The time complexity of Hausdorff distance for the worst case is O(n².m²) when all the points are positive, except that in our case, as we look each time at what the same point is positive in the other image, then we would have a completeness of O(n.m) operations. The worst case would then be every other square in each of the images with no neighbour checks. This would give us O(((n.m)/2)²). However, we are concentrating on long-term growth and we can therefore remove the constant.
- The completion time with the sum remains the same, as both work in the same way. However, we know that for the sum we use the square root and so it will take a little longer.

The completion time for the Hausdorff distance is O(t.(p.(n.m)²+t.p.log(p))). O(t.p.(n.m)²) represents the completeness of all distances calculated with t, the number of test images, p the number of images in the comparison dataset and n.m the size of an image. O(t.p.log(p)) is less insignificant but should be noted, it is the sorting of the list to take the smallest distances. If we want to be more precise for our case: we only have images measuring 28 pixels by 28, so 784 pixels each: 
O(t.(p.784²+p.log(p))).

### K-NN with D22 et D23 distances

The complexity remains the same as for the Haussdorf distance because the only differences in execution time are whether or not to use the root in calculating a distance from one point to another:
O(t.(p.784+n.log(n))), for the MNIST dataset.

## Performance and Big O analysis comparison

So we can't compare the complexity because for the 4 distances we're using, it's more or less the same. However, there are differences between the distances which mean that they don't have the same performance.
Firstly, it is possible to run these performance tests by launching main :

```bash
python3 main.py
```

but also by simply launching:

```bash
python3 performance_test.py
```

Here's the table of performance tests I was able to run:

| Dataset(size, number of tests) | Metric         | Performance | Ratio    | Time (seconds)       |
|-------------------------------|----------------|-------------|----------|----------------------|
| 1000, 10                       | Default        | 0.9         | (9, 10)  | 16.60970664024353     |
|                               | Hausdorff_sum  | 1.0         | (10, 10) | 17.698243618011475    |
|                               | D22            | 1.0         | (10, 10) | 18.353026866912842    |
|                               | D23            | 1.0         | (10, 10) | 18.28653311729431     |
| 30, 5000                       | Default        | 0.9         | (27, 30) | 235.08828711509705    |
|                               | Hausdorff_sum  | 0.9667      | (29, 30) | 250.10133838653564    |
|                               | D22            | 0.9333      | (28, 30) | 257.7845547199249     |
|                               | D23            | 0.9667      | (29, 30) | 250.75405430793762    |
| 1, 70000                       | Default        | 0.0         | (0, 1)   | 107.64047741889954    |
|                               | Hausdorff_sum  | 1.0         | (1, 1)   | 108.0590009689331     |
|                               | D22            | 1.0         | (1, 1)   | 116.72253632545471    |
|                               | D23            | 1.0         | (1, 1)   | 114.389075756073      |

In terms of performance, we can see that the Hausdorff sum, the D22 distance and the D23 distance show a slight dominance over the Hausdorff distance, although the Hausdorff distance wins in terms of execution time. This difference in performance is due to the fact that the normal Hausdorff distance only takes the maximum of the distances we calculate. In terms of calculation time, we know that the unmodified Hausdorff distance doesn't use the square root function and therefore saves a little time over the other 3.

## Use of extensive language models

For this project I mainly used GitHub Copilot for writing long code or quick tests to test my code. I also used ChatGPT in case of misunderstanding about something too specific to be found online. 
Most of the code and documentation is written by myself with the help of GitHub Copilot to simplify code writing.

## References 

- [Modifications of hausdorff distance for object matching](https://www.researchgate.net/publication/290011464_Modifications_of_hausdorff_distance_for_object_matching)
- [KNN (K Nearest Neighbors) in Python - Machine Learning From Scratch 01 - Python Tutorial](https://www.youtube.com/watch?v=ngLyX54e1LU)
- My courses last year at the University of La Rochelle (Analyse de donnée (Data analysis) by Carl FRELICOT).
- [ChatGPT](https://chatgpt.com/) and [GitHub Copilot](https://github.com/features/copilot) and my knowledge for binarising images 
- [Tk Documentation](https://docs.python.org/3/library/tk.html)
- [PIL Documentation](https://pillow.readthedocs.io/en/stable/)
