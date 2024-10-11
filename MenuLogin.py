usuarios_cadastrados=["Alex","Bruno","Caio","Daniel","Evandro"]
senhas_cadastradas=["11","12","13","14","15"]
menu=0

def exibir_menu():
   while True:
     try:
       menu=int(input("Digite 1 para realizar login \nDigite 2 para cadastrar\nDigite 3 para sair\n"))
       if menu==1:
          usuario=input("Digite o nome do usuario:\n")
          senha=input("Digite a senha:\n")
          for contagem, cadastro in enumerate(usuarios_cadastrados):
            if usuario==cadastro and senha==senhas_cadastradas[contagem]:
               print(f"Bem-vindo {usuario}")
               return False
            elif contagem==len(usuarios_cadastrados)-1:
               print("Usuario ou senha incorretos")
               return False
      
       elif menu==2: 
          nome=input("Crie o nome do usuario: ")
          for cadastro in usuarios_cadastrados:
            while cadastro==nome:
              nome=input("Usuario já existe, tente outro nome.\n")
          usuarios_cadastrados.append(nome)
          senha=input("Crie uma senha: ")
          senhas_cadastradas.append(senha)
          print("\nUsuario cadastrado com sucesso!\nVoltando ao menu...\n")
          
          
       elif menu==3:
          print("Saindo...")
          return False
     except ValueError as e:
          print("\nValor inválido, digite novamente.\n")
        
exibir_menu()
