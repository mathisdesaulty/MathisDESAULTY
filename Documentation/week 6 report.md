# Week 5 report

12 hours this week

## What I've learned

- Tkinter for the user interface
- PIL for image use
- Make a requirement.txt

## What I did this week

### UI (Performance part and drawing part)

This week, I wanted to concentrate on the element I was missing to make this project communicate with the user. I had the algorithm, but nothing that would allow the user to use this algorithm in a particular way. 
So my first idea was to create a kind of [Tkinter](https://docs.python.org/3/library/tk.html) on which we would have a sort of drawing area where the user could then draw a number and have it predicted by my K-NN algorithm. With the help of the doc and online information, it wasn't very complicated to be able to make the interface, however, what caused me problems was the fact of taking the user's input. So I discovered [ImageGrab](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Object/draw_interface.py#L52) of the PIL module to create a kind of screen of the page. I then took the image, put it in the form of 28 by 28 pixels and binarised it, the rest was pretty straightforward, I just had to create another function in K-NN to get the neighbours as you can see by running the program with the command:

```bash
python3 main.py
```

### Tests

I was then able to [tests](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Tests/test_draw_interface.py#L26) of my user interface, these tests just let me know that everything was running, I did them simply for myself, but as they're not very useful I've put them in the comments because they really take too long to finish and I didn't feel they were necessary for this project. 

### Coverage

One of the things that was missing from this project was the coverage, I've always tried to have clean 10/10 code on pylint and that the tests are always complete, but I was missing a few lines of coverage. For the most part it was just small parameters that I hadn't tested to take into account, so I now have [100% coverage on every classes](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Documentation/Testing.md#L5-L16).

### Requirements

In order to make my programme easier to use, and to ensure that the person trying to test it doesn't run into any module problems, I decided to make a [requirements.txt](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/requirements.txt#L2) which can be used as indicated in the [README.md](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/README.md#L18-L21).

### Testing doc

For this project, we also needed a file to explain the tests, their inputs... Everything in my tests is then just explained [here](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Documentation/Testing.md#L1). You'll find information on how to run my tests, how to run a particular test, and even the coverage of all my tests.

### Neighbors method

For optimisation reasons I have also modified the method [neighbors_positive](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Object/math_tool.py#L35) but above all [generate_neighbors_offsets](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Object/math_tool.py#L11) which calculates all the neighbours we need to look at for a pixel, we calculate the distance directly to avoid doing this in neighbors_positive.

### Implementation document/ Performance test

I then finished the week by writing the implementation document to explain everything in the project. [complexity](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Documentation/Implementation_document.md#L21-L32). But also performance tests as you can see in [this table](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/Documentation/Implementation_document.md#L49-L65). Now you can also run performance tests as shown [here](https://github.com/mathisdesaulty/MathisDESAULTY/blob/0303007a0a458bc5e322f0fae713a84bd682d1d5/README.md#L29-L32)

## Issues

Just some optimisation problems that I'll deal with before the end of the course.

## What's next ?

The project itself is finished, but I can still optimise the distances, so I'm going to look into that. I may also change the UI to make it easier to use, but I'm not sure yet.