

class Node():
  def __init__(self, name, parent=None):
    self.parent = parent
    self.name = name

    self.children = []
    self.files = []
    
    if self.parent is None:
      # If there is no parent, then this Node must be the root, depth is 0 here
      self.depth = 0
    else:
      # Otherwise, set the depth equal to the parent's depth + 1
      self.depth = self.parent.depth + 1
  
  
  def get_path(self):
    """
    Returns the full path to the node.

    This is a recursive method and will
    call itself on the parent node until 
    it reaches the root node of the tree
    """
    path = ""
    if self.parent:
      path += self.parent.get_path()
    return path + self.name + "\\"

  def __str__(self) -> str:
    """
    Returns a string representation of this node's children.
    """
    value = ""
    for i in range(self.depth):
      if i == self.depth - 1:
        value += "┣━"
      else:
        value += " "
    
    value += self.name
    
    for dir in self.children:
      value += "\n" + str(dir)
    
    return value