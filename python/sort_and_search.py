import math
a_list = [12, 3, 7, 1, 11, 5, 0, 2, 9, 4]

# Selection Sort: O(n^2)
def selection_sort(list):
  if len(list) <= 1:
    return list

  for idx in range(len(list) - 1, 0, -1):
    highest = 0

    for sub_idx in range(1, idx + 1):
      if list[sub_idx] > list[highest]:
        highest = sub_idx

    if idx != highest:
      temp = list[idx]
      list[idx] = list[highest]
      list[highest] = temp

  return list

# Insertion Sort: O(n^2)
def insertion_sort(list):
  for idx in range(0, len(list)):
    current_value = list[idx]
    position = idx

    while position > 0 and list[position - 1] > current_value:
      list[position] = list[position - 1]
      position = position - 1
      print(list)
    list[position] = current_value

  return list

# Quick Sort: O(n log(n))
def quick_sort(list):
  if len(list) <= 1:
    return list

  pivot, left, right = list[0], [], []

  for el in list[1:]:
    if el <= pivot:
      left.append(el)
    else:
      right.append(el)

  left, right = quick_sort(left), quick_sort(right)

  return left + [pivot] + right

# Merge Sort: O(n log(n))
def merge_sort(list):
  if len(list) <= 1:
    return list

  middle = int(len(list) / 2)
  left = merge_sort(list[0:middle])
  right = merge_sort(list[middle:])

  return merge(left, right)

def merge(left, right):
  sorted_arr = []

  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      sorted_arr.append(left.pop(0))
    else:
      sorted_arr.append(right.pop(0))

  if len(left) == 0:
    sorted_arr = sorted_arr + right

  if len(right) == 0:
    sorted_arr = sorted_arr + left

  return sorted_arr

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

print('selection sort: ', selection_sort(a_list))
print('insertion sort: ', insertion_sort(a_list))
print('quick sort: ', quick_sort(a_list))
print('merge sort: ', merge_sort(a_list))
print(recursive_binary_search(1, range(1, 6)))
print(recursive_binary_search(5, range(1, 6)))
print(recursive_binary_search(7, range(1, 6)))
print(binary_search(1, range(1, 6)))
print(binary_search(5, range(1, 6)))
print(binary_search(7, range(1, 6)))
