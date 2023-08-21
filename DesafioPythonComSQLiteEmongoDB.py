#  Integrando com SQLite usando SQLAlchemy
# Respeitando a estruturação do código de acordo com a pepi
# Documentação para explorar: https://docs.sqlalchemy.org/en/20/orm/query.html

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import func  # Importando o módulo func para usar funções SQL

Base = declarative_base()

# Criando tabelas com base no esquema relacional
class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(Integer)
    cliente = relationship("Cliente", back_populates="contas")

# Conexão com o banco de dados
engine = create_engine("sqlite:///banco.db")  # Especifique o nome do banco de dados
Base.metadata.create_all(engine)

# Criando a instância da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados
cliente1 = Cliente(nome='Alice', cpf='123456789', endereco='Rua A')
cliente2 = Cliente(nome='Bob', cpf='987654321', endereco='Rua B')

conta1 = Conta(tipo='Corrente', agencia='001', numero=1001, saldo=1000, cliente=cliente1)
conta2 = Conta(tipo='Poupança', agencia='001', numero=2001, saldo=500, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2])
session.commit()

# Restante do código...


# Recuperação de dados
print("\nRecuperando informações de clientes e suas contas:")
for cliente in session.query(Cliente):
    print(cliente.nome)
    for conta in cliente.contas:
        print(f"Conta: {conta.tipo} - Saldo: {conta.saldo}")


# Recuperação de dados com filtros:
# Recuperar contas de um cliente específico pelo nome

cliente_nome = "Alice"
cliente = session.query(Cliente).filter_by(nome=cliente_nome).first()
if cliente:
    print(f"Contas de {cliente.nome}:")
    for conta in cliente.contas:
        print(f"Tipo: {conta.tipo} - Saldo: {conta.saldo}")
else:
    print(f"Cliente {cliente_nome} não encontrado.")

# Atualizar saldo de uma conta específica
conta_id = 1
novo_saldo = 1500
# conta = session.query(Conta).get(conta_id) depreciado
conta = session.query(Conta).filter_by(id=conta_id).first()
if conta:
    conta.saldo = novo_saldo
    session.commit()
    print(f"Saldo da conta {conta_id} atualizado para {novo_saldo}.")
else:
    print(f"Conta {conta_id} não encontrada.")

# Excluir um cliente e suas contas associadas
cliente_id = 1
#cliente = session.query(Cliente).get(cliente_id) depreciado
cliente = session.query(Cliente).filter_by(id=cliente_id).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} e suas contas associadas excluídos.")
else:
    print(f"Cliente {cliente_id} não encontrado.")

# Recuperar o total de saldo em todas as contas de um cliente
cliente_id = 1
soma_saldo = session.query(func.sum(Conta.saldo)).filter_by(id_cliente=cliente_id).scalar()
if soma_saldo:
    print(f"Total de saldo das contas do cliente {cliente_id}: {soma_saldo}")
else:
    print(f"Cliente {cliente_id} não encontrado ou sem contas.")



