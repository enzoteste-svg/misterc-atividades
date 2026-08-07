# database.py
# Cria o banco de dados SQLite do restaurante
# e coloca os dados iniciais (categorias e pratos)

import sqlite3

# nome do arquivo do banco
DB = "restaurante.db"


def get_conn():
    # abre a conexao com o banco
    conn = sqlite3.connect(DB)
    # row_factory deixa pegar os campos pelo nome: linha["nome"]
    conn.row_factory = sqlite3.Row
    # ativa a chave estrangeira (sem isso o CASCADE nao funciona)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_banco():
    conn = get_conn()

    # cria as tabelas se ainda nao existirem
    # pratos tem uma FOREIGN KEY que aponta para categorias(id)
    # ON DELETE CASCADE: apagou a categoria, apaga os pratos dela junto
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS pratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
        );
    """)

    # categorias iniciais (so entra se a tabela estiver vazia)
    total = conn.execute("SELECT COUNT(*) FROM categorias").fetchone()[0]
    if total == 0:
        conn.execute("INSERT INTO categorias (nome) VALUES ('Massas')")
        conn.execute("INSERT INTO categorias (nome) VALUES ('Pizzas')")
        conn.execute("INSERT INTO categorias (nome) VALUES ('Sobremesas')")
        conn.execute("INSERT INTO categorias (nome) VALUES ('Bebidas')")
        conn.execute("INSERT INTO categorias (nome) VALUES ('Vinhos')")

    # pratos iniciais (so entra se a tabela estiver vazia)
    total = conn.execute("SELECT COUNT(*) FROM pratos").fetchone()[0]
    if total == 0:
        # pega o id de cada categoria pelo nome
        massas = conn.execute("SELECT id FROM categorias WHERE nome = 'Massas'").fetchone()[0]
        pizzas = conn.execute("SELECT id FROM categorias WHERE nome = 'Pizzas'").fetchone()[0]
        sobremesas = conn.execute("SELECT id FROM categorias WHERE nome = 'Sobremesas'").fetchone()[0]
        bebidas = conn.execute("SELECT id FROM categorias WHERE nome = 'Bebidas'").fetchone()[0]
        vinhos = conn.execute("SELECT id FROM categorias WHERE nome = 'Vinhos'").fetchone()[0]

        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Pizza Margherita', 'Molho de tomate, mussarela e manjericao', 59.90, ?)", (pizzas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Pizza Calabresa', 'Calabresa, cebola e oregano', 54.90, ?)", (pizzas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Lasanha a Bolonhesa', 'Camadas de massa, molho bolonhesa e queijo', 68.00, ?)", (massas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Ravioli de Ricota', 'Massa recheada com ricota e espinafre', 62.50, ?)", (massas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Tiramisu', 'Sobremesa italiana com cafe e mascarpone', 24.90, ?)", (sobremesas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Cannoli', 'Massa crocante com recheio de ricota', 22.00, ?)", (sobremesas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Refrigerante', 'Lata 350ml', 8.00, ?)", (bebidas,))
        conn.execute("INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES ('Vinho Tinto', 'Taca de vinho tinto da casa', 28.00, ?)", (vinhos,))

    conn.commit()
    conn.close()
