
"""
BinarySearch Normal

def BinarySearch(numList,val):
    start = 0
    end = len(numList) - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        mid_val = numList[mid]
        if val == mid_val:
            return mid
        if mid_val < val:
            start = mid + 1
        else:
            end = mid - 1

    return -1
"""

# By recursion
def BinarySearch(numList,val,left,right):
    if right < left:
        return -1
        
    mid = (left + right) // 2
    mid_val = numList[mid]
    if val == mid_val:
        return mid
    else:
        if val < mid_val:
            right = mid - 1
        else:
            left = mid + 1

    return BinarySearch(numList,val,left,right)
        
num_list = [4,9,11,17,21,25,29,32,38]
print(BinarySearch(num_list,29,0,len(num_list)-1))
