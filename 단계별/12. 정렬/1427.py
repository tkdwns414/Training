num = input()
nums = []

for i in range(len(num)):
    nums.append(num[i])
nums.sort(reverse=True)
print("".join(nums))