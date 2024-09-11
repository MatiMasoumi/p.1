import copy
numbers=[10,12,13]
try:
  res=sum(numbers)
  print('sum:',res)
except TypeError as e:
  print('error sum:',e)


numbers=[2,3,10,23]
try:
  numbers.remove(300)
except ValueError as e:
  print('error removing:',e)

try:
  print(numbers[8])
except IndexError as e:
  print('index error:',e)