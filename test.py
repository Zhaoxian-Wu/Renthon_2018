from evaluate import evaluate
from normalize import normalize
from normalize import getStd
import numpy

houseList = numpy.array([
  [113.1, 23.1],
  [113.3, 23.2],
  [113.5, 23.9],
  [112.9, 23.65],
  [113.4, 23.1],
  [113.21, 23.21],
  [112.19, 23.115]
])

utilityList = numpy.array([
  [113.7,   23.63,   10],
  [113.3,   23.124,  10],
  [113.313, 23.124,  14],
  [113.13,  23.1214, 13],
  [113.223, 23.1224, 10],
  [113.2,   23.111,  30]
])

scoreVec = evaluate(houseList, utilityList, 40)
print('规范化前评分：')
print(scoreVec)

# 居中比重
C = 0.8
# 溢出概率
p = 0.2

scoreVec = normalize(scoreVec, 10, getStd(10, C, p))
print('规范化后评分：')
print(scoreVec)