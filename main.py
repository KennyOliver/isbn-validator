print("ISBN-10 Validator")
print("Enter an ISBN code with a single '-' between the numbers")
isbn = input("--> ")

code_digits = []
valid_digits = [0,1,2,3,4,5,6,7,8,9,'X']

count = 0
digits  = isbn.split('-')
for digit in digits:
  code_digits.append(digit)
    count += 1
print(code_digits)
print("Test")
print(count)