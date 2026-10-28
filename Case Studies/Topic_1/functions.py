def square(number: int) -> int:
    squared = (number ** 2)
    print(f"Original number: {number}")
    print(f"Squared number: {squared}")
    print()

def parity(number: int) -> int:
    result = 'even' if number % 2 == 0 else 'odd'
    print(f"{number} is {result}.")
    print()

def average(num_list):
    total = sum(num_list)
    length = len(num_list)
    avg = total/length
    print(f"The average (mean) of this list is {avg}.")
    print()

square(5)
square(3)
parity(1)
parity(4)
average([1, 2, 3, 4, 5])
average([17, 32, 63, 45, 5])