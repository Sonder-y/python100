# test 3: A function to determine whether a number is prime
def check_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count = count + 1
    if count > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    print(check_prime(17))