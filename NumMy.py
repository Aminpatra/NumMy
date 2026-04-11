
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
        self.type = self.arr_type(iterable)
      
      else: raise ValueError('Elements Should Have The Same Data Type')

    else: raise ValueError('Only Accepts List/Tuple Objects')
    
  
  def __valid_input(self, iterable):
    return isinstance(iterable, list) or isinstance(iterable, tuple)
  
  def __flatten(self, iterable):
    data = []


    # if iterable:
    #   if self.__valid_input(iterable) and not self.__valid_input(iterable[0]):
    #     for element in iterable:
    #       data.append(element)
    #   return self.__flatten(iterable[0])
    
    # else:
    #   return data

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

    if iterable:
      try:
        if (self.__valid_input(iterable) and not self.__valid_input(iterable[0])):
          # if it is not an empty iterable
            first_element_type = type(iterable[0])
            for i in range(len(iterable)):
              for element in iterable[i]:
                if (type(element) != first_element_type):
                  return False
      except:
        print(iterable)
        
    else:
      return None

    if not (self.__valid_input(iterable)):
      return type(iterable)

    return self.arr_type(iterable[0])
  

a = NummyArray([[1, 2], [3, 0.1]])
print(a.data)
  
  
# d__1 = "string"
# d0 = (1, 1)
# d1 = []
# d2 = [[1.0,2.2],
#       [3.4,4.4]]
# d3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# d4 = [[[[[1,2,3]]]]]
# d_not = [[1, 2], [3]]

# print('NEW')
# s = NummyArray(d__1)
# arr1 = NummyArray(d0)
# arr2 = NummyArray(d1)
# arr3 = NummyArray(d2)
# arr4 = NummyArray(d3)
# arr5 = NummyArray(d4)
# arr6 = NummyArray(d_not)

# print(arr1.type)

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


# Limitations of this library
# 1- can't accept [[1, 2], [1]], unbalanced arrays