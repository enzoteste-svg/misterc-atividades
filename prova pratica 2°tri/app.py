from flask import Flask, jsonify, render_template, request

from database import get_conn, criar_banco

app = Flask(__name__)

criar_banco()


def pratos_para_json(linhas):
    lista = []
    for p in linhas:
        lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "descricao": p["descricao"],
            "preco": p["preco"],
            "categoria_id": p["categoria_id"],
        })
    return lista


@app.route("/")
def site():
    return render_template("index.html")


# ====================== CATEGORIAS ======================

# GET /categorias - lista todas
@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conn = get_conn()
    linhas = conn.execute("SELECT * FROM categorias ORDER BY id").fetchall()
    conn.close()

    categorias = []
    for c in linhas:
        categorias.append({"id": c["id"], "nome": c["nome"]})
    return jsonify(categorias)


# GET /categorias/1 - mostra uma so
@app.route("/categorias/<int:id>", methods=["GET"])
def ver_categoria(id):
    conn = get_conn()
    # o "?" e um parametro, assim o valor nunca vai junto do SQL
    # (isso evita SQL Injection)
    c = conn.execute("SELECT * FROM categorias WHERE id = ?", (id,)).fetchone()
    conn.close()

    if c is None:
        return jsonify({"erro": "Categoria nao encontrada"}), 404

    return jsonify({"id": c["id"], "nome": c["nome"]})


# POST /categorias - cria uma nova
@app.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.get_json(silent=True)
    if not dados or "nome" not in dados:
        return jsonify({"erro": "O campo nome e obrigatorio"}), 400

    conn = get_conn()
    cur = conn.execute("INSERT INTO categorias (nome) VALUES (?)", (dados["nome"],))
    conn.commit()
    nova = conn.execute("SELECT * FROM categorias WHERE id = ?", (cur.lastrowid,)).fetchone()
    conn.close()

    return jsonify({"id": nova["id"], "nome": nova["nome"]}), 201


# PUT /categorias/1 - atualiza o nome
@app.route("/categorias/<int:id>", methods=["PUT"])
def editar_categoria(id):
    dados = request.get_json(silent=True)
    if not dados or "nome" not in dados:
        return jsonify({"erro": "O campo nome e obrigatorio"}), 400

    conn = get_conn()
    c = conn.execute("SELECT * FROM categorias WHERE id = ?", (id,)).fetchone()
    if c is None:
        conn.close()
        return jsonify({"erro": "Categoria nao encontrada"}), 404

    conn.execute("UPDATE categorias SET nome = ? WHERE id = ?", (dados["nome"], id))
    conn.commit()
    atualizada = conn.execute("SELECT * FROM categorias WHERE id = ?", (id,)).fetchone()
    conn.close()

    return jsonify({"id": atualizada["id"], "nome": atualizada["nome"]})


# DELETE /categorias/1 - apaga (e os pratos dela, por causa do CASCADE)
@app.route("/categorias/<int:id>", methods=["DELETE"])
def apagar_categoria(id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # rowcount = quantas linhas foram apagadas
    if cur.rowcount == 0:
        return jsonify({"erro": "Categoria nao encontrada"}), 404

    return jsonify({"mensagem": "Categoria apagada (e os pratos dela junto)"})


# ====================== PRATOS ======================

# GET /pratos - lista todos
@app.route("/pratos", methods=["GET"])
def listar_pratos():
    conn = get_conn()
    linhas = conn.execute("SELECT * FROM pratos ORDER BY id").fetchall()
    conn.close()

    return jsonify(pratos_para_json(linhas))


# GET /pratos/1 - mostra um so
@app.route("/pratos/<int:id>", methods=["GET"])
def ver_prato(id):
    conn = get_conn()
    p = conn.execute("SELECT * FROM pratos WHERE id = ?", (id,)).fetchone()
    conn.close()

    if p is None:
        return jsonify({"erro": "Prato nao encontrado"}), 404

    return jsonify({
        "id": p["id"],
        "nome": p["nome"],
        "descricao": p["descricao"],
        "preco": p["preco"],
        "categoria_id": p["categoria_id"],
    })


# POST /pratos - cria um novo
@app.route("/pratos", methods=["POST"])
def criar_prato():
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie os dados em JSON"}), 400

    # campos que nao podem faltar
    for campo in ("nome", "preco", "categoria_id"):
        if campo not in dados:
            return jsonify({"erro": "O campo " + campo + " e obrigatorio"}), 400

    conn = get_conn()

    # confere se a categoria do prato existe
    cat = conn.execute("SELECT id FROM categorias WHERE id = ?", (dados["categoria_id"],)).fetchone()
    if cat is None:
        conn.close()
        return jsonify({"erro": "Categoria nao encontrada"}), 400

    cur = conn.execute(
        "INSERT INTO pratos (nome, descricao, preco, categoria_id) VALUES (?, ?, ?, ?)",
        (dados["nome"], dados.get("descricao"), dados["preco"], dados["categoria_id"]),
    )
    conn.commit()
    novo = conn.execute("SELECT * FROM pratos WHERE id = ?", (cur.lastrowid,)).fetchone()
    conn.close()

    return jsonify({
        "id": novo["id"],
        "nome": novo["nome"],
        "descricao": novo["descricao"],
        "preco": novo["preco"],
        "categoria_id": novo["categoria_id"],
    }), 201


# PUT /pratos/1 - atualiza um prato
@app.route("/pratos/<int:id>", methods=["PUT"])
def editar_prato(id):
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie os dados em JSON"}), 400

    conn = get_conn()
    p = conn.execute("SELECT * FROM pratos WHERE id = ?", (id,)).fetchone()
    if p is None:
        conn.close()
        return jsonify({"erro": "Prato nao encontrado"}), 404

    # pega o que veio no JSON, e se nao veio, mantem o que ja tinha
    nome = dados.get("nome", p["nome"])
    descricao = dados.get("descricao", p["descricao"])
    preco = dados.get("preco", p["preco"])
    categoria_id = dados.get("categoria_id", p["categoria_id"])

    # se for mudar a categoria, confere se ela existe
    if "categoria_id" in dados:
        cat = conn.execute("SELECT id FROM categorias WHERE id = ?", (categoria_id,)).fetchone()
        if cat is None:
            conn.close()
            return jsonify({"erro": "Categoria nao encontrada"}), 400

    conn.execute(
        "UPDATE pratos SET nome = ?, descricao = ?, preco = ?, categoria_id = ? WHERE id = ?",
        (nome, descricao, preco, categoria_id, id),
    )
    conn.commit()
    atualizado = conn.execute("SELECT * FROM pratos WHERE id = ?", (id,)).fetchone()
    conn.close()

    return jsonify({
        "id": atualizado["id"],
        "nome": atualizado["nome"],
        "descricao": atualizado["descricao"],
        "preco": atualizado["preco"],
        "categoria_id": atualizado["categoria_id"],
    })


# DELETE /pratos/1 - apaga um prato
@app.route("/pratos/<int:id>", methods=["DELETE"])
def apagar_prato(id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM pratos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    if cur.rowcount == 0:
        return jsonify({"erro": "Prato nao encontrado"}), 404

    return jsonify({"mensagem": "Prato apagado"})


# ====================== JOIN ======================

# GET /pratos/join - mostra os pratos com o nome da categoria
# INNER JOIN junta as duas tabelas pelo id da categoria
@app.route("/pratos/join", methods=["GET"])
def pratos_com_categoria():
    conn = get_conn()
    linhas = conn.execute("""
        SELECT pratos.id, pratos.nome, pratos.descricao, pratos.preco,
               categorias.nome AS categoria
        FROM pratos
        INNER JOIN categorias ON pratos.categoria_id = categorias.id
        ORDER BY pratos.id
    """).fetchall()
    conn.close()

    lista = []
    for p in linhas:
        lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "descricao": p["descricao"],
            "preco": p["preco"],
            "categoria": p["categoria"],
        })
    return jsonify(lista)


