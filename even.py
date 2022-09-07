
number = (int(input("Pick an even number between 1 and 10 ")))


if number < 10:
    num_1 = int(input("How many times is your number divisible by 2? "))
elif number >= 10:
    print("Please pick a number between 1 and 10")
prime = (str(input("Is it a prime number? ")))
if prime.upper() == "Y":
    print("Your number is 2 ")
elif prime.upper() == "N":
    factor = input("Is your number bigger than 6? ")
if factor.upper() == "Y":
    print("Your number is 10 ")
elif factor.upper() == "N":
    print("Your number is 6 ")
if num_1 == 2:
    print("Your number is 4 ")
if num_1 == 3:
    print("Your number is 8 ")
else:
    print("Try again")


