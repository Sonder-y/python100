# created by Sonder on 2020.09.10

def selection_sort_v1(li):
    new_li = []
    for i in range(len(li)):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li

def selection_sort_v2(li):
    for i in range(len(li) - 1):
        index = i
        for j in range(i + 1, len(li)):
            if li[index] < li[j]:
                index = j
        li[index], li[i] = li[i], li[index]
    return li


if __name__ == '__main__':
    lis = [7, 5, 4, 6, 3, 8, 2, 9, 1]
    lis2 = [2, 5]
    print(selection_sort_v2(lis2))