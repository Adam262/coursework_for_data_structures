def anagrams(list, str):
  str = __sort(str)

  return [item for item in list if __sort(item) == __sort(str)]

def anagram_one(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    matches = True
    i = 0
    s1, s2, = __sort(s1), __sort(s2)

    while(matches and i < len(s1)):
      if (s1[i] == s2[i]):
        i = i + 1
      else:
        matches = False

  return matches

def anagram_two(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    s2 = list(s2)
    is_anagram = True

    for char in s1:
      if char in s2:
        s2[s2.index(char)] = None
      else:
        is_anagram = False

  return is_anagram

def anagram_three(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    matches = True
    hash_one, hash_two = {}, {}

    for item in list(s1):
      if item in hash_one:
        hash_one[item] = hash_one[item] + 1
      else:
        hash_one[item] = 1

    for item in list(s2):
      if item in hash_two:
        hash_two[item] = hash_two[item] + 1
      else:
        hash_two[item] = 1

    for key in hash_one:
      if key in hash_two and (hash_one[key] != hash_two[key]):
        matches = False

    for key in hash_two:
      if key in hash_two and (hash_one[key] != hash_two[key]):
        matches = False

  return matches

def __sort(str):
  return ''.join(sorted(str))


print(anagrams(['ab', 'cba', 'abc', 'ca'], 'bac'))
print(anagram_one('abc', 'cba'))
print(anagram_one('abc', 'cdba'))
print(anagram_two('abc', 'cba'))
print(anagram_two('abc', 'cdba'))
print(anagram_three('abc', 'cba'))
print(anagram_three('abc', 'cdba'))
