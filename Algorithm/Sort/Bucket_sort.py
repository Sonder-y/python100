# created by Sonder on 2020.09.20

def bucket_sort(li, n=100, max_num = 10000):
    buckets = [[] for _ in range(n)]
    for var in li:
        # consider the last element, e.g. 100 or 10000
        i = min(var // (max_num // n), n - 1) # i: means the bucket we should put the number into
        buckets[i].append(var)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j - 1], buckets[i][j] = buckets[i][j], buckets[i][j - 1]
            else:
                break
    sorted_list = []
    for buc in buckets:
        sorted_list.extend(buc)
    return sorted_list

if __name__ == '__main__':
    import random
    li = [random.randint(0, 10000) for i in range(10000)]
    print(bucket_sort(li))

