from module5_mod import NumberSearch

def main():
    N = int(input("Enter a positive integer N: "))

    searcher = NumberSearch()

    for i in range(N):
        num = int(input(f"Enter number #{i+1}: "))
        searcher.insert_number(num)

    X = int(input("Enter X: "))
    result = searcher.search(X)
    print(result)


if __name__ == "__main__":
    main()
