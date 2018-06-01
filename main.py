from evaluate import evaluate
from normalize import normalize
from normalize import getStd
from scipy.optimize import minimize
import numpy
import os
import pandas
import time

DataList = [
  pandas.read_csv('data/utility/医疗.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/娱乐.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/安全.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/教育.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/交通.csv', delimiter=',', skiprows=0).as_matrix(),
  pandas.read_csv('data/utility/就业.csv', delimiter=',', skiprows=0).as_matrix()
]
FindingRadioList = [
  9.46,
  10.16,
  9.41,
  9.84,
  3.00,
  14.03
]
houseList = pandas.read_csv('data/house.csv', delimiter=',', skiprows=0).as_matrix()

# 居中比重
C = 0.3
# 溢出概率
p = 0.1

# 平均值
mu = 60
# 方差
std = getStd(mu, C, p)

scoreList = []
for i in range(0, len(DataList)):
  score = evaluate(houseList, DataList[i], FindingRadioList[i])
  score = normalize(score, mu, std)
  scoreList.append(score)

# 评分矩阵
A = numpy.vstack(scoreList)
A = numpy.transpose(A)
# 房价
b = houseList[:, 2]
b = normalize(b, mu * A.shape[1], 9 * std)

newDir = 'result/' + time.strftime('%m-%d-%H-%M', time.localtime())
os.mkdir(newDir)
print('结果位置：' + newDir)
columns = ['医疗', '娱乐', '安全', '教育', '交通', '就业']
pandas.DataFrame(columns=columns, data=A).to_csv(newDir + '/A.csv', columns=columns, index=False)
pandas.DataFrame(columns=['findingRadio'], data=FindingRadioList).to_csv(newDir + '/findingRadio.csv', columns=['findingRadio'], index=False)
pandas.DataFrame(columns=['b'], data=b).to_csv(newDir + '/b.csv', columns=['b'], index=False)

# 权重
# 误差函数
def f(x):
  return numpy.linalg.norm(A.dot(x) - b) / numpy.linalg.norm(b)
solution = minimize(f, [1] * A.shape[1], bounds = [[0,None]] * A.shape[1])
x = solution.x
columns = ['weight']
pandas.DataFrame(columns=columns, data=x).to_csv(newDir + '/x.csv', columns=columns, index=False)

# 误差
err = A.dot(x) - b
reer = numpy.linalg.norm(err) / numpy.linalg.norm(b) 
print('相对误差：{0}'.format(reer))

# 相关性分析
_A = A
for i in range(A.shape[1]):
  _A[:,i] = A[:,i] / numpy.linalg.norm(A[:,i])

R = _A.transpose().dot(_A)
print(R)

columns = ['医疗', '娱乐', '安全', '教育', '交通', '就业']
pandas.DataFrame(columns=columns, data=R).to_csv(newDir + '/Relativity.csv', columns=columns, index=False)