# ====================== FILTROS ======================

# GET /categorias/2/pratos - todos os pratos de uma categoria
@app.route("/categorias/<int:id>/pratos", methods=["GET"])
def pratos_da_categoria(id):
    conn = get_conn()

    # confere se a categoria existe
    cat = conn.execute("SELECT * FROM categorias WHERE id = ?", (id,)).fetchone()
    if cat is None:
        conn.close()
        return jsonify({"erro": "Categoria nao encontrada"}), 404

    # filtra os pratos por categoria_id
    linhas = conn.execute("SELECT * FROM pratos WHERE categoria_id = ? ORDER BY id", (id,)).fetchall()
    conn.close()

    return jsonify(pratos_para_json(linhas))


# GET /pratos/busca?nome=pizza - procura pelo nome com LIKE
# aceita varios filtros juntos: nome, preco (minimo) e preco_max
@app.route("/pratos/busca", methods=["GET"])
def buscar_pratos():
    nome = request.args.get("nome", "")
    preco = request.args.get("preco")
    preco_max = request.args.get("preco_max")

    # o WHERE 1=1 deixa a gente ir juntando os filtros com AND
    sql = "SELECT * FROM pratos WHERE 1=1"
    valores = []

    if nome:
        # LIKE com % procura em qualquer parte do nome
        sql += " AND nome LIKE ? COLLATE NOCASE"
        valores.append("%" + nome + "%")

    if preco:
        sql += " AND preco >= ?"
        valores.append(float(preco))

    if preco_max:
        sql += " AND preco <= ?"
        valores.append(float(preco_max))

    sql += " ORDER BY id"

    conn = get_conn()
    linhas = conn.execute(sql, valores).fetchall()
    conn.close()

    return jsonify(pratos_para_json(linhas))


# ====================== LEFT JOIN (extra) ======================

# GET /categorias/com-pratos - todas as categorias com os pratos dela
# LEFT JOIN mostra tambem as categorias que nao tem prato
@app.route("/categorias/com-pratos", methods=["GET"])
def categorias_com_pratos():
    conn = get_conn()
    linhas = conn.execute("""
        SELECT categorias.id, categorias.nome, pratos.nome AS nome_prato
        FROM categorias
        LEFT JOIN pratos ON pratos.categoria_id = categorias.id
        ORDER BY categorias.id
    """).fetchall()
    conn.close()

    resultado = []
    for l in linhas:
        # procura se essa categoria ja esta na lista
        achou = False
        for cat in resultado:
            if cat["id"] == l["id"]:
                if l["nome_prato"]:
                    cat["pratos"].append(l["nome_prato"])
                achou = True
                break

        # se nao estava, cria uma nova
        if not achou:
            pratos = []
            if l["nome_prato"]:
                pratos.append(l["nome_prato"])
            resultado.append({
                "id": l["id"],
                "nome": l["nome"],
                "pratos": pratos,
            })

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)