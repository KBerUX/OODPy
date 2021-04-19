# usually we create a list and just have
# the attributes
# however, we will have lists in the number_grid
# lists within the list number_grid essentially

# we can create grid-like structure within python
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])


# nested for loop - for loop inside of a for loop
for row in number_grid:
    for column in row:
        print(column)
