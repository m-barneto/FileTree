from logging import root
import sys
from os import listdir
from os.path import isfile

from node import Node


class FileTree():
  def __init__(self, root_path: str):
    # Create the root node using the provided directory path
    self.root = Node(root_path)
    # Start the recursive generate method on the root node
    self.generate(self.root)

  def generate(self, node: Node):
    """
    Fills out the passed in node's children

    This is a recursive method that will
    call itself on the passed in node's 
    children as well.
    """
    # Get all directories and files under the node
    items = listdir(node.get_path())
  
    # Loop through all the items
    for item in items:
      if isfile(node.get_path() + item):
        # If the item is a file, add it to the base node's files list
        node.files.append(item)
      else:
        # Otherwise, if it's a directory, initialize it as a new node and add it to the base node's children list
        node.children.append(Node(item, node))
    
    # Loop through the children of the base node and call the generate method recursively
    for n in node.children:
      self.generate(n)
  
  def __str__(self) -> str:
      return str(self.root)



if __name__ == "__main__":
  # Initialize filetree with the argument containing the path of the directory to list
  filetree = FileTree(sys.argv[1])
  print(str(filetree))



