nomes=["Alex","Bruno","Caio","Daniel","Evandro"]
senhas=[11,12,13,14,15]
menu=0

while menu<1 or menu>3:
   menu=int(input("Digite 1 para realizar login \nDigite 2 para cadastrar\nDigite 3 para sair\n"))
   
if menu==1:
   usuario=input("Digite o nome do usuario:\n")
   for índice, x in enumerate(nomes):
      if x==usuario:
         senha=int(input("Digite a senha:\n"))
         if senha==senhas[índice]:
            print(f"Bem-vindo {x}")
            break
         elif índice==len(nomes)-1:
            print("Senha incorreta")
      elif índice==len(nomes)-1:
         print(f"Usuario {usuario} não cadastrado")
   
elif menu==2:
   nome=input("Crie o nome do usuario:")
   nomes.append(nome)
   senha=int(input("Crie uma senha:"))
   senhas.append(senha)

else:
   print("Saindo...")
