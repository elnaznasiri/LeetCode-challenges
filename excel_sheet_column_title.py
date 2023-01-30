def convertToTitle(columnNumber):
    result = ""
    while columnNumber > 0:
        result = chr(ord('A') + (columnNumber - 1) % 26) + result
        columnNumber = (columnNumber - 1) // 26
    return result

print(convertToTitle(28))