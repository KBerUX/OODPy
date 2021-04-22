# can you compute all multiples of 3, 5
# that are less than 100?
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
