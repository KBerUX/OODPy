lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "John", "Oscar", "Timmy", "Allie"]
friends.extend(lucky_numbers)
friends.append("Bitty")
friends.insert(1, "Kelly")
friends.remove("Oscar")
friends.pop()
print(friends)

print(friends.index("Kevin"))
print(friends.count("John"))
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)

lucky_numbers[1] = 2
print(lucky_numbers)
