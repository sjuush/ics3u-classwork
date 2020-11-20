x = input("What is your favourite colour?")
print("{} !, That's my favourite colour as well!".format(x))

x = int(input("How many cans come in a pack?"))
y = int(input("How many packs are there?"))
print("The amount of cans is:", x*y)

x = float(input("What is the length?"))
y = float(input("What is the width?"))
z = float(input("What is the height?"))
print("The volume of the rectangular prism is:", x * y * z)

x = input("Did you just enter a google meet and then mute the teacher?")
if x == "yes":
  print("You probably shouldn't do that")
if x == "no":
  print("Ok, Good")
else:
  print("Invalid response")
