class NumberSearch:
    def __init__(self):
        self.data = []

    def insert_number(self, num):
        self.data.append(num)

    def search(self, x):
        if x in self.data:
            return self.data.index(x) + 1  # index from 1 to N
        return -1


def main():
    # Ask for N
    N = int(input("Enter a positive integer N: "))

    searcher = NumberSearch()

    # Read N numbers
    for i in range(N):
        num = int(input(f"Enter number #{i+1}: "))
        searcher.insert_number(num)

    # Read X and search
    X = int(input("Enter X: "))
    result = searcher.search(X)
    print(result)


if __name__ == "__main__":
    main()
