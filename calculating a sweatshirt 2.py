n = int(input("Veuillez saisir le rang: "))
while n < 2:
      n = int(input("Veuillez saisir le rang : "))
Upp = 0
Up = 1
print("Les termes de la suite de Fibonacci sont: ")
print(Upp ,end=" ")
print(Up, end=" ")
for i in range (n-1):
    U = Upp + Up
    print(U, end=" ")
    Upp = Up
    Up = U