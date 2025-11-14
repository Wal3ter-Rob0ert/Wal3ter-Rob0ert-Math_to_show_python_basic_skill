import math

def main():
    n = int(input("How many values do you want to enter? ")) 

    values = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        values.append(num)

    avg = sum(values) / n

    values_sorted = sorted(values)
    if n % 2 == 1:
        median = values_sorted[n // 2]
    else:
        median = (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2

    variance = sum((x - avg) ** 2 for x in values) / n

    std_dev = math.sqrt(variance)

    print(f"Average: {round(avg)}")
    print(f"Median: {round(median)}")
    print(f"Variance: {round(variance)}")
    print(f"Standard Deviation: {round(std_dev)}")

if __name__ == "__main__":
    main()