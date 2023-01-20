def longestCommonPrefix(strs):

    result = ""

    if strs is None or len(strs) == 0:
        return result
        
    # If there is only one element in array then return it
    if len(strs) == 1:
        return strs[0]

    # Find the minimum length string from the array
    minimum_length = len(strs[0])
    for i in range(1, len(strs)):
        minimum_length = min(minimum_length, len(strs[i]))

    # Loop until the minimum length
    for i in range(0, minimum_length):

        # Get the current character from the first string
        current = strs[0][i]

        # Check if this character is found in all other strings or not
        for j in range(0, len(strs)):
            if strs[j][i] != current:
                return result
        result += current
    return result

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))