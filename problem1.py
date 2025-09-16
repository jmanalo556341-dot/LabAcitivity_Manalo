
def gcd(x, y):

    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):

    return abs(x * y) // gcd(x, y)

def get_positive_int(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


x = get_positive_int("Enter a value for x: ")
y = get_positive_int("Enter a value for y: ")

result = lcm(x, y)
print(f"The LCM of {x} and {y} is = {result}")