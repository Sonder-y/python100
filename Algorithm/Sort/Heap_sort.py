# created by Sonder on 2020.09.12

# O(n * logn)
# sift: logn, always iterate half of the tree 1/2, 1/4, 1/8 ...


def sift(li, top, bottom):  # bottom - the position of the last leaf
    i = top             # the position level of root
    j = 2 * i + 1       # the position of the left leaf of the previous root
    temp = li[i]

    while j <= bottom:
        if j + 1 <= bottom and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > temp:
            li[i] = li[j]   # put the bigger leaf on the position of root
            i = j       # process next level
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp

def heap_sort(li):
    length = len(li)
    for i in range((length - 2)//2, -1, -1): # build the heap
        sift(li, i, length - 1)

    for i in range(length - 1, -1, -1):  # i: the last position of the heap
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)

if __name__ == '__main__':
    lis = [3,2,4,1,5,7,9,6,8]
    heap_sort(lis)
    print(lis)
