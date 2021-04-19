# this would read the information in the file
tryexcept_file = open("tryexcept.py", "r")

# this would tell us whether or not we can read from this file. Boolean value
# True means you can read it
print(tryexcept_file.readable())

# this would spit out the information in the file
print(tryexcept_file.read())

# would allow me to read the first line
# replicating this would read the next file
print(tryexcept_file.readline())

# would take each line and put it an array
print(tryexcept_file.readlines())
# making it easier to identify what line you want. simply just use it in array
print(tryexcept_file.readlines()[1])


# this would change the file
tryexcept_file = open("tryexcept.py", "w")

# this would append the information in the file. you can add information to the file
tryexcept_file = open("tryexcept.py", "a")

# this would let me read and write in the file
tryexcept_file = open("tryexcept.py", "r+")

# this would close the file afterwards. good to close the file every time
tryexcept_file.close()
