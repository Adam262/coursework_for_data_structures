#! /usr/bin/python
#
class BinaryHeap:
  def __init__(self):
    self.heap_list = [0] # do not init empty
    self.current_size = 0

  def insert(self, node):
    self.heap_list.append(node)

  def find_min(self):
    print 'foo'

  def delete_min(self):
    print 'foo'

  def size(self):
    return len(self.help_list)

  def is_empty(self):
    return len(self.heap_list) == 0

  def build_heap_list(self, list):
    print 'foo'

  def foo(self):
    return self.__perc_up()

  def __perc_up(self):
    print 'foo'

  def __perc_down(self):
    print 'foo'

  def __min_child(self):
    print 'foo'

print BinaryHeap().foo()
