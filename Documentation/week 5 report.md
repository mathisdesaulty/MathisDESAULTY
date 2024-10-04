# Week 5 report

8 hours this week.

## What I've learned

This week I learnt how distances D22 and D23 were created and what they are used for. I then read this [article](https://www.researchgate.net/publication/290011464_Modifications_of_hausdorff_distance_for_object_matching), in which it is explained that there are 6 distances and 4 functions composed of these distances which, when added together, can help us to obtain very precise distances. Distances D22 and D23 use functions f3 and f4 on distance d6, which is simply the average of the minimum distances of each point of image A in image B.

## What I did this week

### Research for other distances

I started the week by doing a little research into the distances I could use. In the last weekly report I talked about the fact that I didn't know how to improve the performance of my algorithm, and one of the only ways I'd found was to change my distance methods. More suitable methods could then lower the execution time of my algorithm but also improve performance.
I then found a number of distances that I won't go into here, but the most interesting seemed to be D22 and D23, proposed by the professor earlier.

### Upgrades

#### Numpy to list

After talking to the teacher, I realised that my code was slow for several reasons. One of the most important was the use of Numpy arraylists, when I could just use simple Lists of Lists. I then had to make changes to most of my code. This took a bit of time because all my data was in the form of Numpy arraylists and I had to change a number of things, for example: [Binarize the image](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Object/image_user.py#L39-L45) which was then done very simply with Numpy in one line.

#### Neighbors functions and performances acceleration

The second observation was that the images are made of 28 by 28 pixels. Searching in all the pixels when you want to look for the nearest one, most of the time, is what lengthens the code. For the last 2 weeks we've been looking at the neighbours first, before going round all the points in the other image. By neighbours we mean only the first circle around the point. But suppose we could change that to look at 4 circles around the point, then we'd have a lot more points to check but we'd be almost certain to find one inside. So I modified [neighbors_positive](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Object/math_tool.py#L32-L57) so that we can set the number of circles we want to check around our point as a parameter, this function now returns a tuple, consisting of a boolean to indicate whether we've found it and a tuple of the nearest neighbour's coordinates.

### Distance D22/23

Now that I've got an algorithm that works, I want to look at the best distances I could use. So this week I set up distances D22 and D23, as well as distance D6 (which is compulsory for these two distances). You can find these distances in this [article](https://www.researchgate.net/publication/290011464_Modifications_of_hausdorff_distance_for_object_matching). Vous pouvez revenir [there](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Documentation/week%205%20report.md#L7) where I quickly explain what these distances are without going into detail.
I was then able to do some tests to find out which distances were the best. Distances D22 and D23 are close to the Hausdorff distance with the sum, the results are almost the same but a little longer and more efficient for distances d22 and d23. 

### Peer Review 

One of the tasks this week was to do a peer review of one person's work. The work focused mainly on reading the code and looking at what was good but also what needed to be improved in the code. 

## Issues

This week has mainly been about sorting things out, so for the moment I don't have any other problems.

## What's next ?    

The next step will be to create a user interface. My idea would be to make a tkinter interface where the person could enter a number and the algorithm could try to predict it.