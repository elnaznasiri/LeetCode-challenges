def add_string(number1: str, number2: str) -> str:
    i, j = len(number1) - 1, len(number2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = int(number1[i]) if i >= 0 else 0
        digit2 = int(number2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(total % 10)

        i -= 1
        j -= 1
    result.reverse()
    return ''.join(map(str, result))


# Example usage
num1 = "123"
num2 = "456"
print(add_string(num1, num2))  # Output: "579"
