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

total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)

# find the
# sum of all the negative numbers instead of the positive numbers
# in given_list3
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

print("printing total 6")
total6 = 0
i = 0
while given_list3[i] < 0:
    total6 += given_list3[i]
    i += 1
print(total6)


# as long as i is less than the length of the array, the loop will continue
total10 = 0
i = 0
while i < len(given_list3):
    # the if statement checks each value in the array and see if it is less than zero, if it is less than zero, it adds it to the total.
    if given_list3[i] <= 0:
        total10 += given_list3[i]
# i goes up 1 regardless if the if statement is true or false.
    i += 1
print(total10)
