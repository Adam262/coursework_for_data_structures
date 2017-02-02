# lists
# pythion class experience re run times
    # concat is O(n), 6.54352807999 milliseconds

    # all others are O(1), but not same speed
    # append 0.306292057037 milliseconds
    # comprehension  0.147661924362 milliseconds
    # list range  0.0655000209808 milliseconds

def concat_to_list(n):
    list = []
    for i in range(1, n+1):
        list += [i]
    return list
    
def append_to_list(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list

def comprehend_to_list(n):
    return [i for i in range(1,n+1)]
    
def range_to_list(n):
    return list(range(1,n+1))

concat_to_list(10) == append_to_list(10) == comprehend_to_list(10) == range_to_list(10)