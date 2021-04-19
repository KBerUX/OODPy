# dictionaries allow us to store information
# in key value pairs
# the word is the key which allows us to uniquely identify it in the dictionary

# you create a dictionary in python
# you use open and closed curly brackets
# inside the dictionary you can define a key
# and then give it a value
# the keys in the dictionary must be unique
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Nov"])
print(month_conversions.get("Luv", "Not a valid Key"))
