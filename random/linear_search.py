def linear_search(list, target):

    for i in range(1, len(list)):
        #Return the index value of the target. If not found return
        if list[i] == target:
            return i
    return None
    

def verify(index):
    if index is not None:
        print("Index value found at : ", index)
    else:
        print("Index value not found")


numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 11)
verify(result)
