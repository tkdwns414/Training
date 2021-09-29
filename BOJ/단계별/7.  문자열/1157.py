n = input().upper()

ls = []
for i in range(ord("A"), ord("Z") + 1):
    ls.append(0)
for s in n:
    ls[ord(s) - ord("A")] += 1

if ls.count(max(ls)) > 1:
    print("?")
else:
    print(chr(ls.index(max(ls)) + ord("A")))
