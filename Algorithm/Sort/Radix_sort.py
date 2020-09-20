# created by Sonder on 2020.09.20

# O(kn) k is the number of digits
def radix_sort(li):
    max_num = max(li)
    max_num_str = str(max_num)
    for i in range(len(max_num_str)):
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // (10 ** i)) % 10
            buckets[digit].append(val)
        li.clear()
        for buc in buckets:
            li.extend(buc)
    return li

if __name__ == '__main__':
    import random
    li = [random.randint(0, 10000) for i in range(10000)]
    print(radix_sort(li))
