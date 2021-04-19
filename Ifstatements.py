is_male = True

# under the if statement will be executed if that condition
# is true
is_male = True
is_tall = True

# if the person is either male or they are tall
# only will be true if one of the values is true
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male or tall")

#Else is 'otherwise'

if is_male and is_tall:
    print()
    # elif stands for elseif
    # using 'not' negates it if is_tall is true it is false and the other way as well

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_tall and not(is_male):
    print("You are a tall female")
else:
    print("You are not male and not tall")
