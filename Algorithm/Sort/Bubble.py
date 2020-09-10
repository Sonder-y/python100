# created by Sonder on 2020.09.10

def bubble_sort(li):
    for i in range(len(li) - 1):
        flag = False
        for j in range(1, len(li) - i):
            if li[j - 1] > li[j]:
                temp = li[j - 1]
                li[j - 1] = li[j]
                li[j] = temp
                flag = True
        if not flag:
            break
    return li

if __name__ == '__main__':
    lis = [7, 5, 4, 6, 3, 8, 2, 9, 1]
    print(bubble_sort(lis))