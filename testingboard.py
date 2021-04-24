given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

print("printing total 6")
total6 = 0
i = 0
while given_list3[i] < 0:
    total6 += given_list3[i]
    i += 1
print(total6)


total10 = 0
i = 0
while i < len(given_list3):
    if given_list3[i] <= 0:
        total10 += given_list3[i]
    i += 1
print(total10)
