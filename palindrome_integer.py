def palindrome_integer(palindrome):
    if str(palindrome) == str(palindrome)[::-1]:
        return True
    else:
        return False

print(palindrome_integer(321))          