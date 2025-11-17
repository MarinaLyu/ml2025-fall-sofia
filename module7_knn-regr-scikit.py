import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


def main():
    try:
        # Get N (number of points)
        N = int(input("Enter the number of points (N, positive integer): "))
        if N <= 0:
            print("Error: N must be a positive integer.")
            return

        # Get k (number of neighbors)
        k = int(input("Enter the number of neighbors (k, positive integer): "))
        if k <= 0:
            print("Error: k must be a positive integer.")
            return

        if k > N:
            print(f"Error: k ({k}) cannot be greater than N ({N}).")
            return

              points = np.zeros((N, 2))

        print(f"Enter {N} points (x, y) one by one:")
        for i in range(N):
            print(f"Point {i + 1}:")
            x = float(input("  Enter x value (real number): "))
            y = float(input("  Enter y value (real number): "))
            points[i] = [x, y]

            X_train = points[:, 0].reshape(-1, 1)  # Reshape to 2D array for scikit-learn
        y_train = points[:, 1]

        variance = np.var(y_train)
        print(f"\nVariance of labels in training dataset: {variance:.4f}")

            X_pred = float(input("\nEnter X value for prediction: "))

              knn_regressor = KNeighborsRegressor(n_neighbors=k)
        knn_regressor.fit(X_train, y_train)

        X_pred_2d = np.array([[X_pred]])  # Reshape for prediction
        y_pred = knn_regressor.predict(X_pred_2d)

        print(f"\nPredicted Y value for X = {X_pred}: {y_pred[0]:.4f}")

        distances, indices = knn_regressor.kneighbors(X_pred_2d)
        print(f"\nThe {k} nearest neighbors:")
        for i, idx in enumerate(indices[0]):
            print(
                f"  Point {idx + 1}: X = {X_train[idx][0]:.4f}, Y = {y_train[idx]:.4f} (distance: {distances[0][i]:.4f})")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
