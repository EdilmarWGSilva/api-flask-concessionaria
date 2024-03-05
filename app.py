from flask import Flask, request

app = Flask(__name__)

concessionaria = [
    {"veiculo": "HONDA", "items":
        [
            {"modelo": "CIVIC", "preco": 130000.00}
        ]
    },
     {"veiculo": "NISSAN", "items":
        [
            {"modelo": "SENTRA", "preco": 90000.00}
        ]
    }
    ]


@app.get("/concessionaria")
def get_concessionaria():
    return {"concessionaria": concessionaria}

@app.get("/concessionaria/<string:veiculo>")
def get_concessionaria_by_veiculo(veiculo):
    for loja in concessionaria:
        if loja["veiculo"] == veiculo:
            return loja
    return {"message": "Loja not found"}, 404

@app.get("/concessionaria/<string:veiculo>/item/")
def get_item_in_concessionaria(veiculo):
    for loja in concessionaria:
        if loja["veiculo"] == veiculo:
            return {"items": loja["items"]}
    return {"message": "Loja not found"}, 404

@app.post("/concessionaria")
def create_concessionaria():
    request_data = request.get_json() #pega o conteudo do body
    new_concessionaria = {"veiculo": request_data["veiculo"], "items": []}
    concessionaria.append(new_concessionaria) #insere o payload na viagens
    return new_concessionaria, 201

@app.post("/concessionaria/<string:veiculo>/item")
def create_item(veiculo):
    request_data = request.get_json()
    for loja in concessionaria:
        if loja["veiculo"] == veiculo:
            new_item = {"modelo": request_data["modelo"], "preco": request_data["preco"]}
            loja["items"].append(new_item)
            return new_item, 201
    return {"message": "Veiculo nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)