# a = int(input("a = "))
# b = int(input("b = "))
# c = input("c = ")
#
# print("hhh%d + %d = %d" % (a, b, a + b))
# print("String: %s" % c)

# test1: Convert Fahrenheit to Celsius.
# a = float(input("Fahrenheit: "))
# c = (a -32) / 1.8
# print("Fahrenheit: %.1f, Celsius: %.1f" % (a, c))

# test2: calculate the circumference and area based on the radius of the circle.
# import math
# r = float(input("Radius: "))
# area = math.pi * math.pow(r, 2)
# c = 2 * math.pi * r
# print("Radius: %.1f, area: %.1f, circumference: %.1f" % (r, area, c))

# test3: check leap year
year = int(input('year: '))
if year % 4 == 0:
    print("year %d is a leap year." % year)
else:
    print("year %d is not a leap year." % year)