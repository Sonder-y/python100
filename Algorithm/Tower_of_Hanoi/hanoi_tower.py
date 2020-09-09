# created by Sonder on 2020.09.09 

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('move from %s to %s' % (a, c))
        hanoi(n - 1, b, a, c)


if __name__ == '__main__':
    hanoi(3, 'a', 'b', 'c')