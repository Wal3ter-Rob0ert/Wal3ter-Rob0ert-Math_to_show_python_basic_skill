def calculate_mean(values): # Calculate the mean of a list of values
    return sum(values) / len(values)

def calculate_median(values): # Calculate the median of a list of values
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1: # Odd number of elements
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

def calculate_variance(values, mean): # Calculate the variance of a list of values
    return sum((x - mean) ** 2 for x in values) / len(values)

def calculate_std_dev(variance): # Calculate the standard deviation from variance
    return variance ** 0.5      

def main(): # Main function to execute the calculations
    n = int(input("How many values do you want to enter? "))

    values = [] # List to store the input values
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        values.append(num)

    avg = calculate_mean(values)
    median = calculate_median(values)
    variance = calculate_variance(values, avg)
    std_dev = calculate_std_dev(variance)

    print(f"Average: {round(avg)}")
    print(f"Median: {round(median)}")
    print(f"Variance: {round(variance)}")
    print(f"Standard Deviation: {round(std_dev)}")

if __name__ == "__main__": # Ensuring the main function runs only when the script is executed directly
    main() # Calling the main function to start the program