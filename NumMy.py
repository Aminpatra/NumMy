
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
  

a = NummyArray([1,2])
print(a.data)
  
  