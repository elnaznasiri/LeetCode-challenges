#solution 1
def lenghtOfLastWord(s):
    verb = s.split()
    return len(verb[-1])

print(lenghtOfLastWord("luffy is still joyboy"))


#solution 2
def lenghtOfLastWord(s):
    strip = s.strip()
    word = strip.split()
    return len(word[-1])
    
print(lenghtOfLastWord("luffy is still joyboy"))
