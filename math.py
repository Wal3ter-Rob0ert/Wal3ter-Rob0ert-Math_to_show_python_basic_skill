def mean(numbers): # Calculate the mean (average) of a list of numbers
    return sum(numbers) / len(numbers) # Sum of numbers divided by count


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
    total = 0  # Initialize total to 0
    for value in numbers: # Loop through each number
        diff = value - avg # Calculate the difference from the mean
        total = total + (diff * diff) # Add the squared difference to total
    return total / len(numbers)  # Return the average of the squared differences


def std_dev(variance_value): # Calculate the standard deviation from variance
    return variance_value ** 0.5 # Square root of variance


def main(): # Main function to interact with the user and display results
    while True: # Loop to get a valid number of values from the user
        how_many_text = input("How many values do you want to enter? (>= 1) ") # Prompt user for number of values
        try: # Try to convert input to an integer
            how_many = int(how_many_text) # Convert input to integer
            if how_many < 1: # Check if the number is less than 1
                print("Please enter a number 1 or greater.") # Prompt user to enter a valid number
                continue # Continue the loop to ask again
            break # Exit the loop if a valid number is entered
        except ValueError: # Handle invalid input
            print("Please enter a whole number (like 3 or 10).") # Prompt user to enter a valid number

    numbers = [] # Initialize an empty list to store the numbers

    for i in range(1, how_many + 1): # Loop to get each number from the user
        while True: # Loop to get a valid number
            value_text = input(f"Enter number {i}: ") 
            try: # Try to convert input to a float
                value = float(value_text)  # Convert input to float
                numbers.append(value) # Add the number to the list
                break   # Exit the loop if a valid number is entered
            except ValueError: # Handle invalid input
                print("Please enter a valid number (for example: 3, 4.5, -1).") # Prompt user to enter a valid number

    avg = mean(numbers) # Calculate the mean
    med = median(numbers) # Calculate the median
    var = variance(numbers, avg) # Calculate the variance
    sd = std_dev(var) # Calculate the standard deviation

    print("\nResults:") # Display the results
    print("Average:", round(avg))   # Rounded average
    print("Median:", round(med))    # Rounded median
    print("Variance:", round(var))  # Rounded variance
    print("Standard Deviation:", round(sd))  # Rounded standard deviation

if __name__ == "__main__": # Entry point of the program
    main() # Call the main function