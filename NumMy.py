
from math import prod

class NummyArray:
  def __init__(self, iterable):
    if (isinstance(iterable, list) or isinstance(iterable, tuple)):
      shape = self.arr_shape(iterable)
      self.shape = tuple(shape) if shape else (0,)
      self.data = list(iterable)
      self.ndim = len(self.shape)
      self.size = prod(self.shape)
      self.type = self.arr_type(iterable) if self.size else "float64"
    else: raise ValueError('Only Accepts List/Tuple objects')
    

  def arr_shape(self, iterable, shape = None):

    if shape is None:
      shape = []

    if not iterable:
      return shape

    if not (isinstance(iterable, list) or isinstance(iterable, tuple)):
      return shape
    
    shape.append(len(iterable))
    return self.arr_shape(iterable[0], shape)
  
  def arr_type(self, iterable):

    
    if not (isinstance(iterable, list) or isinstance(iterable, tuple)):
      return type(iterable)

    return self.arr_type(iterable[0])
  
# d__1 = "string"
d0 = ()
d1 = (1,2,3,4)
d2 = [[1.0,2.2],
      [3.4,4.4]]
# d3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# d4 = [[[[[1,2,3]]]]]
# d_not = [[1, 2], [3]]

# print('NEW')
# s = NummyArray(d__1)
arr1 = NummyArray(d0)
arr2 = NummyArray(d1)
arr3 = NummyArray(d2)
# arr4 = NummyArray(d3)
# arr5 = NummyArray(d4)
# arr6 = NummyArray(d_not)

print(arr3.type)

# print(arr1.size)
# print(arr2.shape)
# print(arr3.shape)
# print(arr4.shape)
# print(arr5.shape)
# print(arr6.shape)
# print(arr1.data)
# print(arr2.data)
# print(arr3.data)
# print(arr4.data)
# print(arr5.data)
# print(arr6.data)

# print(arr1.size)
# print(arr1.shape)
# print(arr2.size)
# print(arr3.size)
# print(arr4.shape)
# print(arr4.data)
# print(arr4.ndim)
# print(arr4.size)
# print(arr4.size)
# print(arr4.type)
# print(arr5.size)
# print(arr6.size)


# a = NummyArray([[1, 2], [3, 4]])
# print(a.data)