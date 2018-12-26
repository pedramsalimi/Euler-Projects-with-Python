# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def Project_6():

    sumOfSquare = 0
    squareOfsum = 0

    sumOfSquare = sum(i**2 for i in range(1,101))
    squareOfsum = sum(range(1,101))**2
    result = squareOfsum - sumOfSquare

    return result

print(Project_6())
# or for more pythonic
print(sum(range(1,101)) ** 2 - sum(x ** 2 for x in range(1,101)))
