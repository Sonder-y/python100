# test1: find Number of daffodils
# import math
# list1 = []
# for i in range(100, 1000):
#     a = i % 10
#     b = math.floor((i % 100) / 10)
#     c = math.floor(i / 100)
#     if math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3) == i:
#         list1.append(i)
# print(list1)


# test2: A hundred money and a hundred chickens problem
# import math
# for gj in range(0, 21):
#     money = 100
#     money = money - 5 * gj
#     for mj in range(0, math.ceil(money/3)):
#         xj = (money - mj * 3) * 3
#         print("gj: %d, mj: %d, xj: %d" % (gj, mj, xj))

# # test3: CRAPS
# import random
# money = 1000
# while money >= 0:
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     if dice1 + dice2 == 7 or dice1 + dice2 == 11:
#         money = money + 1
#     elif dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
#         money = money - 1
#     else:
#         win_flag = True
#         while win_flag == True:
#             dice3 = random.randint(1, 6)
#             dice4 = random.randint(1, 6)
#             if dice3 + dice4 == 7:
#                 money = money - 1
#                 win_flag = False
#             elif dice3 + dice4 == dice1 + dice2:
#                 money = money + 1
#                 win_flag = False
#             else:
#                 win_flag = True

# # exercise 1: generate the first 20 number of Fibonacci sequence
# list1 = [1, 1]
# for i in range(1, 19):
#     list1.append(list1[i-1] + list1[i])
# print(list1)

# exercise 2: find perfect number within 10000
# num_list = [1]
# for num in range(2, 10000):
#     count = 0;
#     for i in range(1, num):
#         if num % i == 0:
#             count = count + i
#     if count == num:
#         num_list.append(num)
# print(num_list)

# exercise 3: Output all prime numbers within 100
for i in range(2, 100):
    count = 0
    for single in range(2, i):
        if i % single == 0:
            count = count + 1
    if count == 0:
        print(i)