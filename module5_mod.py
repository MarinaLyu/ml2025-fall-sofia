class NumberProcessor:

    def __init__(self):

        self.numbers = []

    def set_numbers(self, numbers_list):

        self.numbers = numbers_list

    def add_number(self, number):

        self.numbers.append(number)

    def search_number(self, x):

        for i, num in enumerate(self.numbers):
            if num == x:
                return i + 1  # Return 1-based index
        return -1

    def get_numbers_count(self):

        return len(self.numbers)

    def clear_numbers(self):

        self.numbers = []
