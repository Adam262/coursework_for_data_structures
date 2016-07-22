#! /usr/bin/python

class BinaryTree:
  def __init__(self, root):
    self.root = root
    self.left_child = None
    self.right_child = None

  def insert_left(self, node):
    new_tree = BinaryTree(node)

    if self.left_child == None:
      self.left_child = new_tree
    else:
      new_tree.left_child = self.left_child
      self.left_child = new_tree
    return self

  def insert_right(self, node):
    new_tree = BinaryTree(node)

    if self.right_child == None:
      self.right_child = new_tree
    else:
      new_tree.right_child = self.right_child
      self.right_child = new_tree
    return self

  def get_left(self):
    return self.left_child

  def get_right(self):
    return self.right_child

  def set_root(self, root):
    self.root = root
    return self

  def get_root(self):
    return self.root

tree = BinaryTree(5).insert_left(4).insert_left(3)
print(tree.get_left().get_root())


