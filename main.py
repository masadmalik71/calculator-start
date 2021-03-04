from art import logo
from replit import clear

print(logo)

def add(f_num, s_num):
  return f_num + s_num
def sub(f_num, s_num):
  return f_num - s_num
def mul(f_num, s_num):
  return f_num * s_num
def div(f_num, s_num):
  return f_num / s_num


def math_operation(f_num, operator , s_num):
  if operator == "+":
    result = add(f_num, s_num)
    return result
  if operator == "-":
    result = sub(f_num, s_num)
    return result
  if operator == "*":
    result = mul(f_num, s_num)
    return result
  if operator == "/":
    result = div(f_num, s_num)
    return result

operation = ["+", "-", "*", "/"]
is_start_new = False
is_cal_again = False

while not is_start_new:
  f_num = float(input("What's your first number: "))
  for operator in operation:
    print(operator)
  operator = input("Pick an operation: ")
  s_num = float(input("What's your next number: "))
  result = math_operation(f_num, operator, s_num)
  print(f"{f_num} {operator} {s_num} = {result}")
  while not is_cal_again:
    closed = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if closed == 'n':
      is_cal_again = True
      clear()
    else:
      clear()
      for operator in operation:
        print(operator)
      operator = input("Pick an operation: ")
      s_num = float(input("What's your next number: "))
      result1 = result
      result = math_operation(result, operator, s_num)
      print(f"{result1} {operator} {s_num} = {result}")