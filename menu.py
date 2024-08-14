menu = 0
while menu != 6:
    print("***Menu principal***")
    print("Escolha uma das opções abaixo:")
    print("[1] - CADASTRAR USUARIOS")
    print("[2] - CADASTRAR FUNCIONÁRIOS")
    print("[3] - CADASTRAR PRODUTOS")
    print("[4] - CADASTRAR ESTOQUE")
    print("[5] - CADASTRAR VENDAS")
    print("[6] - SAIR DO PROGRAMA")
    print()
    menu = int(input("Escolha uma das opções: "))
    print()
    
    if menu == 1:
        print("Cadastrar dados de Usuarios\n")
    elif menu == 2:
        print("Cadastrar dados de Funcionários\n")
    elif menu == 3:
        print("Cadastrar dados de produtos\n")
    elif menu == 4:
        print("Cadastrar dados de Estoque\n")
    elif menu == 5:
        print("Cadastrar dados de Venda\n")


print()
print("Programa encerrado!!!")        