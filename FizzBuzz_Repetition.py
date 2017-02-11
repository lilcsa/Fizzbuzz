#FizzBuzz

print "Welcome to FizzBuzz"

number = int(raw_input("Enter a number between 1 and 100:"))

try:
    number = int(number)

    for num in range(number+1):
        if num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"


