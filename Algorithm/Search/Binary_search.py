# created by Sonder on 2020.09.09

def binary_search(li, element):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if element == li[mid]:
            return mid
        elif li[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


if __name__ == '__main__':
    t = binary_search([1, 2, 3, 4, 5, 6], 2)
    print(t)