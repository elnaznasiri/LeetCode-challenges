# solution 1
def isPalindrome(x):
    temp = x
    rev = 0
    while (x > 0):
        dig = x % 10
        rev = rev * 10 + dig
        x = x // 10
    if (temp == rev):
        return True
        print("The number is a palindrome!")
    else:
        return False
        print("The number isn't a palindrome!")


print(isPalindrome(121))


# solution 2
def is_Palindrome(x: int) -> bool:
    if x < 0:
        return False
    str_n = str(x)
    return str_n == str_n[::-1]


print(is_Palindrome(12321))
