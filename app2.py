from flask import Flask, request

app = Flask(__name__)

viagens = [
    {"pais": "EUA", "items":
        [
            {"cidade": "Massasshussets", "preco": 1500.99}
        ]
    },
     {"pais": "Inglaterra", "items":
        [
            {"cidade": "Londres", "preco": 1500.99}
        ]
    }
    ]

#get
#127.0.0.1:5000/viagens
@app.get("/viagens")
def get_viagens():
    return {"viagens": viagens}

#127.0.0.1:5000/viagens/COLOQUEOPAISAPESQUIAR
@app.get("/viagens/<string:pais>")
def get_viagens_by_pais(pais):
    for viagem in viagens:
        if viagem["pais"] == pais:
            return viagem
    return {"message": "Viagens not found"}, 404

#127.0.0.1:5000/viagens/PAISAPESQUISAR/ITEM
@app.get("/viagens/<string:pais>/item/")
def get_item_in_viagens(pais):
    for viagem in viagens:
        if viagem["pais"] == pais:
            return {"items": viagem["items"]}
    return {"message": "Viagens not found"}, 404

@app.post("/viagens")
def create_viagens():
    request_data = request.get_json() #pega o conteudo do body
    new_viagens = {"pais": request_data["pais"], "items": []}
    viagens.append(new_viagens) #insere o payload na viagens
    return new_viagens, 201

@app.post("/viagens/<string:pais>/item")
def create_item(pais):
    request_data = request.get_json()
    for viagem in viagens:
        if viagem["pais"] == pais:
            new_item = {"cidade": request_data["cidade"], "preco": request_data["preco"]}
            viagem["items"].append(new_item)
            return new_item, 201
    return {"message": "Pais nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)