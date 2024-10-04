usuarios=["Alex","Bruno","Caio","Daniel","Evandro"]
senhas=[11,12,13,14,15]
menu=0

def exibir_menu():
   while True:
       menu=int(input("Digite 1 para realizar login \nDigite 2 para cadastrar\nDigite 3 para sair\n"))
       if menu==1:
          usuario=input("Digite o nome do usuario:\n")
          senha=int(input("Digite a senha:\n"))
          for contagem, x in enumerate(usuarios):
            if x==usuario and senha==senhas[contagem]:
               print(f"Bem-vindo {x}")
               return False
            elif contagem==len(usuarios)-1:
               print("Usuario ou senha incorretos")
               return False
      
       elif menu==2: 
          nome=input("Crie o nome do usuario: ")
          for x in usuarios:
            if x==nome:
              print("Usuario já existe")
              return False
          usuarios.append(nome)
          senha=int(input("Crie uma senha:"))
          senhas.append(senha)
          print("Usuario cadastrado com sucesso!")
          print("="*30)
          menu=int(input("Digite 1 para voltar ao menu ou 2 para sair: "))
          if menu==2:
             print("Saindo...")
             return False
          else:
             print("\nVoltando ao menu\n")

       elif menu==3:
          print("Saindo...")
          return False
   
exibir_menu()
