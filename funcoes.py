##Uma breve explicação sobre as funcionalidades do codigo. O codigo tem a função de ler as palavras digitadas pelo úsuario e identifica pelo banco de dados palavras considerada feia.


# Lista de palavras proibidas
# Função para ler palavras proibidas de um arquivo
def carregar_palavras_proibidas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return [linha.strip() for linha in arquivo]


# Caminho para o arquivo de palavras proibidas
caminho_arquivo = (
    r"C:\Users\Sr.Matheus\Documents\projeto_milhonario\palavras_proibidas.txt"
)

# Carregar palavras proibidas
palavras_proibidas = carregar_palavras_proibidas(caminho_arquivo)

# Solicitar entrada do usuário
pala = input("Digite o texto: ")

# Encontrar palavras proibidas no texto
palavras_encontradas = [palavra for palavra in palavras_proibidas if palavra in pala]

# Verificar e informar sobre palavras proibidas
if palavras_encontradas:
    for palavra in palavras_encontradas:
        print(
            f"A palavra '{palavra}' foi encontrada em seu texto. Ela não é permitida na plataforma."
        )
else:
    print("Tudo certinho, chefe!!!")
