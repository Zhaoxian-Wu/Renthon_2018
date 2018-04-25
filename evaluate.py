import numpy

#######################################################
#
# 评分函数
#
# 必须参数
# houseList    (numpy.array): 房源经纬度, 为nx2矩阵
# utilityList  (numpy.array): 相关设施经纬度，为mx2矩阵
#
# 可选参数
# FindingRadio (float)      : 查找半径(单位：千米)，默认为20
#
# return       (numpy.array): 对每套房源的评分，为nx1矩阵
#
#######################################################
def evaluate(houseList, utilityList, FindingRadio = 20):

  # 返回一栋房屋的评分
  def evaluateOneHouse(longitude, latitude, utilityList, FindingRadio = 20):
    result = 0
    SCORE_PER_UTILITY = 10
    for uti in utilityList :
      if getDistance(
          longitude, latitude, 
          uti[0], uti[1]
        ) <= FindingRadio :
        result += SCORE_PER_UTILITY
    return result

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
  for house in houseList:
    result.append(evaluateOneHouse(
      house[0], 
      house[1], 
      utilityList
    ))
  return numpy.array(result)