actual_cat = "Ming"
cat_name = " "
name_count = 0
name_limit = 5
correctName = False

while cat_name != actual_cat and not(correctName):
    if name_count < name_limit:
        cat_name = input("Please type another cat name!: ")
        name_count += 1
    else:
        correctName = True

if correctName:
    print("You LOSE!! no more guesses")
else:
    print("You win!!")
