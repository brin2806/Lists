
num = [-1,10,-3,0,-20]

# this is my function for adding items in a list

def sumOfList(lst):
    total = 0
    for item in lst:
        total = total + item

    return total

print sumOfList(num)


# function for calculating max num in a list using loops
def get_max_of_list(lst):
    num = None
    for item in lst:
        if item > num:
            num = item

    return num

print get_max_of_list(num)

# use sorted function to generate maximum number
def max_using_sort(lst):
    lst_sort = sorted(lst)
    return lst_sort[-1]

print max_using_sort(num)


# generating the smallest and largest numbers using sort function

def smallest_largest(lst):
    lst_sort = sorted(lst)
    return lst_sort[0], lst_sort[-1]

print smallest_largest(num)


# generating smallest and largest using loops and no inbuilt functions

def smallestLargest(lst):
    smallest = None
    largest = None
    for item in lst:
        if smallest is None and largest is None:
            smallest = item
            largest = item

        elif item < smallest:
            smallest = item

        elif item > largest:
            largest = item

    return smallest, largest


print smallestLargest(num)

