# Strings and stuff
# immutable collection of characters
# letters, numbers, spaces, special characters

language = "Python"
# this will give attribute errors
# language.add(" is cool")
# language.append(" is cool")
# language.remove("n")

# we can index into strings
print(language[1])
# but we cannot change what is at that index
# language[1] ="i" TypeError

#                 concatenation - combing to strings to a new variable
# language = language + " is cool"
# print(language)

new_language = language[0] + "i" + language[2:]
print(new_language)

# indexing into a string
print(language[3])
letter = language[3]
print(letter)

# -1 still the last index
print(language[-1])
print(language[-2]) #second to last index

# iterating through a string with a for loop
track = "Marathon"
# loop prints each character in track
for letter in track:
    print(letter)

half_track = "half marathon"
# with spaces, it still prints each character, including the space
for letter in half_track:
    print(letter)

# for letter in half_track:
#     if letter == " ":
#         continue <----- continue will skip over the space
#     print(letter)

# splitting a string into a list wiht .split()
# our_string.split("separator") #often a space
track_list = half_track.split()
print(track_list)
for word in track_list: # half_track.split() this could also be looped through
    print(word)

# Slicing a string
field = "Touchdown"

# slicing field to just get Touch
play_one = field[:5]
print(play_one)
# slicing field to get down
play_two = field[5:]

# Create a review preview or something like, and only show the first 30 characters
# after the thirty is a ...
review = "This product was really good. I put it in my hair and its never felt so soft and luscious"
print(review[:31])

almost_noodles = field[2::3]
print(almost_noodles)

# Iterating with a slice
game_plan = "Execute play number 9"
print(game_plan[8:])
for letter in game_plan[8:]:
    if letter == game_plan[8:][-1]:
        print(letter)
    else:
        print(letter, end=" ")
# print()
# names = ["Ryan", "Winter", "Victor", "Da'Von"]
# print()
# for name in names:
#     print(name)

# Concatenation and string formatting 
quarterback = "Tom"
receiver = "Jerry"
play = " runs really fast to catch the ball from "

# new variable        concatenation - combining strings together 
complete_play = receiver + play + quarterback 
print(complete_play)

# concatenating from a list
# basically what "".join(list) does
python_fact = ["Python", "is","great", "for", "string", "manipulation"]
python_sentence = ""
for word in python_fact:
    python_sentence += word + " "
print(python_sentence.strip())

# doing the same thing with join
sentence = " ".join(python_fact)
print(sentence)

# .lstrip() removes whitespace from the left side
# .rstrip() removes whitespace from the right side
# .strip() removes whitespace from both sides

name = " Lando"
print(name, "before strip")
name = name.lstrip() # remove whitespace from the left side
print(name, "after strip")

occupation = "Bounty Hunter                                    "
print(occupation, "before strip")
occupation = occupation.rstrip()
print(occupation, "after strip")

space_ship = "                 x-wing                   "
print(space_ship, "before strip")
space_ship = space_ship.strip()
print(space_ship, "after strip")

# formatting strings 
# .format()
celebration = "{} scores a touchdown and does the {} dance"
# filling in the details of the format
touchdown_celebration = celebration.format("Victor", "worm")
print(touchdown_celebration)

celebration = "{} scores a touchdown and does the {} dance"
# filling in the details of the format

# player = input("Who is scoring the touchdown? ")
# dance = input("What dance are they doing? ")
# touchdown_celebration = celebration.format(player, dance)
print(touchdown_celebration)

import random
names = ["Spencer", "Winter", "Victor", "Da'Von", "Karen", "Chris", "Brad", "Kayla", "Farzin", "Charlet", "Pheona", "Kris", "Taylor", "Caleb"]
print(random.choice(names))
# touchdown_celebration = f"{player} scores a touchdown and does the {dance} dance"
print(touchdown_celebration)

# .upper() capitalize all characters in a string
# .lower() decapitalize all characters in a string

chant = "We want a pitcher not a belly itcher!"
print(chant.upper())
yell = chant.upper()
print(yell)
# .title() capitalize the first letter of each word
print(chant.title())
# .capitalize()
print(chant.capitalize()) # only the first letter of the string

# .lower() make everything in a string lowercase
greeting = "HELLO THERE"
quiet_greeting = greeting.lower()
print(quiet_greeting)

# response = input("Say 'quit' to quit: ").lower().strip()
# if response == 'quit':
#     print("thanks for shopping")
# else:
#     print("please enter a valid response")

# .replace()

battle_plan = "Attack from the left flank"
print(battle_plan)

# changing the battle plan
new_battle_plan = battle_plan.replace("left", "right")

print(new_battle_plan)

sentence = "I ordered pizza last night."

my_list = sentence.split(" ")
print(my_list)

new_sentence = sentence.replace(".", "")
print(new_sentence)

for word in my_list:
    print(word)
    word = word.replace(".", "")
    print(word)

print(my_list)

word_list = ["hello.", 'goodbye.', "hello.", "hello."]

hello = 0
for word in word_list:
    if word.replace(".", "") == "hello":
        hello += 1
print(hello)


# "".join(ourlist)
sentence_list = ["The", "other", "day", "I", "saw", "a", "coyote"]
sentence = " ".join(sentence_list)
print(sentence)

# .split("whatever we're splitting")
my_string = "There is a hawk that hangs out by my house we named him Carl"
my_list = my_string.split()
print(my_list)

# .find()
droids = "These are not the droids you're looking for"
found_droids = droids.find("droids")
print(found_droids)

# .count() counts the number of occurrences of a character or string in a string
name_sentence = "Everyone in our class has names. Names like Ryan and Victor and Andy and Chris"
print(name_sentence.count("a"))

# isalpha()
name = "Ryan"
print(name.isalpha()) #True becuase all characters are letters
droid = "R2D2"
excited_person = "Lando!"
print(excited_person.isalpha())
print(droid.isalpha()) # False because there are numbers or digits

# isdigit()
my_number = "901"
print(my_number.isdigit())
my_false_number = "1OO1"
print(my_false_number.isdigit())
my_false_number2 = "1001!"
print(my_false_number2.isdigit())

# isspace
spaces = "         "
print(spaces.isspace())
spaces2 = "            :)                 "
print(spaces2.isalpha())


# number = input("Please enter a number")

# if number.isdigit():   
#     number = int(number)
#     print(number + 10)
# else:
#     print("please enter a valid whole number")



# my_string = "testdfdsfsdfsdfsdfs"
# print(my_string.index())

python_reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                     "I had a bad experience with this product. It didn't meet my expectations.", 
                     "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."
                ]

upper_case_reviews = []
review_words = ["good", "excellent", "bad", "poor"]
for sentence in python_reviews:
    for word in review_words:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    upper_case_reviews.append(sentence)
    print(sentence)

print(upper_case_reviews)


python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]
reviews = " ".join(python_reviews)
print(reviews)

for word in keywords:
    reviews = reviews.replace(word, word.upper())
    reviews = reviews.replace(word.title(), word.upper())
print(reviews)


