import numpy

#######################################################
#
# 规范化函数
# 该函数用于把一个给定的向量转化规范化，使其拥有固定的均值和方差
#
# 必须参数
# vector       (numpy.array): 需要规范化的向量
# mu           (real)       : 需要的均值
# sig          (real)       : 需要的方差
#
# return       (numpy.array): 规范化后的向量
#
#######################################################
def normalize(vector, mu, sig):
  _vector = numpy.array(vector)
  mu_ori  = numpy.mean(_vector)
  sig_ori = numpy.std(_vector)

  a = mu_ori - mu * sig_ori / sig
  b = sig_ori / sig

  _vector = (_vector - a) / b

  return _vector

#######################################################
#
# 标准差计算
# 该函数用于计算一个方差，使用这个方差代入normalize函数规范化后，
# 数据过度偏离均值的可能性被控制在指定范围内
# 例如，给定均值mu = 10,居中比例80%，溢出概率9%，
# 数据波动范围为10×80% = 8
# 则使用生成的方差normalize后，数据不在范围2-18内的概率不超过9%
# （切比雪夫不等式）
#
# 必须参数
# mu                  (real): 给定均值（大于零）
# centerPortion       (real): 居中比例（取值范围0-1）
# overflowProbability (real): 溢出概率（取值范围0-1）
#
# return       (numpy.array): 规范化后的向量
#
#######################################################
def getStd(mu, centerPortion, overflowProbability):
  assert(mu > 0)
  assert(0 <= centerPortion and centerPortion <= 1)
  assert(0 <= overflowProbability and overflowProbability <= 1)
  return numpy.sqrt(overflowProbability) * centerPortion * mu