from dataclasses import dataclass

import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
meucursor=banco.cursor()
pesquisa='select * from alunos;'
meucursor.execute(pesquisa)
resultado=meucursor.fetchall()
# fetchall traz itens em forma de tupla
for x in resultado:
    print(x)

opcao = input("Deseja adicionar valores? 0 para sim, 1 para não: ")
if opcao == 1:
    meucursor.close()
    banco.close()
    print("Até mais!")
    exit()

nome1 = input("Digite o nome: ")
telefone1 = input("Digite o telefone: ")

sql = "insert into alunos (nome, telefone) values (%s, %s)"
data = (nome1, telefone1)
meucursor.execute(sql,data)
banco.commit()

meucursor.close()
banco.close()