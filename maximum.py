def maximum(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        print("a and b are the same!")


print("The maximum of 10 and 6 is: " + str(maximum(10,6))