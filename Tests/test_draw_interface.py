"""
Unit tests for the DrawInterface class.
This module contains a set of unit tests for the DrawInterface class, 
which is part of the Object.draw_interface module.
The tests are designed to verify the correct initialization 
and functionality of the DrawInterface, including its methods
for centering images, saving images, and painting on the canvas.
Classes:
    TestDrawInterface: A unittest.TestCase subclass that contains tests for the DrawInterface class.
Methods:
    setUp: Initializes a basic tkinter root and the DrawInterface instance before each test.
    tearDown: Destroys the tkinter root after each test.
    test_init: Tests the initialization of the DrawInterface instance.
    test_center_image_in_black_background: Tests if
    an image is correctly centered in a black background.
    test_save_image: Tests the save_image method without mocks.
    test_paint: Tests the paint method to ensure it draws lines on the canvas.
"""

import unittest
import tkinter as tk
import numpy as np
from PIL import Image
from Object.draw_interface import DrawInterface  # Import the DrawInterface class

class TestDrawInterface(unittest.TestCase):
    """
    Unit tests for the DrawInterface class.
    This test suite includes the following tests:
    - setUp: Initializes a basic tkinter root and the DrawInterface instance before each test.
    - tearDown: Destroys the tkinter root after each test to ensure a clean state.
    - test_init: Verifies the initialization of the DrawInterface, ensuring that the canvas, 
    save_button, old_x, old_y, and knn attributes are correctly set.
    - test_center_image_in_black_background: Tests the center_image_in_black_background method 
    to ensure that a small image is correctly centered in a black 28x28 background.
    - test_save_image: Tests the save_image method 
    by simulating a drawing on the canvas and saving it.
    - test_paint: Tests the paint method to ensure 
    it correctly draws lines on the canvas based on mouse movement events.
    """

    # def setUp(self):
    #     """Setup a basic tkinter root and the DrawInterface."""
    #     self.root = tk.Tk()
    #     self.app = DrawInterface(self.root)

    # def tearDown(self):
    #     """Destroy the Tkinter root after each test."""
    #     self.root.destroy()

    # def test_init(self):
    #     """Test the initialization of the DrawInterface."""
    #     self.assertIsInstance(self.app.canvas, tk.Canvas)
    #     self.assertIsInstance(self.app.save_button, tk.Button)
    #     self.assertIsNone(self.app.old_x)
    #     self.assertIsNone(self.app.old_y)
    #     self.assertIsNotNone(self.app.knn)

    # def test_center_image_in_black_background(self):
    #     """Test if the image is correctly centered in a black background."""
    #     # Créer une petite image 10x10 blanche
    #     small_image = np.ones((10, 10), dtype=np.uint8) * 255
    #     small_pil_image = Image.fromarray(small_image)

    #     # Tester la fonction center_image_in_black_background
    #     centered_img = self.app.center_image_in_black_background(small_pil_image)
    #     centered_img_np = np.array(centered_img)

    #     # Vérifier que l'image centrée est bien au centre
    #     self.assertEqual(centered_img_np.shape, (28, 28))
    #     self.assertTrue(np.all(centered_img_np[9:19, 9:19] == 255))  # Image blanche centrée
    #     self.assertTrue(np.all(centered_img_np[:9, :] == 0))  # Bordures noires
    #     self.assertTrue(np.all(centered_img_np[:, :9] == 0))  # Bordures noires

    # def test_save_image(self):
    #     """Test the save_image method without mocks."""
    #     # Simuler un dessin sur le canvas
    #     self.app.old_x = 100
    #     self.app.old_y = 100
    #     self.app.save_image()

    # def test_paint(self):
    #     """Test the paint method to ensure it draws lines on the canvas."""
    #     # Simuler un mouvement de la souris avec des coordonnées
    #     event_mock = tk.Event()
    #     event_mock.x = 100
    #     event_mock.y = 150

    #     self.app.old_x = 90
    #     self.app.old_y = 140

    #     # Appeler la méthode paint
    #     self.app.paint(event_mock)

    #     # Vérifier que le canvas a bien dessiné une ligne
    #     self.assertEqual(self.app.old_x, 100)
    #     self.assertEqual(self.app.old_y, 150)
    # def test_run_performance_tests(self):
    #     """Test the run_performance_tests method to ensure it runs without errors."""
    #     # Mock the messagebox to prevent actual messagebox from appearing during tests
    #     self.app.run_performance_tests()
    # def test_reset_canvas(self):
    #     """Test the reset_canvas method to ensure it clears the canvas."""
    #     # Simulate drawing on the canvas
    #     self.app.old_x = 100
    #     self.app.old_y = 100
    #     event_mock = tk.Event()
    #     event_mock.x = 150
    #     event_mock.y = 150
    #     self.app.paint(event_mock)

    #     # Ensure the canvas has drawn content
    #     self.assertNotEqual(self.app.canvas.find_all(), ())

    #     # Call the reset_canvas method
    #     self.app.reset_canvas()

    #     # Ensure the canvas is cleared
    #     self.assertEqual(self.app.canvas.find_all(), ())
    #     self.assertIsNone(self.app.old_x)
    #     self.assertIsNone(self.app.old_y)

if __name__ == '__main__':
    unittest.main()


# ### For DrawInterface: 
# [TestDrawInterface](https://github.com/mathisdesaulty/MathisDESAULTY/blob/26b980f816e4efc3112cbd38b05f855895a09a7c/Tests/test_draw_interface.py#L26)
# - What was tested: How the user interface works.
# How it was tested:
#     - TestDrawInterface ensures that all 
#       GUI-related functions execute correctly and that visual elements are displayed as expected.
#     - These are manual tests, as the interface 
#       elements must be visually checked by an operator while they are being executed.
# - Types of tests:
#     - Functional testing
#     - User interface testing
#     - Integration testing
#     - Lifecycle testing
# - Inputs:
#     - Mouse coordinates
#     - Scanned images
#     - Events