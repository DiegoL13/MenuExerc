usuarios=["Alex","Bruno","Caio","Daniel","Evandro"]
senhas=["11","12","13","14","15"]
menu=0

def exibir_menu():
   while True:
     try:
       menu=int(input("Digite 1 para realizar login \nDigite 2 para cadastrar\nDigite 3 para sair\n"))
       if menu==1:
          usuario=input("Digite o nome do usuario:\n")
          senha=input("Digite a senha:\n")
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
            while x==nome:
              nome=input("Usuario já existe, tente outro nome.\n")
            
          usuarios.append(nome)
          senha=input("Crie uma senha: ")
          senhas.append(senha)
          print("\nUsuario cadastrado com sucesso!\n")
          menu=int(input("Digite 1 para voltar ao menu\nDigite 2 para sair\n"))
          if menu==2:
             print("\nSaindo...")
             return False
          else:
             print("\nVoltando ao menu.\n")

       elif menu==3:
          print("Saindo...")
          return False
     except ValueError as e:
          print("\nValor inválido, digite novamente.\n")
        
exibir_menu()
