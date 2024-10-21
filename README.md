# AlgoAndAILab_K-NN_MNIST
Project for the "Algorithms and AI Lab" Course of the 1st period (2024-2025).

## Description

This project allows you to use the MNIST dataset to predict images of numbers that you can draw yourself using the following information.
    
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mathisdesaulty/MathisDESAULTY.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MathisDESAULTY-main
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    If your on MacOs/Linux, install tkinter with:
   ```bash
    sudo apt-get install python3-tk
    ```

## Usage

You can run the main with the executable *main.exe*.

Or with theses commands:

1. Run the main script to start the prediction:
    ```bash
    python main.py
    ```
2. Run the performance test:
    ```bash
    python performance_test.py
    ```

## How does the programme work? 

When you launch the main programme, you will see an image page appear in which you can draw your number so that the programme can try to predict it. You can see how the programme performs by looking at the performance test next to the prediction buttons. If you try to predict several times, you may be able to see that the performance tests are very optimistic. The problem is that the MNIST dataset may be very large, but most of the numbers are written the same. If you have a way of drawing the numbers that is a little outside the dataset, the predictions will be poor. All the User informations can be find in [User Guide](https://github.com/mathisdesaulty/MathisDESAULTY/blob/main/Documentation/User_guide.md#user-guide).
