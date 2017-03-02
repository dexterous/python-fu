from __future__ import print_function


from contextlib import contextmanager


class abandon():
  def __enter__(self):
    pass

  def __exit__(self, *args):
    print('=' * 80)
    for arg in args:
      print("-- {} --".format(arg))
    print('=' * 80)
    return True


with abandon():
  print("I'm telling the truth")
  raise Exception, 'Maybe not!'


print('#' * 80)


@contextmanager
def caution():
  try:
    yield
  except Exception as x:
    print(x.message)

  with abandon():
    yield


with caution():
  print("I'm telling the truth")
  raise Exception, 'Honest!'
