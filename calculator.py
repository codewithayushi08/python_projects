
def calculate(num1,num2,operation):
    if operation == "+" :
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation =="**":
       return num1**num2
    elif operation == "/" or operation== "%":
      if num2 ==0:
        return "Error:Div by 0"
      if operation =="/":
        return num1/num2
      else:
        return num1%num2
    else:
        return "Invalid operation"

        
while True:
    print("\n--New calculation---")
    try:
      num1=int(input("Enter num1="))
      num2=int(input("Enter num2="))
    except ValueError:
      print("Invalidinput!.Please enter numbers only.")
      continue

      op=input("Enter operation(+,-,*,**,/,%):")
      if op not in ["+","-","*","**","/","%"]:
         print("Error:Invalid operation symbol!")
         continue

    
      result=calculate(num1,num2,op)
      print("Result is:",result)
    
    again=input("Do another? (y/n):"). lower()
    if again !="y":
        print("Goodbye!")
    break
