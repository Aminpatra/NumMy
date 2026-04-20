
from math import prod

class NummyArray:
  # Layer 1
  def __init__(self, iterable):

    if (self.__valid_input(iterable)):

      if (self.__arr_type(iterable)):

        shape = self.__arr_shape(iterable)
        self.iterable = iterable
        self.shape = tuple(shape) if shape else (0,)
        self.data = list(self.__flatten(iterable))
        self.ndim = len(self.shape)
        self.size = prod(self.shape)
        self.dtype = type(self.data[0]) if self.data else None
      
      else: raise ValueError('Elements Should Have The Same Data Type')

    else: raise ValueError('Only Accepts List/Tuple Objects')

  def __repr__(self):
    return (f"NumMyArray({self.iterable}), "
            f"shape={self.shape}, "
            f"ndim={self.ndim}, "
            f"dtype={self.dtype.__name__}")
  
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

  def __arr_shape(self, iterable, shape = None):

    if shape is None:
      shape = []

    if not iterable:
      return shape

    if not (self.__valid_input(iterable)):
      return shape
    
    shape.append(len(iterable))
    return self.__arr_shape(iterable[0], shape)
  

  def __arr_type(self, iterable):
    
    data = self.__flatten(iterable)
    if data:
      type1 = type(data[0])
      for element in data:
        if type(element) != type1:
          return False
    return True
  
  # Layer 2
  @classmethod
  def array(cls, iterable):
    return NummyArray(iterable)
  

  @staticmethod
  def __generate(shape, fill):
    
    if isinstance(shape, int):
      rows = cols = shape
    
    elif isinstance(shape, tuple):
      if len(shape) != 2:
        raise ValueError("Only 2D shapes supported")
      rows, cols = shape
    
    else:
      raise TypeError("Shape must be int or tuple")
    
    matrix = [[fill for _ in range(cols)] for _ in range(rows)]
    return matrix
  
  # TODO: try to make it support more than 2D shapes
  @classmethod
  def zeros(cls, shape):

    return cls(cls.__generate(shape, 0))
  
  @classmethod
  def ones(cls, shape):

    return cls(cls.__generate(shape, 1))


  @classmethod
  def full(cls, shape, fill):
    
    return cls(cls.__generate(shape, fill))



d0 = NummyArray([[], []])
d1 = NummyArray([1, 2, 1])
d1_2 = NummyArray.array([[2, 4], 
                        [2, 4], 
                        [3, 1]])
d2 = NummyArray([
                [1, 2], 
                [3, 4]
                ])
d3 = NummyArray([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(d1_2)

# zeros = NummyArray.zeros(2)

# ones = NummyArray.ones()
# print(ones)
# print(zeros)
# print(d0.data)
# print(d1.shape)
# print(d2.shape)
# print(d3.dtype)

# d5 = NummyArray.array([1, 2])
# print(d5)

full = NummyArray.full(2, 10)
print(full)