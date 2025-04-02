import mysql.connector

class Funcionario():
    def conectar(self):
        return mysql.connector.connect(
            host = 'paparella.com.br', 
            user = 'paparell_aluno_6',
            password = '@Senai2025',
            database = 'paparell_python'
        )
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = ("""
                 create table if not exists funcionarios(
                     id int auto_increment primary key,
                     nome varchar(255) not null,
                     idade int not null,
                     cargo varchar(255) not null,
                     departamento varchar(255) not null,
                     salario decimal(10,2))
                 
                 """)
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()

    def adcionar_funcionario(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        nome = input("Digite o Nome do Funcionário: ")
        idade = int(input("Digite a Idade: "))
        cargo = input("Digite o Cargo: ")
        dep = input("Digite o Departamento: ")
        salario = float(input("Digite o Salário: "))
        cursor.execute("INSERT INTO funcionarios(nome, idade, cargo, departamento, salario) values(%s,%s,%s,%s,%s)", (nome, idade, cargo, dep, salario))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Funcionario Cadastrado Com Sucesso!")
        
    def listar_funcionarios(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * from funcionarios")
        funcionarios = cursor.fetchall()
        if not funcionarios:
            print("Funcionarios nao encontrados")
        else:
            for f in funcionarios:
                print(f"ID: {f[0]} | Nome: {f[1]} | Idade: {f[2]} | Cargo: {f[3]} | Departamento: {f[4]} | Salario: R${f[5]}")
        conexao.commit()
        cursor.close()
        conexao.close()
                
    def atualizar_salario(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do Funcionario para Atualizar o Salario: "))
        while True:
            novo_salario = float(input("Digite o Novo Salario; "))
            if novo_salario <= 0:
                print("O Salario Tem Que Ser Maior Que 0!")
            else:
                cursor.execute("UPDATE funcionarios SET salario=%s where id=%s", (novo_salario, funcionario_id))
                conexao.commit()
                cursor.close()
                conexao.close()
                print("Salario Atualizado com Sucesso!")
                break
        
    def alterar_cargo(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do Funcionario para Atualizar o Cargo: "))
        novo_cargo = input("Digite o Novo Cargo: ")
        cursor.execute("UPDATE funcionarios SET cargo=%s where id=%s", (novo_cargo, funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Cargo Atualizado com Sucesso!")
        
    def alterar_departamento(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do Funcionario para Atualizar o Departamento: "))
        novo_departamento = input("Digite o Novo Departamento: ")
        cursor.execute("UPDATE funcionarios SET departamento=%s where id=%s", (novo_departamento, funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Departamento Atualizado com Sucesso!")
        
    def alterar_nome(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do Funcionario para Atualizar o Nome: "))
        novo_nome = input("Digite o Novo Nome: ")
        cursor.execute("UPDATE funcionarios SET nome=%s where id=%s", (novo_nome, funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Departamento Atualizado com Sucesso!")
        
    def deletar(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        Funcionario_id = int(input("Digite o ID do Funcionario que Deseja Excluir: "))
        cursor.execute("DELETE FROM funcionarios WHERE id=%s",[Funcionario_id],)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Funcionario Excluido com sucesso!")