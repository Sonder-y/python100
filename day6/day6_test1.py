# test1: a function to calculate their greatest common divisor and least common multiple.
def gbs(num1, num2):
    temp = 0
    if num1 >= num2:
        temp = num1
    else:
        temp = num2
    for i in range(temp, num1 * num2):
        if i % num1 == 0 and i % num2 == 0:
            temp = i
            break
    return temp

def gys(num1, num2):
    list1 = []
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
    return common_div

if __name__ == '__main__':
    print(gys(8,16))
    print(gbs(8,16))