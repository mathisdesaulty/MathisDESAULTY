"""Module for drawing and recognizing digits using KNN classifier."""

import time
import threading
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageOps, ImageGrab
import numpy as np
import matplotlib.pyplot as plt
from Object.k_nn_mnist import KNNClassifierMNIST
from Object.image_user import ImageUser


class DrawInterface:
    """Interface for drawing and recognizing digits using KNN classifier."""

    def __init__(self, root):
        """Initialize the drawing interface."""
        self.root = root
        self.root.title("Drawing Interface")

        # Configure grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create label
        self.label = tk.Label(self.root, text="Write your number to predict!")
        self.label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Create canvas for drawing
        self.canvas = tk.Canvas(self.root, bg="white", width=500, height=500)
        self.canvas.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
        self.canvas.bind("<B1-Motion>", self.paint)

        # Create buttons
        self.save_button = tk.Button(self.root, text="Predict number", command=self.save_image)
        self.save_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.test_button = tk.Button(self.root, text="Run Performance Tests",
                                     command=self.open_performance_test_window)
        self.test_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_canvas)
        self.reset_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        # Initialize drawing variables
        self.old_x = None
        self.old_y = None

        # Initialize KNN classifier
        self.knn = KNNClassifierMNIST(k=5, size=10000)

    def open_performance_test_window(self):
        """Open a new window to set parameters for performance tests."""
        test_window = tk.Toplevel(self.root)
        test_window.title("Set Performance Test Parameters")

        # Number of tests
        tk.Label(test_window, text="Number of Tests:").grid(row=0, column=0, padx=5, pady=5)
        tests_number_entry = tk.Entry(test_window)
        tests_number_entry.grid(row=0, column=1, padx=5, pady=5)
        tests_number_entry.insert(0, "10")

        # Dataset size
        tk.Label(test_window, text="Dataset Size:").grid(row=1, column=0, padx=5, pady=5)
        size_entry = tk.Entry(test_window)
        size_entry.grid(row=1, column=1, padx=5, pady=5)
        size_entry.insert(0, "1000")

        # k (number of neighbors)
        tk.Label(test_window, text="k (Number of Neighbors):").grid(row=2, column=0, padx=5, pady=5)
        k_entry = tk.Entry(test_window)
        k_entry.grid(row=2, column=1, padx=5, pady=5)
        k_entry.insert(0, "5")

        # Run button
        run_button = tk.Button(test_window, text="Run Tests",
                               command=lambda: self.run_performance_tests(tests_number_entry,
                                                                          size_entry,
                                                                          k_entry, test_window))
        run_button.grid(row=3, column=0, columnspan=2, pady=10)

    def run_performance_tests(self, tests_number_entry, size_entry, k_entry, test_window):
        """Run performance tests based on user input."""
        try:
            tests_number = int(tests_number_entry.get())
            size = int(size_entry.get())
            k = int(k_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the parameters.")
            return

        # Close the test window
        test_window.destroy()

        # Create loading window
        loading_window = tk.Toplevel(self.root)
        loading_label = tk.Label(loading_window, text="Running performance tests... Please wait.")
        loading_label.pack(pady=10)

        # Run the performance tests in a separate thread
        def run_tests_in_thread():
            # Initialize KNN classifier with the user-provided values
            knn = KNNClassifierMNIST(k, size)

            results = []

            # Performance with default metric
            start_time = time.time()
            performance = knn.performance(tests_number)
            end_time = time.time()
            results.append(
                f"Default metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
                           f"Time: {end_time - start_time} seconds")

            # Performance with hausdorff_sum metric
            start_time = time.time()
            performance = knn.performance(tests_number, "hausdorff_sum")
            end_time = time.time()
            results.append(
                f"Hausdorff_sum metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
                           f"Time: {end_time - start_time} seconds")

            # Performance with d22 metric
            start_time = time.time()
            performance = knn.performance(tests_number, "d22")
            end_time = time.time()
            results.append(f"D22 metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
                           f"Time: {end_time - start_time} seconds")

            # Performance with d23 metric
            start_time = time.time()
            performance = knn.performance(tests_number, "d23")
            end_time = time.time()
            results.append(f"D23 metric: Performance: {performance[0]}, Ratio: {performance[1]}, "
                           f"Time: {end_time - start_time} seconds")

            # Close the loading window and show results when done
            def show_results():
                loading_window.destroy()  # Close the loading window
                messagebox.showinfo("Performance Results", "\n".join(results))

            # Ensure the results are shown on the main thread
            self.root.after(0, show_results)

        # Run the tests in a separate thread to avoid blocking the GUI
        threading.Thread(target=run_tests_in_thread).start()

    def save_image(self):
        """Save the drawn image, preprocess it, and predict using KNN classifier."""
        self.canvas.update()
        diff = 40
        x = self.canvas.winfo_rootx() + diff
        y = self.canvas.winfo_rooty() + diff
        x1 = x + self.canvas.winfo_width() - diff
        y1 = y + self.canvas.winfo_height() - diff

        img = ImageGrab.grab(bbox=(x, y, x1, y1))
        img = ImageOps.grayscale(img)
        img = img.resize((28, 28), Image.LANCZOS)
        img = ImageOps.invert(img)
        img = self.center_image_in_black_background(img)

        pixel_data = list(img.getdata())
        pixel_matrix = [pixel_data[i * 28:(i + 1) * 28] for i in range(28)]

        binarized_image = np.array(pixel_matrix, dtype=np.uint8)
        binarized_image = ImageUser.binarize_image(binarized_image, threshold=40)

        self.predict_with_progress(binarized_image)

    def predict_with_progress(self, binarized_image):
        """Predict the digit with a progress bar indication."""
        progress = ttk.Progressbar(self.root, orient="horizontal", length=200,
                                   mode="indeterminate", style="TProgressbar")
        style = ttk.Style(self.root)
        style.configure("TProgressbar", troughcolor='white', background='blue')
        progress.grid(row=3, column=0, columnspan=3, pady=10)
        progress.start()

        def task():
            predictions = self.knn.predict_return_neighbors([binarized_image], "hausdorff_sum")
            neighbors = predictions[0][1]

            def display_results():
                progress.stop()
                progress.grid_forget()

                fig, axes = plt.subplots(1, self.knn.k + 1, figsize=(10, self.knn.k + 1))
                axes[0].imshow(binarized_image, cmap='gray')
                axes[0].set_title("Your Image")
                axes[0].axis('off')

                for i, neighbor_idx in enumerate(neighbors):
                    neighbor_image = self.knn.images[neighbor_idx]
                    axes[i + 1].imshow(neighbor_image, cmap='gray')
                    axes[i + 1].set_title(f"Neighbor {i+1}")
                    axes[i + 1].axis('off')

                messagebox.showinfo("Prediction", f"Predicted digit: {predictions[0][0]}")
                plt.show()

            self.root.after(0, display_results)

        threading.Thread(target=task).start()

    def center_image_in_black_background(self, img):
        """Center the drawing in a black background to match MNIST format."""
        img_np = np.array(img)
        rows = np.any(img_np, axis=1)
        cols = np.any(img_np, axis=0)
        ymin, ymax = np.where(rows)[0][[0, -1]]
        xmin, xmax = np.where(cols)[0][[0, -1]]

        img_cropped = img_np[ymin:ymax+1, xmin:xmax+1]
        new_img = np.zeros((28, 28), dtype=np.uint8)

        y_offset = (28 - img_cropped.shape[0]) // 2
        x_offset = (28 - img_cropped.shape[1]) // 2

        new_img[
            y_offset:y_offset+img_cropped.shape[0],
            x_offset:x_offset+img_cropped.shape[1]] = img_cropped

        return Image.fromarray(new_img)

    def paint(self, event):
        """Draw on the canvas."""
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x,
                                    self.old_y,
                                    event.x,
                                    event.y,
                                    width=5,
                                    fill="black",
                                    capstyle=tk.ROUND,
                                    smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset_canvas(self):
        """Clear the canvas."""
        self.canvas.delete("all")
        self.old_x = None
        self.old_y = None
