from __future__ import print_function

from itertools import ifilter

import re


def snake_case(string):
  return re.sub('[A-Z]+', lambda m: '_' + m.group().lower(), string).lstrip('_')

def dashy_caps(string):
  return re.sub('[A-Z]+', lambda m: '-' + m.group(), string).lstrip('-').upper()


class Metaclazz(object):
  def __init__(self, name_mangler=snake_case):
    self.name_mangler = name_mangler

  def __call__(self, name, bases, clazz_dict):
    if '__custom_attr__' not in clazz_dict:
      clazz_dict['__custom_attr__'] = self.name_mangler(name)

    for key, value in ifilter(lambda (k, v): type(v) is DescriptorClazz, clazz_dict.iteritems()):
      value.name = key

    return type(name, bases, clazz_dict)


class DescriptorClazz(object):
  def __set__(self, instance, value):
    self.value = value

  def __get__(self, instance, clazz):
    attr_value = 'attr {}'.format(self.name)
    if instance is not None:
      attr_value += ' with value {}'.format(getattr(self, 'value', None))
    return attr_value


class ClazzA(object):
  __metaclass__ = Metaclazz()

print(ClazzA.__custom_attr__)


class ClazzB(object):
  __metaclass__ = Metaclazz()
  __custom_attr__ = 'something else'

print(ClazzB.__custom_attr__)


class ClazzC(object):
  __metaclass__ = Metaclazz(dashy_caps)
  desc_attr1 = DescriptorClazz()
  desc_attr2 = DescriptorClazz()


c = ClazzC()
c.desc_attr1 = 'something'

print(ClazzC.__custom_attr__)
print(ClazzC.desc_attr1)
print(ClazzC.desc_attr2)
print(c.desc_attr1)
print(c.desc_attr2)
