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

num_list = [4,9,11,17,21,25,29,32,38]
print(BinarySearch(num_list,29))
