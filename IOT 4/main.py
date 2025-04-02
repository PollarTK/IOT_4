from empresa import Funcionario

def main():
    funcionario = Funcionario()
    funcionario.criar_tabela()
    
    while True:
        print("\n")
        print("[1] Adicional Funcionario")
        print("[2] Listar Funcionarios")
        print("[3] Atualizar salario")
        print("[4] Excluir Funcionario")
        print("[5] Alterar Cargo")
        print("[6]Alterar Departamento")
        print("[7]Alterar Nome")
        print("[8] Sair do programa")
        opcao = int(input("Escolha uma opcao: "))
        
        match opcao:
            case 1:
                funcionario.adcionar_funcionario()
            case 2:
                funcionario.listar_funcionarios()
            case 3:
                funcionario.atualizar_salario()
            case 4:
                funcionario.deletar()
            case 5:
                funcionario.alterar_cargo()
            case 6:
                funcionario.alterar_departamento()
            case 7:
                funcionario.alterar_nome()
            case 8:
                print("Programa encerrado.")
                break
            case _:
                print("Opcao Invalida!")

if __name__ == '__main__':
    main()