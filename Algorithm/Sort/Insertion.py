# created by Sonder on 2020.09.10

def insertion_sort(li):
    for i in range(len(li) - 1):
        j = i + 1
        while li[j] < li[i]:
            li[i], li[j] = li[j], li[i]
            i = i - 1
            j = j - 1
            if i == -1:
                break
        print(li)
    return li

if __name__ == '__main__':
    lis = [3,2,4,1,5,7,9,6,8]
    print(insertion_sort(lis))