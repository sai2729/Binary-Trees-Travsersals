# -*- coding: utf-8 -*-

class Node(object):
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BinaryTree(object):
  def __init__(self,root):
    self.root = Node(root)

  def print_tree(self,trav_type):
    if trav_type=='preorder':
      return self.pre_order_traversal(tree.root,'')
    elif trav_type=='Inorder':
      return self.In_order_traversal(tree.root,'')
    elif trav_type=='Postorder':
      return self.Post_order_traversal(tree.root,'')
    else:
      print('Invalid Traversal type')

  def pre_order_traversal(self,start,travstr):
    if start:                                                    # Root -> Left -> Right
      travstr=travstr+str(start.data)+'-'                 
      travstr=self.pre_order_traversal(start.left,travstr)                            
      travstr=self.pre_order_traversal(start.right,travstr)
    return travstr

  def In_order_traversal(self,start,travstr):
    if start:                                                       # Left -> Root -> Right
      travstr=self.In_order_traversal(start.left,travstr)
      travstr=travstr+str(start.data)+'-'
      travstr=self.In_order_traversal(start.right,travstr)
    return travstr
  
  def Post_order_traversal(self,start,travstr):
    if start:                                                  # Left -> Right -> Root
      travstr=self.Post_order_traversal(start.left,travstr)
      travstr=self.Post_order_traversal(start.right,travstr)
      travstr=travstr+str(start.data)+'-'
    return travstr

tree=BinaryTree(1)            
tree.root.left=Node(2)
tree.root.right=Node(3)                                            1
tree.root.left.left=Node(4)                                     /      \
tree.root.left.right=Node(5)                                   2        3
tree.root.right.left=Node(6)                                 /   \     /  \
tree.root.right.right=Node(7)                               4    5    6    7

print(tree.print_tree('preorder'))
print(tree.print_tree('Inorder'))
print(tree.print_tree('Postorder'))