def isPalindrome(s: str) -> bool:
    sequence=""
    for i in s:
        if i.isalpha():
            sequence+=i
        elif i.isdigit():
            sequence+=i
    sequence=sequence.lower()
    for i in range(len(sequence)//2):
        if sequence[i] != sequence[len(sequence)-1-i]:
            return False
    return True



print(isPalindrome("race a car")) #False