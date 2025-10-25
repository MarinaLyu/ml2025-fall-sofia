# The program asks the user for input N (positive integer) and reads it.
# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
# Hint: use input() function

N = int(input("Enter a positive integer N: "))
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
X = int(input("Enter an integer X: "))
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)

