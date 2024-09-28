# Research on distances
This research allows me to know which distances to test and which might work best to get the most convincing results. 
They are divided into two different types of distance, for greyscale images and for binarised images.

## Binarised images
* Hamming's distance: $$ d_H(A, B) = \sum_{i=1}^{n} |A_i - B_i|$$ 
Faster than Haussdorff distance, simple for binarised images.

* Jaccard's distance:
$$
d_{Jaccard}(A, B) = 1 - \frac{|A \cap B|}{|A \cup B|}
$$
More expensive to calculate than Hamming distance, but provides a more robust measure of similarity.

* Soren-Dice's distance: 
$$
d_{Dice}(A, B) = 1 - \frac{2 |A \cap B|}{|A| + |B|}
$$
Jaccard's distance, with more emphasis on sets.

## Grey scale images

- D22 distance:
$$
D_{22}(A, B) = \sqrt{\sum_{i,j} (A_{i,j} - B_{i,j})^2}
$$
Sensitive to small variations and to the distribution of pixel values.
- D23 distance:
$$
D_{23}(A, B) = \left( \sum_{i,j} |A_{i,j} - B_{i,j}|^3 \right)^{\frac{1}{3}}
$$To accentuate the impact of higher values.

