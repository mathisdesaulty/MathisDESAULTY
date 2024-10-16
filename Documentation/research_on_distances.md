# k-Nearest Neighbors (k-NN)

The **k-Nearest Neighbors (k-NN)** algorithm is a simple, non-parametric method used for classification and regression tasks. In both cases, the idea is to find the \( k \) closest data points (neighbors) to a target point, based on a distance metric (commonly Euclidean distance). The algorithm then makes predictions based on the majority class (in classification) or the average value (in regression) of these neighbors.

## How k-NN Works:
1. **Distance Calculation**: The algorithm calculates the distance between the target point and all other points in the dataset. Common distance metrics include:
   - Euclidean distance
   - Manhattan distance
   - Minkowski distance
   - Cosine similarity

2. **Neighbor Selection**: Once distances are calculated, the algorithm selects the \( k \) closest points (neighbors).

3. **Prediction**:
   - For classification: The algorithm predicts the most common class among the \( k \) neighbors.
   - For regression: The prediction is the average of the values of the \( k \) neighbors.

The choice of distance metric is crucial to the performance of k-NN, as it directly impacts which neighbors are selected.

In image comparison tasks, like those described in this document, distance metrics (such as the **Hausdorff Distance** or **Hausdorff_sum Distance**) are often used to measure the similarity or difference between sets of features (points) in two images. This concept is analogous to how distances are used in k-NN to find neighbors, though in a broader and more complex context.

---

# 1. Hausdorff Distance

The Hausdorff distance between two sets of points \( A \) and \( B \) is defined as:

$$
d_H(A, B) = \max \left( \max_{a \in A} \min_{b \in B} d(a, b), \max_{b \in B} \min_{a \in A} d(b, a) \right)
$$

This is calculated by the `hausdorff_distance` method in the code.

---

# 2. Hausdorff_sum Distance

This version of the Hausdorff distance sums the minimal distances between points from both sets, in both directions:

$$
d_{H\_sum}(A, B) = \sum_{a \in A} \min_{b \in B} d(a, b) + \sum_{b \in B} \min_{a \in A} d(b, a)
$$

This corresponds to the `hausdorff_distance_sum` method.

---

# 3. Distance d22

The \( d_{22} \) distance between two images is defined as the maximum of the \( d_6 \) distances calculated in both directions:

$$
d_{22}(A, B) = \max \left( d_6(A, B), d_6(B, A) \right)
$$

It is calculated by the `distance_d22` method.

---

# 4. Distance d23

The \( d_{23} \) distance is defined as the average of the \( d_6 \) distances calculated in both directions:

$$
d_{23}(A, B) = \frac{d_6(A, B) + d_6(B, A)}{2}
$$

It is calculated by the `distance_d23` method.

---

# Note on the d6 Distance

The \( d_6 \) distance is used as the base for both the \( d_{22} \) and \( d_{23} \) distances. It is calculated by taking the sum of the minimal distances between each point in one set to the other, normalized by the number of points:

$$
d_6(A, B) = \frac{\sum_{a \in A} \min_{b \in B} d(a, b)}{|A|}
$$
