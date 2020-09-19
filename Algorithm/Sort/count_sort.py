# created by Sonder on 2020.09.19

def count_sort(li, max_count=10):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] = count[val] + 1
    li.clear()
    for index, val in enumerate(count):
        for i in range(val):
            li.append(index)

if __name__ == '__main__':
    lis = [3,2,4,1,5,7,9,6,8]
    count_sort(lis, len(lis))
    print(lis)