
from math import prod

class NummyArray:
  def __init__(self, iterable):

    if (self.__valid_input(iterable)):

      if (self.arr_type(iterable)):

        shape = self.arr_shape(iterable)
        self.shape = tuple(shape) if shape else (0,)
        self.data = list(self.__flatten(iterable))
        self.ndim = len(self.shape)
        self.size = prod(self.shape)
        self.dtype = type(self.data[0]) if self.data else None
      
      else: raise ValueError('Elements Should Have The Same Data Type')

    else: raise ValueError('Only Accepts List/Tuple Objects')
    
  
  def __valid_input(self, iterable):
    return isinstance(iterable, list) or isinstance(iterable, tuple)
  

  def __flatten(self, iterable, data = None):
    
    if data is None:
      data = []
    
    if iterable:
      for element in iterable:
        if not self.__valid_input(element):
          data.append(element)
        else: 
          self.__flatten(element, data)
    return data

  def arr_shape(self, iterable, shape = None):

    if shape is None:
      shape = []

    if not iterable:
      return shape

    if not (self.__valid_input(iterable)):
      return shape
    
    shape.append(len(iterable))
    return self.arr_shape(iterable[0], shape)
  

  def arr_type(self, iterable):
    
    data = self.__flatten(iterable)
    if data:
      type1 = type(data[0])
      for element in data:
        if type(element) != type1:
          return False
    return True




d0 = NummyArray([[], []])
d1 = NummyArray([1, 2, 1])
d2 = NummyArray([[1, 2], [3, 4]])
d3 = NummyArray([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(d0.data)
print(d1.data)
print(d2.data)
print(d3.data)

print(d0.dtype)
print(d1.dtype)
print(d2.dtype)
print(d3.dtype)