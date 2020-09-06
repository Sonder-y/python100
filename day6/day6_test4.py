# test 4: A program determines whether the input positive integer is a palindrome prime.
import day6_test3 as pr
import day6_test2 as pa
def check_both(num):
    if pr.check_prime(num) and pa.check_palindrome(num):
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_both(11))