# solution 1
def length_of_last_word(s):
    words = s.split()  # رشته را به کلمات تقسیم می‌کند
    if words:  # بررسی می‌کند که آیا لیست کلمات خالی نیست
        return len(words[-1])  # طول آخرین کلمه را برمی‌گرداند
    else:
        return 0  # اگر لیست کلمات خالی باشد، صفر برمی‌گرداند


# نمونه استفاده
s = "   fly me   to   the moon  "
print(length_of_last_word(s))


# solution 2
def lenghtOfLastWord(s):
    strip = s.strip()
    word = strip.split()
    return len(word[-1])


print(lenghtOfLastWord("luffy is still joyboy"))


# solution3
def lenght_of_last_word(s):
    is_word = False
    lenght = 0
    for char in reversed(s):
        if char != ' ':
            is_word = True
            lenght += 1
        elif is_word:
            break
    return lenght


s = "   fly me   to   the moon  "
print(lenght_of_last_word(s))
