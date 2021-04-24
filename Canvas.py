# for loop
# can you compute all multiples of 3, 5
# that are less than 100?
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# while loop
# while loops are useful when you don't know how many loops you need beforehand.


total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
    print(total2)


# this while loop only takes in positive numbers and adds them u.
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)


given_list2 = [5, 4, 4, 3, 1, -2, -3, 5]
total4 = 0
# for loop to add only the positive values
for element in given_list2:
    # if element is less than or equal to zero, it will "break" out of the loop and stop
    if element <= 0:
        break
    total4 += element
    print(element)
print(total4)
# this will print 17, the sum of all the positive numbers in given_list2.
