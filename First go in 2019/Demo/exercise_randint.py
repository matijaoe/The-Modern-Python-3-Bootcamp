# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint(1, 10)
    if number == 5:
        break
    print(number)
    i += 1

print("\n\tFinal number is " + str(number) + "\n")
