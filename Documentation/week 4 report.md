# Week 4 report

Approximatively 8 hours this.

## What I've learned

This week, most of my work was not research but rather reflection on work already produced. My only research was on variants of Haussdorf's method for calculating the distance between two binarised images.

## What I did this week

### Performance tests and solve problems

So the first thing this week was to see what the changes from last week's work had done to the performance of my K-NN algorithm. I was very surprised by the results, firstly the execution time was divided by 2 with the fact of only looking from one image to another, but the results were still just as mediocre. Only 10% of the results were good and the execution time was still just as long. The second problem was that changing the distance by removing the square root and directly using the power didn't change anything in terms of either performance or execution time. 
I realised the next day that math_tool wasn't actually doing what I wanted it to do. So I took a long time during the week to fix math_tool.
The old tests I ran can be found here [ici](https://github.com/mathisdesaulty/MathisDESAULTY/commit/7ebe17ff4b94889294c441340712eacecfb3c91a). However I didn't keep their outputs.

### Fixing math_tool 

The problem behind math tool was that the function never passed through the Euclidean distance between two points. Here's how the method works [calculate_one_way_distance](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L52-L71), to determine the Haussdorf distance between two binarised images :
- The function checks that the two points are not the same in the function: [same_value](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L39-L50).
- It looks at the neighbours with the: [neighboors_positive](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L14-L37).
- Then, if in both cases we do not receive a positive response, we make the [euclidian distance squared](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L67-L68).
The problem with this function was that [same_value](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L39-L50) was doing too much work and wasn't simply looking at the same point in the two images. As a result, it kept seeing the same value over and over again and we were getting very strange distances.
So I had to modify all the math_tool methods and redo more complex tests than the first ones to check if it really worked.

### New methods of distance calcul

Since I don't yet have several distance methods for comparing performance and execution time. The teacher gave me the idea of modifying the Haussdorf distance so that instead of taking the maximum of the minimum distances, I would take the sum of the distances, which would then take into account all the points and not just the furthest point, which would jeopardise the algorithm's performance.
I was then able to do [this function](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L115-L132) using [this function](https://github.com/mathisdesaulty/MathisDESAULTY/blob/e2eac061c0fbe3e562b4a9961e212f77b389d741/Object/math_tool.py#L93-L112) which calculates the sum of distances using the functions of neighbours with the same values.
I was then able to change the K-NN agorithm so that I could choose between the two functions and compare them. 

### Performance tests

We then have two functionalities that we can test. 
So I was able to see the performance of my two distances and compare them, on several tests I've already realised that the change in the Haussdorf distance simply by removing the square root saved precious seconds compared with the first test. But I've also been able to see that performance is now more than qualitative, more than 95% of my tets work with this first distance on a small dataset (for execution time reasons).
Compared with the second distance we're using, i.e. the modified Haussdorf distance, we can see that the execution time is longer, mainly due to the addition but also to the fact of keeping the square root for this function because otherwise distances that are too high would have too big an impact. However, this function gives us 100% success most of the time, with a few exceptions. 
The results are therefore very conclusive.

## Issues

The biggest problem after trying all this is the execution time, even with optimisation, we can see that it takes time and that we can't then run tests that are too consistent. This would be important if we wanted to do more accurate tests than on a dataset of just a few hundred elements. 

## What's next ?

The next step is therefore to try other distances such as D23, which is in the project description. If the execution time problems aren't solved with these other distances, we'll then have to look at optimisation to carry out tests on larger datasets. 