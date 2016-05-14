# TODO: Draw a UML diagram showing the relationships among Node, Directory, and File.
class Node(object):
  def __init__(self, id):
    self._id = id

  def id(self):
    return self._id

class Directory(Node): # inheritance used here
  def __init__(self, id):
    Node.__init__(self, id)

    self._elements = [] # composition used here

  # adds directory or file to this directory
  def add(self, element):
    self._elements.append(element)

  # lists elements in the directory
  def ls(self):
    for e in self._elements:
      print e.id()

class File(Node): # inheritance used here
  def __init__(self, id):
    Node.__init__(self, id)

    self._contents = ''

  # writes contents into this file
  def write(self, contents):
    self._contents = contents

  # outputs the contents of this file
  def cat(self):
    print self._contents

# create root directory
root = Directory('/')

# create a subdirectory of root
subdir1 = Directory('subdir1')
root.add(subdir1)

# create another subdirectory of root
subdir2 = Directory('subdir2')
root.add(subdir1)

# create a file under the first subdirectory of root
file = File('file')
subdir1.add(file)
file.write('contents')

# output contents of file, root, and the first subdirectory
file.cat()
root.ls()
subdir1.ls()
