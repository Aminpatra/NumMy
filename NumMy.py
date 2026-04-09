
class NummyArray:
  def __init__(self, iterable):
    if (isinstance(iterable, list) or isinstance(iterable, tuple)):
      self.shape = self.arr_shape(iterable)
      self.data = list(iterable)
    else: raise ValueError('Only Accepts List/Tuple objects')
    

  def arr_shape(self, iterable, shape = None):

    if shape is None:
      shape = []

    if not (isinstance(iterable, list) or isinstance(iterable, tuple)) or not iterable:
      return shape
    
    shape.append(len(iterable))
    return self.arr_shape(iterable[0], shape)

d0 = ()
d1 = (1,2,3,4)
d2 = [[1,2],
      [3,4]]
d3 = [[[1, 2, 3],
      [1, 2, 3]]]
d4 = [[[[[1,2,3]]]]]
d_not = [[1, 2], [3]]

print('NEW')
arr1 = NummyArray(d0)
arr2 = NummyArray(d1)
arr3 = NummyArray(d2)
arr4 = NummyArray(d3)
arr5 = NummyArray(d4)
arr6 = NummyArray(d_not)

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)
# print(arr4.shape)
# print(arr5.shape)
# print(arr6.shape)
print(arr1.data)
print(arr2.data)
print(arr3.data)
print(arr4.data)
print(arr5.data)
print(arr6.data)
