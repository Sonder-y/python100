# test1: Enter a positive integer to determine if it is a prime number.
# num = int(input("please input a positive integer: "))
# count = 0
# if num == 1:
#     print("1 is not a prime number!")
# else:
#     for x in range(1, num):
#         if num % x == 0:
#             count = count + 1
# if count >= 2:
#     print("%d is not a prime number!" % num)
# else:
#     print("%d is a prime number!" % num)


# test2: Enter two positive integers and calculate their greatest common divisor and least common multiple.
num1 = int(input("please input a positive integer: "))
list1 = []
num2 = int(input("please input a positive integer: "))
list2 = []
common_div = 1
for x in range(1, num1 + 1):
    if num1 % x == 0:
        list1.append(x)
for x in range(1, num2 + 1):
    if num2 % x == 0:
        list2.append(x)
flag = True
for i in reversed(list1):
    if flag == False:
        break
    else:
        for j in reversed(list2):
            if i == j:
                common_div = i
                flag = False
                break
temp = 0
if num1 >= num2:
    temp = num1
else:
    temp = num2
for i in range(temp, num1 * num2):
    if i % num1 == 0 and i % num2 == 0:
        temp = i
        break
print("least common multiple is %d" % temp)
print("the greatest common divisor is %d" % common_div)
