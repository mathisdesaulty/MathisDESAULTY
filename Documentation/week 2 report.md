# Week 2 Report

## Tasks of the week

### Learning new modules 
The first stage of the week was to familiarise myself with the various new modules that I wasn't familiar with:
- Poetry: this Python module is used to manage my project's dependencies. Personally, I don't think it's one of the most important modules I could use, especially on this project in a short space of time. However, I still preferred to integrate it into my project because I realise that it could be interesting for longer projects that require regular maintenance with many packages in use.
- Pylint: this module lets you give your code a grade and tell whether it's of good quality. Having done very few projects, especially in Python, I know very little about professional ways of commenting on code. This tool solves the problem by giving me a grade and telling me what to change in the code.
- Unittest: this last module allows you to create simple-to-use test files. This will be extremely useful for tests after functions have been created, but also after certain functions have been modified, to check that my modifications haven't altered anything. 

### Start Coding
My aim this week was to start coding slowly and gradually learn to use all the elements we've just talked about. Which I did, but I was able to make progress on several parts of the project:

- Binarising images: since I had to use images on K-NNs, the first step was to ensure that these images could be used by the distance formulae we'll be talking about next. To binarise the images I came up with a simple code: as we can see in [this code](../Object/image_user.py),for the binarisation of images, I preferred to set a threshold as a parameter that the user of the function can change at any time, so all pixels below this light threshold become 0 and the others 1. In the link I gave just above you can see that it's not 1 and 0 but True and False, this change was made in the last day after seeing the review by our teachers, we'll talk about it later.

- Create a mathematical tool: the second major step in this week's project was to create a mathematical tool. [math_tool](../Object/math_tool.py) to calculate a Haussdorf distance, which I completed by calculating the distances between all the coordinates. So I had to do some research on this first distance, which won't be the last. What's interesting about this project is that there are several objects and several functions for each of them that fit together simply and that if we have the slightest change it doesn't take long to change.

- Writing tests: while I was writing this code, after each function I wrote, I started writing tests using unittest. I would then write simple tests without complex images, which would ensure that my code worked as I wanted it to.

- Using pylint: when writing objects and tests, I used pylint in particular and took into account everything it told me about how to write my code and what I could improve to have clean code. 

- Modifications: after seeing the teacher's feedback on the first week, I had a few things I could change. Firstly, the images were no longer in binary but in Boolean and I'm going to have to take the time to optimise Haussford's distancing and complete it by looking at the nearest pixels to take as little time as possible. In particular, I think I can look to see if one of the pixels in a positive image is positive for the other and also look at the 8 around them. 
