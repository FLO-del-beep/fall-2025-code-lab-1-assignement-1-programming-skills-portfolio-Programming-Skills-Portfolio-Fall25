def check_even_odd(number):
    # This code checks if the number is even or odd
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    # Pass the number to the function and get the result
    result = check_even_odd(num)

    # Print the returned message
    print(result)

if __name__ == "__main__":
    main()
