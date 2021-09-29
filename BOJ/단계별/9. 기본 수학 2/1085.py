x, y, w, h = map(int, input().split())
"""
dis_x = w - x if w - x < x else x
dis_y = h - y if h - y < y else y
dis = dis_x if dis_x < dis_y else dis_y
print(dis)
"""
print(min(x, y, w - x, h - y))
