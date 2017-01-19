#! /usr/bin/python

class AlphabetCipher:
  def __init__(self, alphabet, keyword):
    self.alphabet = list(alphabet)
    self.keyword = keyword
    self.grid = reduce(self.__make_grid, self.alphabet, {})

  def encode(self, message):
    cycled_keyword = self.__cycle(self.keyword, len(message))

    return ''.join(map(self.__encode_single_char, list(cycled_keyword), list(message)))

  def decode(self, encrypted_message):
    cycled_keyword = self.__cycle(self.keyword, len(encrypted_message))

    return ''.join(map(self.__decode_single_char, list(cycled_keyword), list(encrypted_message)))

  def deciper(self, message, encrypted_message):
    if len(message) == len(encrypted_message):
      cycled_keyword = ''.join(map(self.__decipher_single_char, message, encrypted_message))
      base = ""

      for char in cycled_keyword:
        base += char
        if self.__cycle(base, len(cycled_keyword)) == cycled_keyword:
          return base

  def __decipher_single_char(self, message_char, encrypted_message_char):
    return [key for key in self.grid if self.grid[key].index(encrypted_message_char) == self.alphabet.index(message_char)][0]

  def __make_grid(self, memo, char):
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
    return self.alphabet[self.grid[column_char].index(row_char)]

cipher = AlphabetCipher(alphabet="abc", keyword="bc")
encoded_message = cipher.encode(message='cabba')
print('encoded message: ' + encoded_message, 'decoded message: ' + cipher.decode(encoded_message))
print('cipher', cipher.deciper('cabba', encoded_message))

cipher = AlphabetCipher(alphabet="abcdefghijklmnopqrstuvwxyz", keyword="vigilance")
encoded_message = cipher.encode(message='meetmeontuesdayeveningatseven')
print('encoded message: ' + encoded_message, 'decoded message: ' + cipher.decode(encoded_message))
print('cipher', cipher.deciper('meetmeontuesdayeveningatseven', encoded_message))
