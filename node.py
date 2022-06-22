

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