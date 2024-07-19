def isPlaindrome(str):
    if len(str) <= 1:
        return True

    if str[0] == str[-1]:
        isPlaindrome(str[1:-1])
    else:
        return False