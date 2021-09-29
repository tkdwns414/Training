# 택시 기하학의 원은 반지름이 n이라고 하면 한 변의 길이가 n*(root 2)인 정사각형이 나온다?
from math import pi

n = int(input())

print("%.6f" % ((n ** 2) * pi))
print("%.6f" % ((n ** 2) * 2))
