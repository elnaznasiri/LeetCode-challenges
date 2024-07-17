# solution 1
def isPalindrome(s: str) -> bool:
    sequence = ""
    for i in s:
        if i.isalpha():
            sequence += i
        elif i.isdigit():
            sequence += i
    sequence = sequence.lower()
    for i in range(len(sequence) // 2):
        if sequence[i] != sequence[len(sequence) - 1 - i]:
            return False
    return True


print(isPalindrome("race a car"))  # False

# solution 2
import re


def is_palindrome(s: str) -> bool:
    # تبدیل حروف بزرگ به حروف کوچک و حذف کاراکترهای غیر الفبایی عددی
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # بررسی پالینڈروم بودن رشته
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  # باید True برگرداند
print(is_palindrome("race a car"))  # باید False برگرداند


# solution 3
def is_palindrome(s: str) -> bool:
    # استفاده از لیست برای ساخت رشته
    sequence = [i.lower() for i in s if i.isalnum()]

    # بررسی پالینڈروم بودن رشته
    return sequence == sequence[::-1]


print(is_palindrome("race a car"))  # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
