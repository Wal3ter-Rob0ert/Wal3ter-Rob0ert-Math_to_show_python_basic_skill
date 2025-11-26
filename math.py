def mean(numbers): # Calculate the mean (average) of a list of numbers
    total = 0
    for value in numbers:
        total = total + value
    return total / len(numbers)


def median(numbers): # Calculate the median of a list of numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers) 
    middle_index = n // 2 # Integer division

    if n % 2 == 1: # Odd number of elements
        return sorted_numbers[middle_index] # Middle element
    else: # Even number of elements
        left_middle = sorted_numbers[middle_index - 1] # Get the left middle element
        right_middle = sorted_numbers[middle_index] # Get the right middle element
        return (left_middle + right_middle) / 2 # Average of the two middle elements


def variance(numbers, avg): # Calculate the variance of a list of numbers
    total = 0
    for value in numbers:
        diff = value - avg
        total = total + (diff * diff)
    return total / len(numbers)


def std_dev(variance_value): # Calculate the standard deviation from variance
    return variance_value ** 0.5 # Square root of variance


def main(): # Main function to interact with the user and display results
    while True:
        how_many_text = input("How many values do you want to enter? (>= 1) ")
        try:
            how_many = int(how_many_text)
            if how_many < 1:
                print("Please enter a number 1 or greater.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (like 3 or 10).")

    numbers = []

    for i in range(1, how_many + 1): # Loop to get each number from the user
        while True:
            value_text = input(f"Enter number {i}: ")
            try:
                value = float(value_text)
                numbers.append(value)
                break
            except ValueError:
                print("Please enter a valid number (for example: 3, 4.5, -1).")

    avg = mean(numbers)
    med = median(numbers)
    var = variance(numbers, avg)
    sd = std_dev(var)

    print("\nResults:")
    print("Average:", round(avg))
    print("Median:", round(med))
    print("Variance:", round(var))
    print("Standard Deviation:", round(sd))


if __name__ == "__main__": # Entry point of the program
    main() # Call the main function