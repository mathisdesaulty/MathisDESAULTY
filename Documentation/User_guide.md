# User Guide

## Introduction
Welcome to the AlgoAndAILab User Guide. This document will help you understand how to use the various features and functionalities of the AlgoAndAILab project.

## Table of Contents
1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Features](#features)
4. [Contact](#contact)

## Installation
To install the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mathisdesaulty/AlgoAndAILab_MathisDESAULTY.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AlgoAndAILab_MathisDESAULTY
    ```
3. Create a virtual envirronement:
    ```bash
    python3 -m venv yenv
    ```
4. Activate the virtual envirronement:
       Linux : 
        ```bash
        source yenv/bin/activate
        ```
       Windows:
       ```bash
        yenv\Scripts\activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    If your on MacOs/Linux, install tkinter with:
   ```bash
    sudo apt-get install python3-tk
    ```

## Getting Started
After installation, you can start the application by running:

You can run the main with the executable *main.exe*. 

Or with theses commands:

1. Run the main script:
    ```bash
    python main.py
    ```
    The main launch can sometimes take a little time.
2. Run the performance test:
    ```bash
    python performance_test.py
    ```


## Features
- **Image prediction**: (main.py and executable) allows you to draw your number and have it predicted by the MNIST dataset. This programme takes some time because it compares the image with a MNIST dataset of 10,000 images.
- **Performance test**: (main.py and executable) allows you to see the performance where you can choose: k, number of tests, number of images in the dataset used.
- **Terminal Performance test**: (performance.py) allows you to run performance tests in the terminal with k, the number of tests and the size of the dataset chosen at runtime.
- **K-NN class**: You can use this class for your own project, maximum optimisation has been done. If you want to use it, I leave you with the code [here](https://github.com/mathisdesaulty/MathisDESAULTY/blob/8b1f675fb66de66af5a47e26466f32d37e88b921/Object/k_nn_mnist.py#L10), all the docstrings are complete and allow you to understand the project.

## Contact
For further assistance, contact me at mathis.desaulty@gmail.com.

Thank you for using KNN-MNIST! 