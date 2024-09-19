# Week 3 report

Approximatively 2 hours by day this week so 10 hours or less.

## What I've learned

This week has been mostly about code and thinking about how to set up the various elements, but what I've learnt in particular this week is how to use the coverage tool. This tool lets us know for each of our tests which part of which code it covers and the percentage of coverage of that code. I was then able to test it on the various tests I'd already done. This week I also had a chance to think about the K-NN algorithm, which I'll go into in more detail later.

## What I did this week

### Improvement on previous codes 

This week started with improving last week's versions of the classes, especially the maths class. The main problem was that we could drastically optimise the calculation of the Haussford distance. So I followed the advice of our teachers: for each point, we calculate the distance between it and all the points in the other image. A simple way of optimising this is to first look at all the points to see if they also have a positive coordinate for the second image. We could then directly send the value 0. We could also look at its neighbours, to give the value 1 and then test with all the points. The first version of this modified function was made up of too many lines but was also complicated to debug because of its length. So I preferred to try refactoring, which took a bit of time. However, it's now easier to change elements of this distance because it's made up of 3 functions that make the code less annoying to read and more understandable. You can see the code here: *[math_tool](https://github.com/mathisdesaulty/MathisDESAULTY/blob/c3692891743d930938445ab2cc248ce295faecb1/Object/math_tool.py#L14)*.

### Creation of the K-NN algorithm

####  __init__ function
Last week consisted of setting up the various tools to be able to implement the most important algorithm of this project: the K-NN. This week therefore consisted of starting to make the K-NN and having a usable version that would give some initial results. So I had a basic version of K-NN to work with. This version was not at all suited to using the MNIST dataset. I then started to implement in the function *[init](https://github.com/mathisdesaulty/MathisDESAULTY/blob/c3692891743d930938445ab2cc248ce295faecb1/Object/k_nn_mnist.py#L16-L29)* in which I initialise the dataset directly so that I can use it. During my first week's tests I had already tried to calculate distances as you can see here: *[notebook](https://github.com/mathisdesaulty/MathisDESAULTY/blob/c3692891743d930938445ab2cc248ce295faecb1/Notebooks/haussdorf_distance.ipynb)*. I was then able to reuse these tests to ensure that we first had the labels in one variable and in the other the MNIST dataset in the correct format and binarised as we can see in the *init* function above.

#### Prediction and Tests

The algorithm has no training function, in fact it will simply make comparisons and give a result. So all we need is a function to predict the K-NNs. I was able to create two functions: firstly, the prediction function: [def _predict(self, x):](https://github.com/mathisdesaulty/MathisDESAULTY/blob/c3692891743d930938445ab2cc248ce295faecb1/Object/k_nn_mnist.py#L39-L56), function for predicting a single element, as I don't think it's necessarily useful and most of the time tests and predictions are made on a group of images. In this function we calculate the distances of the image *x* and compare it with all the other images in the dataset, to find the element that stands out the most in the *k* neighbouring elements. The second function [def predict(self, x):](https://github.com/mathisdesaulty/MathisDESAULTY/blob/c3692891743d930938445ab2cc248ce295faecb1/Object/k_nn_mnist.py#L30-L37), allows the prediction of the first, but on all the elements of a list. 
As far as the test function is concerned, I'm still not sure about keeping it in the k-nn, bearing in mind that I've made a test script for the k-nn, and its usefulness is simply to know its success rate depending on the initial data and the number of tests we want to run. 

### K-NN review

After launching the K-NN test function, I realised two things: firstly, the execution time for K-NN is very long, and secondly, the results are not very conclusive with approximately 10% success rate on samples of 200 images and 50 tests.  

## Issue

This was due to the last problem I mentioned. I then decided to send a message to our professor to find out whether my algorithm was bad or whether this was normal. The first conclusion was that many improvements are possible that would drastically reduce the code execution time. Secondly, I was only testing on a very small part of the dataset, which explains the bad predictions, but what explains the bad predictions even more is the fact that the Haussford distance is not totally adapted in the case where I use it. 

## What's next ?

The next steps would therefore be to review all the code that I discussed with the teachers: change the Haussford distance and find optimisations for this K-NN algorithm. The next step would then be to test with different distances: using the average of the distances of the nearest points, the sum of these distances, etc. 