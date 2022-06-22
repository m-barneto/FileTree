from logging import root
import sys
from os import listdir
from os.path import isfile

from node import Node


class FileTree():
  def __init__(self, root_path: str):
    self.root = Node(root_path)
    self.generate(self.root)

  def generate(self, node: Node):
    items = listdir(node.get_path())
    for item in items:
      if isfile(node.get_path() + item):
        node.files.append(item)
      else:
        node.children.append(Node(item, node))
    for n in node.children:
      self.generate(n)
  
  def __str__(self) -> str:
      return str(self.root)



if __name__ == "__main__":
  filetree = FileTree(sys.argv[1])
  print(str(filetree))



