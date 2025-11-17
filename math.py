import statistics # Importing statistics module for calculations

def main(): # Main function to execute the program
    n = int(input("How many values do you want to enter? ")) # Getting number of inputs from user

    values = [] # List to store user input values
    for i in range(1, n + 1): # Loop to get user input
        num = float(input(f"Enter number {i}: ")) # Getting user input
        values.append(num) # Appending input to the list 

    avg = statistics.mean(values) # Calculating average
    median = statistics.median(values) # Calculating median
    variance = statistics.pvariance(values) # Calculating variance
    std_dev = statistics.pstdev(values) # Calculating standard deviation

    print(f"Average: {round(avg)}") # Printing rounded average
    print(f"Median: {round(median)}") # Printing rounded median
    print(f"Variance: {round(variance)}") # Printing rounded variance
    print(f"Standard Deviation: {round(std_dev)}") # Printing rounded standard deviation

if __name__ == "__main__": # Ensuring the main function runs only when the script is executed directly
    main() # Calling the main function to start the program