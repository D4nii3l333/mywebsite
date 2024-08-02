from flask import Flask, render_template, request
import os

app = Flask(__name__)


# Função para ler palavras proibidas de um arquivo
def carregar_palavras_proibidas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return [linha.strip() for linha in arquivo]


# Caminho para o arquivo de palavras proibidas
caminho_arquivo = (
    r"C:\Users\Sr.Matheus\Documents\projeto_milhonario\palavras_proibidas.txt"
)
palavras_proibidas = carregar_palavras_proibidas(caminho_arquivo)


@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    if request.method == "POST":
        texto = request.form["texto"]
        palavras_encontradas = [
            palavra for palavra in palavras_proibidas if palavra in texto
        ]
        if palavras_encontradas:
            mensagem = "\n".join(
                [
                    f"A palavra '{palavra}' foi encontrada em seu texto. Ela não é permitida na plataforma."
                    for palavra in palavras_encontradas
                ]
            )
        else:
            mensagem = "Tudo certinho, chefe!!!"
    return render_template("page.html", mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)
