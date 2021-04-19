# ask for name
# how old are you?
# if not old enough --> can't play game
# if old enough, can play game!
user_name = input("What is your name? :")
age = int(input("What is your age? :"))
game_response = 0
game_ask_limit = 3
play = True

if age <= 5:
    print("I am sorry, you are too young to play :(")
elif age > 5:
    game = input(user_name + " Do you want to play this game?: ")
    if game in {"yes", "Yes"}:
        print("let's begin " + user_name)
    else:
        while game != {"yes", "Yes"} and (game_response <= game_ask_limit):
            game = input("are you sure?: ")
            game_response += 1
        if game == {"yes", "Yes"}:
            print("let's begin " + user_name)
        else:
            print("Okay, :(,that's fine then!")
