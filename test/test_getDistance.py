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

FROM = [
  [23.1123809784,113.3309751406], # 广州塔
  [23.1123809784,113.3309751406] # 广州塔
]

TO = [
  [23.1168609784,113.3310051406], # 海心沙
  [23.1043454041,113.3480714517] # 磨碟沙地铁站
]

REAL = [
  0.561,
  1.9
]

for i in range(0, len(FROM)):
  print("(%12.10lf,%12.10lf) -> (%12.10lf,%12.10lf) : %10.6lf, 百度地图给定值：%10.6lf" % (
    FROM[i][0], FROM[i][1], TO[i][0], TO[i][1], 
    getDistance(FROM[i][0], FROM[i][1], TO[i][0], TO[i][1]),
    REAL[i]
  ))