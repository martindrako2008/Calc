





a = False
while a == True:
 siffror = input("Skriv in två siffror, separerade med ett mellanslag: ---->  ")
 a, b = map(float, siffror.split())


def addition(a,b):
    ans = a + b
    return int(ans)

def subtraction(a,b):
    ans = a - b
    return int(ans)

def multiplication(a,b):
    ans = a * b
    return int(ans)

def division(a,b): 
    if b == 0:
        return "Error: Division by zero is not allowed."
    ans = a / b
    return ans

r = True

while r == True:
 val = input("Skriv in en siffra för vad du vill göra med talen\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divition\n----> ")

 if val == "1":
  print()
  print(addition(a,b))
  print()
  r == False
 elif val == "2":
  print()
  print(subtraction(a,b))
  print()
  r == False
 elif val == "3":
  print()
  print(multiplication(a,b))
  print()
  r == False
 elif val == "4":
  print()
  print(division(a,b))
  print()
  r == False
    
 else:
    print()
    print("Du måste välja en av alternativen\n")
  



