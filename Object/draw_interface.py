"""
This module provides a graphical interface for drawing 
and recognizing digits using a K-Nearest Neighbors (KNN) classifier.
Classes:
    DrawInterface: A class that creates a drawing interface using Tkinter 
    and processes the drawn image to predict digits using a KNN classifier.
Methods:
    __init__(self, root):
        Initializes the drawing interface with a Tkinter root window.
    save_image(self):
        Saves the drawn image, preprocesses it, and predicts the digit using the KNN classifier. 
        Displays the drawn image and its nearest neighbors.
    center_image_in_black_background(self, img):
        Centers the drawn image in a black background to match the MNIST format.
    paint(self, event):
        Draws on the canvas when the mouse is dragged.
"""

import tkinter as tk
from PIL import Image, ImageOps, ImageGrab
import numpy as np
import matplotlib.pyplot as plt
from Object.k_nn_mnist import KNNClassifierMINST
from Object.image_user import ImageUser


class DrawInterface:
    """Interface for drawing and recognizing digits using KNN classifier."""    
    def __init__(self, root):
        """Initialize the drawing interface."""
        self.root = root
        self.root.title("Interface de Dessin")
        self.canvas = tk.Canvas(self.root, bg="white", width=500, height=500)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.save_button = tk.Button(self.root, text="Sauvegarder", command=self.save_image)
        self.save_button.pack()
        self.old_x = None
        self.old_y = None
        self.knn = KNNClassifierMINST(k=5, size=2000)

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
        predictions = self.knn.predict_return_neighbors([binarized_image], "hausdorff_sum")
        neighbors = predictions[0][1]

        fig, axes = plt.subplots(1, self.knn.k + 1, figsize=(10, self.knn.k + 1))
        axes[0].imshow(binarized_image, cmap='gray')
        axes[0].set_title("Your Image")
        axes[0].axis('off')

        for i, neighbor_idx in enumerate(neighbors):
            neighbor_image = self.knn.images[neighbor_idx]
            axes[i + 1].imshow(neighbor_image, cmap='gray')
            axes[i + 1].set_title(f"Neighbor {i+1}")
            axes[i + 1].axis('off')

        plt.show()

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
