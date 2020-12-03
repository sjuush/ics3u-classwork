1.
def add_three_numbers(number_1: float, number_2: float, number_3: float):
  return number_1 + number_2 + number_3

result = three_numbers(14, 15, 16)
print(result)

2. 
def name_age (name: str, age: int):
  return "Your name is {} and your age is {}".format(name, age)

result = name_age("James", 27)
print(result)

3. 
def average(number_1: float, number_2: float):
  return (number_1 + number_2)/2

result = average(15, 17)
print(result)

4. 
def largest_number(number_1: float, number_2: float, number_3: float):
  list = [number_1, number_2, number_3]
  list.sort()
  return list[-1]

result = largest_number(12, 18, 15)
print(result)

5. 
def first_two_char(string: str):
  return string[0:2]

result = first_two_char("Chocolate Sauce")
print(result)

