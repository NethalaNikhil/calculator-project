#calcultor
from replit import clear
import art
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
operations = {"+":add,
              "-":sub,
              "*":mul,
              "/":div,}
def calculator ():
  clear()
  print(art.logo)
  
  num1 = float(input("What 's the first number?: "))
  for operator in operations:
    print(operator)
  which_op = input("which operation u want to perform for above?: ")
  num2 = float(input("What 's the second number?: "))
  answer = operations[which_op](num1,num2)
  next_answer =int(answer)
  print(f"{num1} {which_op} {num2} = {answer}")
  
  it_is = True
  while it_is:
    continue_cal = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to  restart exit.: ").lower()
    if continue_cal == 'y':
      new_operator= input("pick an operator: ")
      next_input = float(input("what 's the next number?: "))
      new_answer = operations[new_operator](next_answer,next_input)
      print(f"{answer} {new_operator} {next_input} = {new_answer}")
      answer = new_answer
    elif(continue_cal == 'r'):
      calculator()
    else:
      it_is = False
calculator()
#bug if we enter 3 values last operator with / gives wrong answers
    

    
  
  
