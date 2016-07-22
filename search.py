import math

# O(log n)
def recursive_binary_search(value, sorted_list):
  if len(sorted_list) == 0:
    return False

  middle = int(len(sorted_list) / 2)

  if value == sorted_list[middle]:
    return True
  elif value > sorted_list[middle]:
    return binary_search(value, sorted_list[middle + 1:])
  else:
    return binary_search(value, sorted_list[:middle])

def binary_search(value, sorted_list):
  first = 0
  last = len(sorted_list) - 1
  found = False

  while first <= last and not found:
    middle = int((first + last) / 2)

    if value == sorted_list[middle]:
      found = True
    elif value > sorted_list[middle]:
      first = middle + 1
    else:
      last = middle - 1

  return found

print(recursive_binary_search(1, range(1, 6)))
print(recursive_binary_search(5, range(1, 6)))
print(recursive_binary_search(7, range(1, 6)))
print(binary_search(1, range(1, 6)))
print(binary_search(5, range(1, 6)))
print(binary_search(7, range(1, 6)))
