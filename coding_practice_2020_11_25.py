Coding Bat:
1. non_start

def non_start(a: str, b: str) -> str:
  length1 = len(a)
  length2 = len(b)
  return (a[1:length1] + b[1:length2])


result = non_start('Hello', 'There')
print(result)

2. extra_end

def extra_end(string: str) -> str:
    length = len(string)
    return (string[3:length] + string[3:length] + string[3:length])


result = extra_end('Hello')
print(result)

3. left_2

def left_2(string: str) -> str:
  length1 = len(string)
  return (string[2:length1] + string[0:2])


result = left_2('Java')
print(result)

4. right_2

def right_2(string: str) -> str:
  length1 = len(string)
  return (string[-2:length1] + string[0:length1 - 2])


result = right_2('Hi')
print(result)

5. the_end

def the_end(string: str, front: bool) -> str:
  if front == True:
    return (string[0])
  else:
    return (string[-1])


result = the_end('Hello', True)
print(result)

6. without_end_2

def without_end_2(string: str) -> str:
    length = len(string) - 1
    return (string[1:length])


result = without_end_2('Hello')
print(result)

7. middle_two

def middle_two(string: str) -> str:
  length1 = ((len(string)) // 2) - 1
  length2 = ((len(string)) // 2) + 1
  return (string[length1:length2])

result = middle_two('string')
print(result)

8. combo_string

def combo_string(a: str, b: str) -> str:
  lengthA = len(a)
  lengthB = len(b)
  if lengthA > lengthB:
    return b + a + b
  else:
    return a + b + a

result = combo_string('hi', 'Hello')
print(result)

9. ends.ly

def ends_ly(string: str) -> bool:
    length = len(string)
    end = (string[-2:length])
    if end == "ly":
      return True
    else:
      return False

result = ends_ly('oddly')
print(result)

10. n_twice

def n_twice(string: str, n: int) -> str:
    length = len(string)
    first = (string[0:n])
    last = (string[-n:length])
    return first + last
    
result = n_twice('Chocolate', 3)
print(result)

Python Workbook:
1. 34
number = int(input("Enter a number:"))
if number % 2 == 0:
  print("This number is even")
else:
  print("This number is odd")

2. 35
humanYears = float(input("How many human years?"))
if humanYears <= 2:
  dogYears = humanYears * 10.5
else:
  dogYears = (2 * 10.5) + ((humanYears - 2) * 4)
print(humanYears, "human years is equal to", dogYears, "dog years")

3. 36
letter = input("Enter a letter").lower()
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
  print("This is a vowel")
elif letter == "y":
  print("Y is sometimes a vowel and sometimes a consonant")
else: 
  print("That is a consonant")
  
4. 37
sides = int(input("Enter the number of sides"))
if sides == 3:
  print("This is a triangle")
elif sides == 4:
  print("This is a quadrilateral")
elif sides == 5:
  print("This is a pentagon")
elif sides == 6:
  print("This is a hexagon")
elif sides == 7:
  print("This is a heptagon")
elif sides == 8:
  print("This is a octagon")
elif sides == 9: 
  print("This is a nonagon")
elif sides == 10:
  print("This is a decagon")
else: 
  print("This is not supported")
 
5. 40
sideA = input("Enter a side length")
sideB = input("Enter a side length")
sideC = input("Enter a side length")
if sideA == sideB == sideC:
  print("This is an equilateral triangle")
elif sideA == sideB or sideA == sideC or sideB == sideC:
  print("This is a isosceles")
else: 
  print("This is a scalene triangle")
  
6. 43
note = int(input("Enter banknote"))
if note == 1:
  print("George Washington")
elif note == 2:
  print("Thomas Jefferson")
elif note == 5:
  print("Abraham Lincoln")
elif note == 10:
  print("Alexander Hamilton")
elif note == 20:
  print("Andrew Jackson")
elif note == 50:
  print("Benjamin Franklin")
else: 
  print("Invalid Note")
  
7. 44
month = input("Enter a month").lower()
days = input("Enter a day")
if month == "january" and days == 1:
  print('This is New Years Day')
elif month == "july" and days == 1:
  print("This is Canada Day")
elif month == "december" and days == 25:
  print("This is Christmas Day")
else: 
  print("There is no holiday")
  
8. 48
year = int(input("Enter a year"))
if year % 12 == 8:
  print("Dragon")
elif year % 12 == 9:
  print("Snake")
elif year % 12 == 10:
  print("Horse")
elif year % 12 == 11:
  print("Sheep")
elif year % 12 == 0:
  print("Monkey")
elif year % 12 == 1:
  print("Rooster")
elif year % 12 == 2:
  print("Dog")
elif year % 12 == 3:
  print("Pig")
elif year % 12 == 4:
  print("Rat")
elif year % 12 == 5:
  print("Ox")
elif year % 12 == 6:
  print("Tiger")
elif year % 12 == 7:
  print("Hare")
 
9. 51
letter = input("Enter a letter grade:").upper()
if letter == "A+" or letter == "A":
  print("4.0")
elif letter == "A-":
  print("3.7")
elif letter == "B+":
  print("3.3")
elif letter == "B":
  print("3.0")
elif letter == "B-":
  print("2.7")
elif letter == "C+":
  print("2.3")
elif letter == "C":
  print("2.0")
elif letter == "C-":
  print("1.7")
elif letter == "D+":
  print("1.3")
elif letter == "D":
  print("1.0")
elif letter == "F":
  print("0")
else: 
  print("INVALID")
 
10. 53
year = int(input("Enter a number of years"))
if year % 400 == 0:
  print("Leap Year")
elif year % 100 == 0:
  print("Not a leap year")
elif year % 4 == 0:
  print("Leap Year")
else: 
  print("Not a leap year")







