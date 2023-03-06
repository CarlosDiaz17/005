#Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 1

def main(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

while True:
    if main(num):
        break
    num += 1

print(num)