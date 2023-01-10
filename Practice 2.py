## Functions Can Return Something
def add(a, b):
print(f"ADDING {a} + {b}")
return a + b

def subtract(a, b):
print(f"SUBTRACTING {a} - {b}")
return a - b

ef multiply(a, b):
print(f"MULTIPLYING {a} * {b}")
return a * b

def divide(a, b):
print(f"DIVIDING {a} / {b}")
return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
CTIONS CAN RETURN SOMETHING 105

print("That becomes: ", what, "Can you do it by hand?")




## Strings, Bytes, and Character Encodings
import sys
script, input_encoding, error = sys.argv
RINGS, BYTES, AND CHARACTER ENCODINGS 111


def main(language_file, encoding, errors):
line = language_file.readline()

if line:
rint_line(line, encoding, errors)
return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
next_lang = line.strip()
raw_bytes = next_lang.encode(encoding, errors=errors)
cooked_string = raw_bytes.decode(encoding, errors=errors)

print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)



##What If
people = 20
cats = 30
dogs = 15


if people < cats:
print("Too many cats! The world is doomed!")

if people > cats:
print("Not many cats! The world is saved!")

if people < dogs:
print("The world is drooled on!")

if people > dogs:
print("The world is dry!")


dogs += 5

if people >= dogs:
print("People are greater than or equal to dogs.")

if people <= dogs:
print("People are less than or equal to dogs.")


if people == dogs:
print("People are dogs.")



## Else and If
people = 30
cars = 40
trucks = 15


if cars > people:
print("We should take the cars.")
SE AND IF 139
elif cars < people:
rint("We should not take the cars.")
else:
print("We can't decide.")

if trucks > cars:
print("That's too many trucks.")
elif trucks < cars:
print("Maybe we could take the trucks.")
else:
print("We still can't decide.")

if people > trucks:
print("Alright, let's just take the trucks.")
else:
print("Fine, let's stay home then.")


## Making Decisions
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
print("There's a giant bear here eating a cheese cake.")
print("What do you do?")
print("1. Take the cake.")
print("2. Scream at the bear.")

bear = input("> ")

if bear == "1":
print("The bear eats your face off. Good job!")
elif bear == "2":
print("The bear eats your legs off. Good job!")
else:
print(f"Well, doing {bear} is probably better.")
print("Bear runs away.")

elif door == "2":
print("You stare into the endless abyss at Cthulhu's retina.")
print("1. Blueberries.")
print("2. Yellow jacket clothespins.")
print("3. Understanding revolvers yelling melodies.")

insanity = input("> ")
ING DECISIONS 143

if insanity == "1" or insanity == "2":
print("Your body survives powered by a mind of jello.")
print("Good job!")
else:
print("The insanity rots your eyes into a pool of muck.")
print("Good job!")

else:
print("You stumble around and fall on a knife and die. Good job!")


## Branches and Functions
from sys import exit

def gold_room():
print("This room is full of gold. How much do you take?")

choice = input("> ")
if "0" in choice or "1" in choice:
how_much = int(choice)
else:
dead("Man, learn to type a number.")

if how_much < 50:
print("Nice, you're not greedy, you win!")
exit(0)
else:
dead("You greedy bastard!")


def bear_room():
print("There is a bear here.")
print("The bear has a bunch of honey.")
print("The fat bear is in front of another door.")
print("How are you going to move the bear?")
bear_moved = False

while True:
choice = input("> ")

if choice == "take honey":
dead("The bear looks at you then slaps your face off.")
elif choice == "taunt bear" and not bear_moved:
print("The bear has moved from the door.")
print("You can go through it now.")
bear_moved = True
elif choice == "taunt bear" and bear_moved:
NCHES AND FUNCTIONS 157
dead("The bear gets pissed off and chews your leg off.")
elif choice == "open door" and bear_moved:
gold_room()
else:
print("I got no idea what that means.")


def cthulhu_room():
print("Here you see the great evil Cthulhu.")
print("He, it, whatever stares at you and you go insane.")
print("Do you flee for your life or eat your head?")

choice = input("> ")

if "flee" in choice:
start()
elif "head" in choice:
dead("Well that was tasty!")
else:
cthulhu_room()


def dead(why):
print(why, "Good job!")
exit(0)

def start():
print("You are in a dark room.")
print("There is a door to your right and left.")
print("Which one do you take?")

choice = input("> ")

if choice == "left":
bear_room()
elif choice == "right":
cthulhu_room()
else:
dead("You stumble around the room until you starve.")


start()




