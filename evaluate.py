import numpy

#######################################################
#
# 评分函数
#
# 必须参数
# houseList    (numpy.array): 房源经纬度, 为nx2矩阵
# utilityList  (numpy.array): 相关设施经纬度，为mx3矩阵,
#                             前两列为经纬度，最后一列为评分
#
# 可选参数
# FindingRadio (float)      : 查找半径(单位：千米)，默认为20
#
# return       (numpy.array): 对每套房源的评分，为nx1矩阵
#
#######################################################
def evaluate(houseList, utilityList, FindingRadio = 20):

  # 返回一栋房屋的评分
  # 评分 = 求和（范围内每个设施的评分 / 房屋到该设施的距离）
  def evaluateOneHouse(longitude, latitude, utilityList, FindingRadio = 20):
    result = 0
    distSum = 0
    for uti in utilityList :
      distance = getDistance(
          longitude, latitude, 
          uti[0], uti[1]
        )
      if distance < 0.01:
        distance = 0.01
      distSum += distance
      if distance <= FindingRadio :
        result += uti[2] / distance
    return result, distSum / utilityList.shape[0]

  # 计算距离
  # 算法来源：https://blog.csdn.net/u013401853/article/details/73368850
  def getDistance(longitude_1, latitude_1, longitude_2, latitude_2):
    from math import sin, asin, cos, radians, fabs, sqrt
    EARTH_RADIUS=6371           # 地球平均半径，6371km

    def hav(theta):
      s = sin(theta / 2)
      return s * s

    # 经纬度转换成弧度
    longitude_1 = radians(longitude_1)
    longitude_2 = radians(longitude_2)
    latitude_1 = radians(latitude_1)
    latitude_2 = radians(latitude_2)

    dlng = fabs(latitude_1 - latitude_2)
    dlat = fabs(longitude_1 - longitude_2)
    h = hav(dlat) + cos(longitude_1) * cos(longitude_2) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance

  result = []
  dist = 0
  count = 0
  for house in houseList:
    score, _dist = evaluateOneHouse(
      house[0], 
      house[1], 
      utilityList,
      FindingRadio
    )
    count = count + 1
    if count % 1000 == 0 :
      print('已评价{0}套房屋'.format(count))
    result.append(score)
    dist += _dist
  print('平均长度:{0}'.format(dist / houseList.shape[0]))
  return numpy.array(result)