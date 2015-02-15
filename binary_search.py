# binary search requires the list to be sorted

lst = [1,34,454,6565,4,6,56,776,76,3,89,-1,-43]
sorted_lst = sorted(lst)
x = 34
def binary_search(lst,x):

    start_index = 0
    end_index = len(lst)-1

    while start_index <= end_index:
        mid = (start_index + end_index)/2
        if sorted_lst[mid]== x:
            return mid
        elif x < sorted_lst[mid]:
            end_index = mid - 1

        else:
            start_index = mid + 1

    return -1


print sorted_lst
print "The number {} is located in {}".format(x, binary_search(lst, x))




