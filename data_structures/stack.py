class Stack():
  def __init__(self):
    self.data = []

  def push(self, el):
    self.data.append(el)

  def pop(self):
    return self.data.pop()

  def peek(self):
    if len(self.data) != 0:
      return self.data[len(self.data) - 1]

  def data(self):
    return self.data

  def is_empty(self):
    return len(self.data) == 0

  def size(self):
    return len(self.data)

def rev_string(str):
  stack = Stack()
  list = []

  for char in str:
    stack.push(char)

  for n in range(0, stack.size()):
    list.append(stack.pop())

  return ''.join(list)

stack = Stack()
stack.push(5)
stack.push(6)
stack.pop()
print stack.peek()
print rev_string('abcde')

def is_balanced(str):
  balanced = True
  stack = Stack()
  open, closed = '[{(', ']})'

  if len(str) == 0:
    return balanced
  else:
    str_list = list(str)

    for char in str_list:
      if char in open:
        stack.push(char)
      if char in closed:
        closed_idx = closed.index(char)

        if stack.size() > 0 and closed_idx == open.index(stack.peek()):
          stack.pop()
        else:
          balanced = False

    if stack.size() > 0:
      balanced = False

  return balanced

print is_balanced('{[()]}')
print is_balanced('()[]')
print is_balanced('{[(]})')
print is_balanced('}{')
print is_balanced('')
  # input: str
  # output: boolean
  # open = '[{('
  # closed = ']})'
  # stack = Stack()
  # [] => true
  # [({})] => true
  # []{}() => true
  # ][ => false
  # (] => false
  # given string
  # split into list
  # for each char
  #   if open?, push to stack
  #   if closed?
  #     if top of stack is corresponding open, pop stack
  #     else return false
  # at end of list
  #   if stack is empty, return true
  #   else return false
