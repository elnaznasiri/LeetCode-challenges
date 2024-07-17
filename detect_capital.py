# solution 1
def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    return word.isupper() or word.islower() or word.istitle()


print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))


# solution 2
def detect_captalUse(word: str) -> bool:
    if word.isupper():
        return True
    # or if
    elif word.islower():
        return True
    # or if
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False
    # or return False


print(detect_captalUse("Google"))
print(detect_captalUse("GooglE"))


# solution 3
def detectCapitalUse(word):
    capital_count = sum(1 for c in word if c.isupper())
    if capital_count == len(word):  # همه حروف بزرگ هستند
        return True
    if capital_count == 0:  # همه حروف کوچک هستند
        return True
    if capital_count == 1 and word[0].isupper():  # فقط حرف اول بزرگ است
        return True
    return False


print(detectCapitalUse("Google"))
print(detectCapitalUse("GooglE"))


# solution 4
def detectCapitalUse(word):
    check_upper = word.isupper()
    check_lower = word.islower()
    if check_upper == 1:
        return True
    if check_lower == 1:
        return True
    if word[1:].islower() and word[0].isupper():
        return True
    return False


print(detectCapitalUse("GOOGLE"))
print(detectCapitalUse("GooglE"))
