# Converter palavras_proibidas.txt para um array JavaScript
input_path = r"C:\Users\Sr.Matheus\Documents\projeto_milhonario\palavras_proibidas.txt"
output_path = r"C:\Users\Sr.Matheus\Documents\projeto_milhonario\palavras_proibidas.js"

with open(input_path, "r", encoding="utf-8") as infile:
    palavras = [line.strip().lower() for line in infile]  # Converter para minúsculas

with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.write("const palavrasProibidas = " + str(palavras) + ";")
