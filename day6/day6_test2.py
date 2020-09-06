# test 2: A function to verify whether a number is a palindrome number
def check_palindrome(num):
    num_str = str(num)
    if num_str == "".join(reversed(num_str)):
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_palindrome(121))