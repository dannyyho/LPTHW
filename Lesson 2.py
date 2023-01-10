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



