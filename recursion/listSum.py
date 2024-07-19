def listsum(numList):
    if numList == []:
        return 0

    rs = numList.pop() + listsum(numList)

    return rs


print(listsum([1, 3, 5, 7, 9]))
