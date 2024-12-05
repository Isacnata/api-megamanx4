from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',  # Substitua com o nome de usuário correto
    'password': '',  # Substitua com a senha correta
    'database': 'isac'  # Substitua com o nome do seu banco de dados
}

# Função para conectar ao banco de dados
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Rota para criar um novo chefe
@app.route('/chefes', methods=['POST'])
def create_chefe():
    nome = request.json.get('nome')
    historia = request.json.get('historia')
    area = request.json.get('area')
    arma_ter_fraqueza = request.json.get('arma_ter_fraqueza')
    img_path = request.json.get('img_path')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO chefes_megaman_x4 (nome, historia, area, arma/tecnica, fraqueza, img_path)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (nome, historia, area, arma/tecnica, fraqueza, img_path))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Chefe criado com sucesso!'}), 201

# Rota para listar todos os chefes
@app.route('/chefes', methods=['GET'])
def get_all_chefes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM chefes_megaman_x4')
    chefes = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(chefes)

# Rota para obter um chefe específico por id
@app.route('/chefes/<int:id>', methods=['GET'])
def get_chefe(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM chefes_megaman_x4 WHERE id = %s', (id,))
    chefe = cursor.fetchone()

    cursor.close()
    conn.close()

    if chefe:
        return jsonify(chefe)
    else:
        return jsonify({'message': 'Chefe não encontrado'}), 404

# Rota para atualizar os dados de um chefe
@app.route('/chefes/<int:id>', methods=['PUT'])
def update_chefe(id):
    nome = request.json.get('nome')
    historia = request.json.get('historia')
    area = request.json.get('area')
    arma_ter_fraqueza = request.json.get('arma_ter_fraqueza')
    img_path = request.json.get('img_path')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE chefes_megaman_x4
        SET nome = %s, historia = %s, area = %s, arma_ter_fraqueza = %s, img_path = %s
        WHERE id = %s
    ''', (nome, historia, area, arma_ter_fraqueza, img_path, id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Chefe atualizado com sucesso!'})

# Rota para excluir um chefe
@app.route('/chefes/<int:id>', methods=['DELETE'])
def delete_chefe(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM chefes_megaman_x4 WHERE id = %s', (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'Chefe excluído com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
