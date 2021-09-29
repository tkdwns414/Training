# 삽입정렬, 버블정렬 이용하는 문제
import sys

# 삽입 정렬
def insertionsort(ls, n):
    for i in range(1, n):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key


# 버블 정렬
def bubblesort(ls, n):
    for i in range(n):
        for j in range(n - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


n = int(sys.stdin.readline())
ls = []

for i in range(n):
    ls.append(int(sys.stdin.readline()))

bubblesort(ls, n)
# insertionsort(ls,n)

for item in sorted(ls):
    sys.stdout.write(str(item) + "\n")