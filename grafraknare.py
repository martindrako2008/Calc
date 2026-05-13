import sys
import matplotlib.pylab as plt
import numpy as np

calc = True

while calc == True:
 choice = int(input("Vill du använda grafräknaren eller miniräknaren?\n1. Grafräknare\n2. Miniräknare\n3. Avsluta\n"))
 if choice == 1:
  x = np.linspace(-1, 5, 500)
  expr = input("Skriv in en funktion t.ex ( 3*x**2 + 3*x - 10): --->  ")

  allowed_names = {
    "x" : x,
    "np" : np
 }

  y = eval(expr,{"__builtins__": {}}, allowed_names)
  loop = True
  while loop == True:
   q = int(input("Vill du veta värdet på en specifik punkt eller se grafen?\n1. Veta Värde\n2. Se Graf\n3. Avsluta\n"))
   if q == 1:
    point = float(input("Skriv in x värdet\n ----> "))

    allowed_names_point = {
    "x" : point,
    "np" : np
    }
    y_value = eval(expr,{"__builtins__": {}}, allowed_names_point)
    print(f"f({point}) = {y_value}")
   elif q == 2:
    plt.plot(x, y)
    plt.title(f"Grafen av f(x) = {expr}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()
   elif q == 3:
     loop = False
 elif choice == 2:
   uttryck = input("Skriv in ett matematiskt uttryck (t.ex. 3*5 + 2): ")
   allowed_names_calc = {
        "np": np,
        "x": str
   }
   val = eval(uttryck, {"__builtins__": {}}, allowed_names_calc)
   print(f"Resultatet av {uttryck} är: {val}")
 elif choice == 3:
   print("Avslutar programmet.")
   calc = False