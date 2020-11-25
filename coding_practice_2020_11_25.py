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





