# test1: the conversion between inch and cm
# value = float(input('please input the length: '))
# unit = input('please input the unit: (in or cm)')
# if unit == 'in':
#     print("%f to inch is: %f in" %(value, value * 2.54))
# elif unit == 'cm':
#     print("%f to inch is: %f cm" % (value, value / 2.54))
# else:
#     print("Your input is invalid!")

# test2: The 100-point system is converted to grade system (A,B,C,D,E).
# grade = int(input("please input grade: "))
# if grade <= 100 and grade >= 90:
#     print("A")
# elif grade < 90 and grade >= 80:
#     print('B')
# elif grade < 80 and grade >= 70:
#     print('C')
# elif grade < 70 and grade >= 60:
#     print('D')
# elif grade < 60 and grade >= 0:
#     print('E')
# else:
#     print("input error!!!")

# test3: Enter the length of three sides, and calculate the perimeter and area if they can form a triangle.
import math
a = float(input("length of the first side: "))
b = float(input("length of the second side: "))
c = float(input("length of the third side: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("input length error!!!")
else:
    perimeter = a + b + c
    per = perimeter / 2
    area = math.sqrt(per * (per - a) * (per - b) * (per - c))
    print("perimeter: %.1f" % perimeter)
    print("area: %.1f" % area)