#! /usr/bin/python

class AlphabetCipher:
  def __init__(self, alphabet, keyword):
    self.alphabet = list(alphabet)
    self.keyword = keyword
    self.grid = self.__make_grid()

  def encode(self, message):
    cycled_keyword = self.__cycle(self.keyword, len(message))

    return ''.join(map(self.__encode_single_char, list(cycled_keyword), list(message)))

  def decode(self, encrypted_message):
    cycled_keyword = self.__cycle(self.keyword, len(encrypted_message))

    return ''.join(map(self.__encode_single_char, list(cycled_keyword), list(encrypted_message)))

  def __make_grid(self):
    return reduce(self.__set_rotated_key, self.alphabet, {})

  def __set_rotated_key(self, memo, char):
    idx = self.alphabet.index(char)
    memo[char] = self.alphabet[idx:] + self.alphabet[:idx]

    return memo

  def __cycle(self, string, length):
    if length < len(string):
      return

    remainder = length % len(string)
    times = length / len(string) - 1
    cycled_string = list(string)

    [cycled_string.append(string) for x in range(times)]
    [cycled_string.append(string[idx]) for idx in range(remainder)]

    return ''.join(cycled_string)

  def __encode_single_char(self, column_char, row_char):
    return self.grid[column_char][self.alphabet.index(row_char)]

  def __decode_single_char(self, column_char, row_char):
    return ''

cipher = AlphabetCipher(alphabet="abc", keyword="bc")
encoded_message = cipher.encode(message='cabba')
print('encoded message: ' + encoded_message, 'decoded message: ' + cipher.decode(encoded_message))
