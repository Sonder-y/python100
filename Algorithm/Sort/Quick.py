# created by Sonder on 2020.09.11
# step 1: find a standard value, divide the list into
# left part and right part based on this standard value.

# O(nlogn)
# recursive times: time = logn
# partition times: n

# the worst condition: 9 8 7 6 5 4 3 2 1    To traverse N numbers  O(n^2)
# the first partition: _ 8 7 6 5 4 3 2 1  ->  1 8 7 6 5 4 3 2 _     (n - 1)
# the second partition: 1 8 7 6 5 4 3 2 _  ->  1 8 7 6 5 4 3 2 _     (n - 2)

def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)

# better solution: find another num randomly to exchange with the first num for temp
def partition(data, left, right):
    temp = data[left]
    while left < right:
        while data[right] >= temp and left < right: # find smaller num in the right side
            right = right - 1   # move 1 step to left
        data[left] = data[right]
        while data[left] <= temp and left < right: # find bigger num in the left side
            left = left + 1     # move 1 step to right
        data[right] = data[left]
    data[left] = temp
    print(data)
    return left

if __name__ == '__main__':
    lis = [5, 3, 2, 4, 1, 10, 7, 9, 6, 8]
    print(quick_sort(lis, 0, len(lis) - 1))
    import heapq