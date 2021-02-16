print("ISBN-10 Validator")
print("Enter an ISBN code with a single '-' between the numbers")
isbn = input("--> ")
digits  = isbn.split('-')

code_digits = []
for digit in digits:
  code_digits.append(digit)
print(code_digits)