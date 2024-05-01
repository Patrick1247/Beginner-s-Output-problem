#Mad-libs
print("Create your Mad-Lib!")
food = input("Name a food: ")
place = input("Name a place: ")
time = input("Your Bedtime: ")
adjective = input("Name an adjective: ")
animal = input("Name an animal: ")
emotion = input("Name a feeling: ")
vehicle = input("Name a mode of transportation: ")
word = input("Name a random word: ")
print("Billy is eating " + food + "in the " + place + "at " + time + ". Suddenly, a " + adjective, animal, "attacked! Billy was " + emotion, "and ran away on a " + vehicle + ", but unfortunately, " + word + "!")

# Q1. Minutes to Seconds
minutes = input("Minutes: ")
print(minutes,"minutes =", int(minutes) * 60,"Seconds.")

# Q2. Birthday Cards
Cruella = input("Cruella's number of birthday cards: ")
print(f"When Cruella recives {Cruella} birthday cards. Jane will recieves at least {int(Cruella)*2}.")

# Age to Days
year = input("Enter your age in years: ")
days = int(year) * 365
print(f"You are {days} days old")
if int(36500-int(days)<0):
    print("Wow! You are more than 100 years old!")
elif int(36500-int(days)>0):
    print(f"You will turn 100 years old in {36500-int(days)} days!")
