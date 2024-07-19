def reverse(str):
    '''A function that takes a string as a parameter and returns 
    a new string that is the reverse of the old string.'''
    if len(str) == 0:
        return str
    else:
        return str[-1] + reverse(str[:-1])


print(reverse('hello'))
