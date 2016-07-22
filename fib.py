#! /usr/bin/python
#
def fib(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
      cidx = len(fib_sequence) - 1
      current_val = fib_sequence[cidx]
      new_val = current_val + fib_sequence[cidx - 1]
      fib_sequence.append(new_val)

    return fib_sequence
print fib(10)

def fib_generator(n):
  a, b, start = 0, 1, 0

  while start < n:
    start += 1
    yield a
    a, b = b, a + b
  # generator comprehension
  print (x for x in fib_generator(10))
