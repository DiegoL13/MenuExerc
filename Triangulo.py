n=int(input("Digite um número acima de 2 para formar os triângulos: "))
for x in range(1,n+1):
  for y in range(0,x):
    print(x , end=" ")
  print()
print()
for x in range(1,n+1):
  for y in range(1,x+1):
    print(y , end=" ")
  print()
