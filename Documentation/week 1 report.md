# Weekly Report n°1

## Introduction

Having spent 6 hours on the project this first week, I didn't want to start coding straight away. In fact, I preferred to devote this week to finding a project and understanding how to set it up. So during this week I was able to do the following steps.

## Finding the project

The first step was to find the project, my first idea was to turn to visualisation with machine learning on objects/writings because these are concepts that interest me. 
I quickly turned to the well-known MNIST dataset, filled with images of handwritten numbers. After a lot of thought and discussions with my teachers, I decided to use the k-nearest neighboors algorithm to be able to use this dataset. 

## Project plan

### Using the dataset

The first step in this project will be to take the dataset and put it into the desired form so that I can use it on the k-nn. This means a limit of pixels that will be either black or white.

### Setting up the K-NN

Once the dataset is in the desired format, we need to set up the K-NN algorithm to use it. One of the main components of K-NN is the choice of the number of k's, which can be quite high given the number of elements in the dataset. This is a good idea when reducing the size of images, as we will lose some data. The second major component is the choice of distance used.

### Testing different distances

We'll start by trying out the Hausdorff distance and the D23 Measure, which have been suggested to us by our teachers and which are suitable for this project. We'll then be able to see the difference in execution time and the percentage of success of these two distances in order to compare them. Later on in the project, we could also try using other distances to compare the performance of each.

### An exchange with the user? 

As a last step, if the project is already finished and we still have time, one of my last ideas would be to create a user interface that would allow the user to draw his own number and to return what the K-NN would return for this image. 

## Tools used

As I said in the Specification Document, I'm going to use the Python programming language with the numpy module to be able to use matrices. During the week I discovered the following tools: *poetry* for dependencies and managing your project in Python, *pylint* for error detection and finally *unittest* and *coverage* for covering all the code I'm going to produce over the next few weeks. 

## What's next ? 

Over the next week, I'm going to learn how to use these tools and start writing lines of code. As I said earlier, the first step is to understand how to use the MNIST dataset and put it in the right format for using K-NN. 
