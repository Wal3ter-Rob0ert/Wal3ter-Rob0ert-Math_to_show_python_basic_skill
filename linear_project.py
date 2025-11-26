from typing import Optional
import sys
import numpy as np

#!/usr/bin/env python3
"""
linear_project.py

Simple linear regression (ordinary least squares) implementation.
Usage:
    - Import LinearRegression in your project.
    - Run this file to see a small self-test with synthetic data.
    - Optionally supply a CSV file path as the first CLI argument:
            CSV should be numeric, features in columns, target as the last column.
"""



class LinearRegression:
        """Ordinary Least Squares linear regression (supports multiple features)."""

        def __init__(self, fit_intercept: bool = True):
                self.fit_intercept = fit_intercept
                self.coef_: Optional[np.ndarray] = None  # shape (n_features,) or (n_targets, n_features)
                self.intercept_: Optional[np.ndarray] = None

        def _prepare_X(self, X: np.ndarray) -> np.ndarray:
                X = np.asarray(X, dtype=float)
                if X.ndim == 1:
                        X = X.reshape(-1, 1)
                if self.fit_intercept:
                        ones = np.ones((X.shape[0], 1), dtype=float)
                        X = np.hstack([ones, X])
                return X

        def fit(self, X: np.ndarray, y: np.ndarray):
                """
                Fit model to X, y using the Moore-Penrose pseudo-inverse.
                X: array-like (n_samples, n_features)
                y: array-like (n_samples,) or (n_samples, n_targets)
                """
                Xp = self._prepare_X(X)
                y = np.asarray(y, dtype=float)
                # Ensure y is 2D (n_samples, n_targets) for consistent math
                if y.ndim == 1:
                        y = y.reshape(-1, 1)

                # Solve for parameters using pseudo-inverse
                params = np.linalg.pinv(Xp) @ y  # shape (n_params, n_targets)

                if self.fit_intercept:
                        self.intercept_ = params[0].reshape(-1)
                        self.coef_ = params[1:].reshape(params.shape[0] - 1, -1).T  # shape (n_targets, n_features)
                else:
                        self.intercept_ = np.zeros(params.shape[1])
                        self.coef_ = params.T  # shape (n_targets, n_features)

                # If single target, flatten coef and intercept
                if self.coef_.shape[0] == 1:
                        self.coef_ = self.coef_.reshape(-1)
                        self.intercept_ = float(self.intercept_)

                return self

        def predict(self, X: np.ndarray) -> np.ndarray:
                X = np.asarray(X, dtype=float)
                if X.ndim == 1:
                        X = X.reshape(-1, 1)
                if self.fit_intercept:
                        return (X @ self.coef_.T) + self.intercept_
                else:
                        return X @ self.coef_.T

        def mean_squared_error(self, X: np.ndarray, y: np.ndarray) -> float:
                y = np.asarray(y, dtype=float)
                preds = self.predict(X).squeeze()
                y = y.squeeze()
                return float(np.mean((preds - y) ** 2))

        def r2_score(self, X: np.ndarray, y: np.ndarray) -> float:
                y = np.asarray(y, dtype=float).squeeze()
                preds = self.predict(X).squeeze()
                ss_res = np.sum((y - preds) ** 2)
                ss_tot = np.sum((y - np.mean(y)) ** 2)
                return float(1 - ss_res / ss_tot) if ss_tot != 0 else 0.0


def load_csv_features_target(path: str, delimiter: str = ","):
        """Load numeric CSV where the last column is the target."""
        data = np.loadtxt(path, delimiter=delimiter)
        if data.ndim == 1:
                # Single row
                X = data[:-1].reshape(1, -1)
                y = np.array([data[-1]])
        else:
                X = data[:, :-1]
                y = data[:, -1]
        return X, y


def _demo():
        # Synthetic data: y = 3 + 2*x1 - x2 + noise
        rng = np.random.default_rng(0)
        n = 200
        x1 = rng.normal(0, 1, n)
        x2 = rng.normal(1, 2, n)
        noise = rng.normal(0, 0.5, n)
        X = np.column_stack([x1, x2])
        y = 3 + 2 * x1 - 1 * x2 + noise

        model = LinearRegression(fit_intercept=True)
        model.fit(X, y)
        print("Intercept:", model.intercept_)
        print("Coefficients:", model.coef_)
        print("MSE:", model.mean_squared_error(X, y))
        print("R^2:", model.r2_score(X, y))


if __name__ == "__main__":
        if len(sys.argv) > 1:
                path = sys.argv[1]
                try:
                        X, y = load_csv_features_target(path)
                except Exception as e:
                        print("Failed to load CSV:", e)
                        sys.exit(1)
                model = LinearRegression()
                model.fit(X, y)
                print("Fitted model from", path)
                print("Intercept:", model.intercept_)
                print("Coefficients:", model.coef_)
                print("MSE:", model.mean_squared_error(X, y))
                print("R^2:", model.r2_score(X, y))
        else:
                _demo()