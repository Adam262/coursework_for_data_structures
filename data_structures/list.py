# append
def print_range_append(n):
  list = []

  for num in range(1, n+1):
    list.append(num)

  print list

# concat
def print_range_concat(n):
  list = []

  for num in range(1, n+1):
    list = list + [num]

  print list

# list comprehension
def print_range_comprehension(n):
  print [num for num in list(range(1, n+1))]

# wrap range in list. By far, fastest
def print_range_list(n):
  print list(range(1, n+1))

# test is with 1000 item range
print_range_list(10) # By far fastest, 0.0655000209808 milliseconds
print_range_comprehension(10) # 0.147661924362 milliseconds
print_range_append(10) # 0.306292057037 milliseconds
print_range_concat(10) # By far slowest, 6.54352807999 milliseconds

# iterative reverse list
def rev(list_param):
  new_list = []

  while len(list_param) > 0:
    new_list.append(list_param.pop())

  return new_list

# recursive reverse list
def recursive_rev(list_param, new_list):
  if len(list_param) == 1:
    return new_list + list_param
  else:
    new_list.append(list_param.pop())
    return recursive_rev(list_param, new_list)

def recursive_rev_single(list_param):
  if len(list_param) == 1:
    return list_param
  else:
    return [list_param.pop()] + recursive_rev_single(list_param)

