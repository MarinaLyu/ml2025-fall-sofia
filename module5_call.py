from module5_mod import NumberProcessor


def main():

    processor = NumberProcessor()

    # Read N (positive integer)
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

    # Read N numbers one by one
    print(f"Please enter {n} numbers, one by one:")
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                processor.add_number(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Read X (integer to search for)
    while True:
        try:
            x = float(input("Enter the number X to search for: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Search for X and output result
    result = processor.search_number(x)
    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
