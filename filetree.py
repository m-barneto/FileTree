from logging import root
import sys
from os import listdir
from os.path import isfile, join

class Node():
  def __init__(self, location, parent=None):
    self.parent = parent
    self.children = []
    self.files = []
    self.location = location
    if self.parent is None:
      self.depth = 0
    else:
      self.depth = self.parent.depth + 1
  
  def get_path(self):
    path = ""
    if self.parent:
      path += self.parent.get_path()
    return path + self.location + "\\"

  def __str__(self) -> str:
      baseDir = ""
      for i in range(self.depth):
        baseDir += "--"
      baseFile = ""
      for i in range(self.depth + 1):
        baseFile += "--"
      value = baseDir + self.location
      for dir in self.children:
        value += "\n" + baseDir + str(dir)
      
      for file in self.files:
        value += "\n" + baseFile + file
      
      return value
      
  

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



