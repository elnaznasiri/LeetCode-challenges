def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    return word.isupper() or word.islower() or word.istitle()