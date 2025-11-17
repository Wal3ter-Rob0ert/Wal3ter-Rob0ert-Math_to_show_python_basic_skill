import math

def main():
    n = int(input("How many values do you want to enter? ")) 

    values = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        values.append(num)

    import statistics

    avg = statistics.mean(values)
    median = statistics.median(values)
    variance = statistics.pvariance(values)
    std_dev = statistics.pstdev(values)

    print(f"Average: {round(avg)}")
    print(f"Median: {round(median)}")
    print(f"Variance: {round(variance)}")
    print(f"Standard Deviation: {round(std_dev)}")

if __name__ == "__main__":
    main()