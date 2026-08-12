class Number:

    def square(self, number: int) -> int:
        squared = (number ** 2)
        print(f"Original number: {number}")
        print(f"Squared number: {squared}")
        print()

    def parity(self, number: int) -> int:
        result = 'even' if number % 2 == 0 else 'odd'
        print(f"{number} is {result}.")
        print()

    def average(self, num_list):
        total = sum(num_list)
        length = len(num_list)
        avg = total / length
        print(f"The average (mean) of this list is {avg}.")
        print()


number = Number()
number.square(5)
number.square(3)
number.parity(1)
number.parity(4)
number.average([1, 2, 3, 4, 5])
number.average([17, 32, 63, 45, 5])