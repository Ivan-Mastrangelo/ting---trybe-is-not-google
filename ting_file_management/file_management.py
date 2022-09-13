import os.path
import sys


def txt_importer(path_file):
    """Aqui irá a implementação"""
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    elif os.path.splitext(path_file)[-1] != ".txt":
        print("Formato inválido", file=sys.stderr)
    else:
        with open(path_file, "r", encoding="utf-8") as file:
            text = file.read()
            new_text = text.split("\n")
            return new_text

# Reference: https://pt.stackoverflow.com/questions/382049/
# verificar-extens%C3%B5es-de-arquivos-em-python &
# https://docs.python.org/pt-br/3/library/os.path.html
