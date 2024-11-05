import requests
import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
meucursor=banco.cursor()

cep = input("Qual o CEP? ")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cep = dic_requisicao['cep']
    logradouro = dic_requisicao['logradouro']
    complemento = dic_requisicao['complemento']

    sql = "insert into enderecos (cep,logradouro,complemento) values (%s,%s,%s)"
    data = (cep, logradouro, complemento)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()
    banco.close()

else:
    print("CEP inválido.")
