from flask import Flask , jsonify

app = Flask ( __name__ )

produtos = [
    {"id": 1, " nome ": " Teclado ", " preco ": 150.0 , " disponivel ": True } ,
    {"id": 2, " nome ": " Mouse ", " preco ": 80.0 , " disponivel ": True } ,
    {"id": 3, " nome ": " Monitor ", " preco ": 900.0 , " disponivel ": False } ,
    {"id": 4, " nome ": " Webcam ", " preco ": 200.0 , " disponivel ": True }
]
@app . route ("/produtos ")
def listar_produtos () :
    return jsonify ( produtos )

if __name__ == " __main__ ":
    app . run ( debug = True )