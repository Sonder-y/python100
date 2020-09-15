# created by Sonder on 2020.09.15

# assume that a list can be divided into two ordered lists (left and right)
def merge(li, low, mid, high): # high: the index of the last element
    i = low      # the first index of left list
    j = mid + 1  # the first index of right list
    l_temp = []
    # O(n)
    while i <= mid and j <= high:  # ensure both right list and left list have one number
        if li[i] < li[j]:
            l_temp.append(li[i])
            i = i + 1
        else:
            l_temp.append(li[j])
            j = j + 1
    while i <= mid:
        l_temp.append(li[i])
        i = i + 1
    while j <= high:
        l_temp.append(li[j])
        j = j + 1
    li[low:high+1] = l_temp

# have to invoke merge_sort logn times
# O(nlogn)
def merge_sort(li, low, high):
    if low < high:  # at least two elements
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        #print(li[low:high + 1], "before merge")
        merge(li, low, mid, high)
        #print(li[low:high + 1], "after merge")


if __name__ == '__main__':
    li = [1,3,8,7,2,4,6,5]
    tt = merge_sort(li, 0, len(li) - 1)
    print(li)
