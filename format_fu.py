from __future__ import print_function

class O(object):
  def __init__(self):
    self.array = list(x for x in range(10))

  @property
  def size(self):
    return len(self.array)

  def __getitem__(self, i):
    return self.array[i]

x = O()
x.what_it_is = 'a value of note'

print("{x} is {x.what_it_is} with {x.size} elements and the 3rd one is {x[2]}.".format(**locals()))
