from flask import Flask, jsonify, request
from bd import connect

# Inicia aplicação Flask

app = Flask(__name__)

# Passa função de conexão para variável para acessar criar o cursor do banco
conexao_com_banco_de_dados = connect()
cursor = conexao_com_banco_de_dados.cursor()


# Cria endpoint(city) para API 

@app.route('/city', methods=['GET'])
def obter_cidade():
    dados_formatados_em_json = list()

    cursor.execute('SELECT * FROM world.city')
    dados_retornados_na_consulta = cursor.fetchall()
    
    # Cria um loop para iterar sobre os dados que o banco retorna e formatar em um array de json

    for linha in dados_retornados_na_consulta:
        json = {
        'id': linha[0],
        'name': linha[1],
        'country_code': linha[2],
        'district': linha[3],
        'population': linha[4]
        }
    
        dados_formatados_em_json.append(json)

    # Retorna os dados formatados

    return jsonify(dados_formatados_em_json)


# Inserir novas cidades
@app.route('/city', methods=['POST'])
def inserir_cidades():
    
    novo_dado = request.get_json()
    cursor.execute(f"INSERT INTO world.city(name, country_code, district, population) VALUES ('{novo_dado['name']}', '{novo_dado['country_code']}', '{novo_dado['district']}', {novo_dado['population']})")
    cursor.fetchall()

    return novo_dado

# Excluir cidades
# Atualizar cidades






# Roda aplicação
app.run()