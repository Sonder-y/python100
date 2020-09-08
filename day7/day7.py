# Strings and common data structures

# Generatives and generators
# import sys
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)
#
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# # for val in f:
# #     print(val)



# test 1: Show marquee text on the screen
import time
def test1():
    text = "Hello World"
    while True:
        print(text)
        time.sleep(0.2)
        text = text[1:] + text[0]

# test 2: A function generates a verification code of a specified length,
# the verification code is composed of uppercase and lowercase letters and numbers
def code_generation(length):
    import string
    import random
    t = random.sample((string.ascii_letters + string.digits),length)
    print("".join(t))
    return t

# test 3: A function returns the suffix of a given file name
def suffix(fname):
    ss = fname.split('.')[-1]
    print(ss)
    return ss

# test 4: A function returns the values of the largest and second largest elements in the passed list.
def large_second(li):
    li.sort(reverse=True)
    print(li[0:2])
    return li[0:2]

# test 5:Print Yanghui Triangle
def yanghui():
    list_line1 = [1,1]
    list_line2 = [1, list_line1[0] + list_line1[1], 1]
    print(list_line1)
    print(list_line2)
    for i in range(10):
        list_line1 = list(list_line2)
        list_line2.append(1)
        for j in range(1, len(list_line2) - 1):
            list_line2[j] = list_line1[j-1] + list_line1[j]
        print(list_line2)

# exercise 1: Joseph ring problem.
# There were 15 Christians and 15 non-Christians in distress at sea. In order to make some people survive,
# 15 of them had to be thrown into the sea. Someone thought of a way to form a circle with someone Start
# counting from 1, and those who report to 9 are thrown into the sea. The people behind him then start
# counting from 1, and those who report to 9 continue to throw into the sea until 15 people are thrown away.
# Thanks to God’s blessing, all 15 Christians were spared. How did these people stand in the first place,
# which positions were Christians and which positions were non-Christians.

def joseph():
    # 1 means Christian
    # 0 means non-Christian
    ll = [1 for n in range(30)]
    bad = 0
    count = 0
    while True:
        for i in range(len(ll)):
            if ll[i] == 1:
                count = count + 1
                if count != 9:
                    continue
                else:
                    ll[i] = 0
                    bad = bad + 1
                    count = 0
        if bad == 15:
            break
    print(ll)


if __name__ == '__main__':
    joseph()