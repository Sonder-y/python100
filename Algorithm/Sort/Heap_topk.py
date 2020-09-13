# created by Sonder on 2020.09.13

def sift(li, top, bottom):  # bottom - the position of the last leaf
    i = top             # the position level of root
    j = 2 * i + 1       # the position of the left leaf of the previous root
    temp = li[i]

    while j <= bottom:
        if j + 1 <= bottom and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < temp:
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

def topk(li, k):
    li_heap = li[0:k]
    # build a heap of legnth k
    for i in range((len(li_heap) - 2) // 2, -1, -1):
        sift(li_heap, i, len(li_heap) - 1)
    # iterate the remaining part of the list, select the bigger num into the li_heap
    for i in range(len(li) - 1, k - 1, -1):
        if li[i] > li_heap[0]:
            li_heap[0] = li[i]
            sift(li_heap, 0, len(li_heap) - 1)
    #
    for i in range(len(li_heap) - 1, -1, -1):  # i: the last position of the heap
        li_heap[0], li_heap[i] = li_heap[i], li_heap[0]
        sift(li_heap, 0, i - 1)
    return li_heap

if __name__ == '__main__':
    lis = [3,2,4,1,5,7,9,6,8]
    li = list(range(10))
    import random
    random.shuffle(li)
    t = topk(li, 5)
    print(t)