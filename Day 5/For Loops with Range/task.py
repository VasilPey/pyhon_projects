for number in range(1,101):
    if (number % 5 == 0 and number % 3 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    elif(number % 5 == 0 and number % 3 == 0):
        print("FizzBuzz")
    else:
        print(number)