from evaluate import evaluate
from normalize import normalize
from normalize import getStd
import numpy
import os
import pandas
import time

DataList = [
  pandas.read_csv('data/utility/医疗.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/娱乐.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/安全.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/教育.csv', delimiter=',', skiprows=0).as_matrix()
]
FindingRadioList = [
  10.62,
  11.25,
  10.53,
  10.99
]
houseList = pandas.read_csv('data/house.csv', delimiter=',', skiprows=0).as_matrix()

# 居中比重
C = 0.8
# 溢出概率
p = 0.2
# 平均值
mu = 60
scoreList = []
for i in range(0, len(DataList)):
  score = evaluate(houseList, DataList[i], FindingRadioList[i])
  score = normalize(score, mu, getStd(mu, C, p))
  scoreList.append(score)

# 评分矩阵
A = numpy.vstack(scoreList)
A = numpy.transpose(A)
# 房价
b = houseList[:, 2]

newDir = 'result/' + time.strftime('%m-%d-%H-%M', time.localtime())
os.mkdir(time.strftime(newDir))
columns = ['医疗', '娱乐', '安全', '教育']
pandas.DataFrame(columns=columns, data=A).to_csv(newDir + '/A.csv', columns=columns, index=False)
pandas.DataFrame(columns=['findingRadio'], data=FindingRadioList).to_csv(newDir + '/findingRadio.csv', columns=['findingRadio'], index=False)
pandas.DataFrame(columns=['b'], data=b).to_csv(newDir + '/b.csv', columns=['b'], index=False)

# 权重
x = numpy.linalg.pinv(A).dot(b)
columns = ['weight']
pandas.DataFrame(columns=columns, data=x).to_csv(newDir + '/result.csv', columns=columns, index=False)

# 误差
err = A.dot(x) - b
reer = numpy.linalg.norm(err) / numpy.linalg.norm(b) 