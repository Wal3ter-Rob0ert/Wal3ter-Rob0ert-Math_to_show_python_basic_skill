import math 
import sys

def read_int(pormpt):
    while True:
        try:
            n = int(input(pormpt))
            if n <= 0:
                print("Need 2+ points")
            else:
                return n
        except ValueError:
                print("Invalid integer, enter an integer value")

def read_float(prompt):
     while True:
          try:
                 return float(input(prompt))
          except ValueError:
                print("Invalid number, enter a numeric value")

def linear_regession(X, Y):
     n = len(X)
     mean_x = sum(X) / n
     mean_y = sum(Y) / n

     num = sum ((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
     den = sum ((X[i] - mean_x) ** 2 for i in range(n))

     if den == 0:
          m = 0.0
     else: 
          m = num / den


     b = mean_y - m * mean_x
     return m, b

def pearson_r(X, Y):
     n = len(X)
     mean_x = sum(X) / n
     mean_y = sum(Y) / n

     num = sum ((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
     den_x = (sum((X[i] - mean_x) ** 2 for i in range(n))) ** 0.5
     den_y = (sum((Y[i] - mean_y) ** 2 for i in range(n))) ** 0.5

     if den_x == 0 or den_y == 0:
          return 0.0

     return num / (den_x * den_y)

def main():
     print("Linear Regression + Pearson Tool")

     n = read_int("Count: ")
     if n < 2:
          print("Need 2+ points")
          sys.exit(0)

     Y = []
     for i in range(n):
          y = read_float(f"Y[{i}]: ")
          Y.append(y)

     X = list(range(n))

     m, b = linear_regession(X, Y)
     r = pearson_r(X, Y)   

     print(f"Linear Regression: Y = {m:.6f} * X + {b:.6f}")
     print(f"Pearson Correlation Coefficient: {r:.10f}")

if __name__ == "__main__":
    main()