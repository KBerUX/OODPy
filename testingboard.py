
nums = [2, 7, 11, 15]
total = 0
i = 0
while True:
    total += nums[i]
    i += 1
    if nums[i] > 2:
        break
    print(total)
