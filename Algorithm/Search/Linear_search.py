# created by Sonder on 2020.09.09

def linear_search(li, element):
    for index, val in enumerate(li):
        if element == val:
            return index
    else:
        return None
    
if __name__ == '__main__':
    t = linear_search([1,2,3,4,5,6], 5)
    print(t)