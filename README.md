<p> <h1 align="center">Python integração com sqlAchemy e com MongoDB utilizando Pymongo</h1></p>

<p align="center">
    <img width="700" src="https://github.com/SuellenDiass/SuellenDiass/assets/102911341/362af47a-bdaa-427a-9a42-5c2090b7d47b">
</p>
<p> <h4 align="center">Esquema relacional na tabela cliente e na tabela conta</h4></p>



<p align="center">
    <img width="700" src="https://github.com/SuellenDiass/SuellenDiass/assets/102911341/bae254b8-77a9-402a-881b-94a02fc5d2b0" alt="Imagem">
</p>
<p> <h4 align="center">Conectando ao Banco de dados MongoDB</h4></p>



<p align="center">
    <img width="700" src="https://github.com/SuellenDiass/SuellenDiass/assets/102911341/6369c6a6-0201-496c-a953-ae42c6ec113e">
</p>
<p> <h4 align="center">Conectando ao Banco de dados MongoDB</h4></p>


<p align="center">
    <img width="700" src="https://github.com/SuellenDiass/SuellenDiass/assets/102911341/6b177ea2-df35-4fd5-b7d7-c8104eb679b2">
</p>
<p> <h4 align="center">Conectando ao Banco de dados MongoDB</h4></p>



<p> <h2 align="center">Implementando um Banco de Dados Relacional com SQLAlchemy</h2></p>


**Estruturação de Tabelas Cliente e Conta com SQLAlchemy:**

Nesta parte do estudo, aprendemos como criar e interagir com bancos de dados relacionais usando o SQLAlchemy, uma biblioteca em Python. Criamos uma estrutura de dados para armazenar informações de clientes e suas contas. Para fazer isso, seguimos os passos:

1. **Definição de Classes:** Criamos classes `Cliente` e `Conta` para representar tabelas do banco de dados. Usamos a classe `declarative_base` do SQLAlchemy para definir a base das classes.

2. **Mapeamento de Relacionamento:** Utilizamos o conceito de mapeamento de relação para conectar a tabela `Cliente` com a tabela `Conta`. Isso nos permitiu associar contas a clientes específicos.

3. **Conexão com Banco de Dados:** Criamos uma instância da classe `create_engine` para estabelecer a conexão com o banco de dados SQLite. Essa conexão nos permite salvar e recuperar dados.

4. **Sessões e Transações:** Usamos a classe `Session` para criar uma sessão, que é uma interface para interagir com o banco de dados. Realizamos operações como inserção, atualização e exclusão dentro de uma sessão. As transações garantem a consistência dos dados.

5. **Inserção e Recuperação de Dados:** Demonstramos como inserir informações de clientes e contas no banco de dados usando a função `add_all` e como recuperar esses dados usando consultas, como `query`.

**Integração Python com SQLite:**

Nesta parte, exploramos como integrar Python com um banco de dados SQLite, um sistema de gerenciamento de banco de dados relacional. Aprendemos a:

- **Criar Tabelas:** Utilizamos o SQLAlchemy para criar tabelas como classes Python, representando a estrutura do banco de dados.

- **Inserir Dados:** Usando sessões, inserimos dados nas tabelas. As transações garantem que os dados sejam inseridos corretamente.

- **Recuperar Dados:** Utilizamos consultas para recuperar informações específicas, como detalhes de clientes e suas contas.

**Integração Python com MongoDB:**

Na segunda parte do estudo, exploramos a integração do Python com o MongoDB, um banco de dados NoSQL. Aprendemos a:

- **Conectar ao MongoDB:** Usando o módulo `pymongo`, estabelecemos uma conexão com o banco de dados MongoDB.

- **Criar Documentos:** Armazenamos informações como documentos, em vez de tabelas. Cada documento pode conter várias informações estruturadas.

- **Inserir Documentos:** Utilizando a função `insert_many`, inserimos vários documentos em uma coleção.

- **Recuperar Documentos:** Utilizamos consultas para recuperar documentos específicos e suas informações associadas.

Em resumo, aprendi  a estruturar dados usando o SQLAlchemy e a integrar Python com bancos de dados relacionais (SQLite) e NoSQL (MongoDB). Esses conceitos formam a base para criar aplicativos que armazenam, recuperam e manipulam dados de maneira eficaz.

#### Documentação para explorar: https://docs.sqlalchemy.org/en/20/orm/query.html
#### Documentação para explorar: https://docs.sqlalchemy.org/en/14/core/reflection.html#fine-grained-reflection-with-inspector
#### Documentação para explorar: https://pymongo.readthedocs.io/en/stable/atlas.html


#### Curso Formação Python Developer da Dio.me administrado pelo mentora Juliana Mascarenhas/ Data Scientist, DIO

[DIO](https://www.dio.me/).


