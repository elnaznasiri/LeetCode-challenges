def isPalindrome(x):
    temp=x
    rev=0
    while(x>0):
        dig=x%10
        rev=rev*10+dig
        x=x//10
    if(temp==rev):
        return True
        print("The number is a palindrome!")
    else:
        return False
        print("The number isn't a palindrome!")
print(isPalindrome(121))

