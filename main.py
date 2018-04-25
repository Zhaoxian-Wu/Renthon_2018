from evaluate import evaluate
import numpy

houseList = numpy.array([
  [113.1, 23.1],
  [113.3, 23.2],
  [113.5, 23.9]
])
utilityList = numpy.array([
  [113.7, 23.63],
  [113.3, 23.124],
  [113.3123, 23.124],
  [113.13, 23.1214],
  [113.223, 23.1224],
  [113.2, 23.111]
])
# print(evaluate(houseList, utilityList))

from evaluate import getDistance
for i in houseList:
  print(getDistance(i[0], i[1], utilityList[0][0], utilityList[0][1]))