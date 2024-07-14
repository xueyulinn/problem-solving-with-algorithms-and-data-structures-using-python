# def revstring(mystr):
#     ''' use stack to reverse a str with O(n) time complexity '''
#     items = []
#     for i in range(len(mystr)):
#         items.append(mystr[i])

#     rs = ''
#     while not items == []:
#         rs += items.pop()

#     return rs


def revstring(mystr):
    # 1. using slicing
    
    # [start:end:step], start is the beginning and end is the ending by default
    # ommit start and end means the entire str
    
    return mystr[::-1]

    # 2. using list comprehension
    # return ''.join([mystr[i] for i in range(len(mystr)-1, -1, -1)])


str = 'Hello World'
print(revstring(str))
