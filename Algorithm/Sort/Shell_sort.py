# created by Sonder on 2020.09.19

def insertion_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i: the index of the new number
        temp = li[i]
        j = i - gap
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
            j = j - gap
        li[j + gap] = temp
    return li

def shell_sort(li):
    d = len(li)
    while d >= 1:
        insertion_sort_gap(li, d)
        d = d // 2

if __name__ == '__main__':
    lis = [3,2,4,1,5,7,9,6,8]
    shell_sort(lis)
    print(lis)
