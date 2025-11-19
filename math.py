def calculate_mean(values):
    return sum(values) / len(values)

def calculate_median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

def calculate_variance(values, mean):
    return sum((x - mean) ** 2 for x in values) / len(values)

def calculate_std_dev(variance):
    return variance ** 0.5

def main():
    n = int(input("How many values do you want to enter? "))

    values = []
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

if __name__ == "__main__":
    main()