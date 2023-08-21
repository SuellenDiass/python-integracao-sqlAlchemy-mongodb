#  Implementando um Banco de Dados mongoDB com Pymongo

from pymongo import MongoClient

# Conectar ao MongoDB (substitua <ATLAS_URI> com sua URI de conexão)
client = MongoClient("ATLAS_URI>") # inserir aqui a uri crianda na sua conta MongoDB para vc se conectar ao BD
db = client["mydatabase"]

# Criar coleção "bank" para documentos de clientes
bank_collection = db["bank"]

# Inserção de documentos
document1 = {
    "nome": "Alice",
    "cpf": "123456789",
    "endereco": "Rua A",
    "contas": [
        {"tipo": "Corrente", "agencia": "001", "numero": 1001, "saldo": 1000},
    ]
}

document2 = {
    "nome": "Bob",
    "cpf": "987654321",
    "endereco": "Rua B",
    "contas": [
        {"tipo": "Poupança", "agencia": "001", "numero": 2001, "saldo": 500},
    ]
}

bank_collection.insert_many([document1, document2])

# Recuperação de informações
print("\nRecuperando informações de clientes e suas contas (MongoDB):")
for cliente in bank_collection.find():
    print(cliente["nome"])
    for conta in cliente["contas"]:
        print(f"Conta: {conta['tipo']} - Saldo: {conta['saldo']}")

# ... (outros métodos de recuperação e manipulação)
