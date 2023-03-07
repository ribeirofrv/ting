import os
import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        message = "Formato inválido"
    elif not os.path.exists(path_file):
        message = f"Arquivo {path_file} não encontrado"
    else:
        with open(path_file, "r") as file:
            return file.read().splitlines()

    print(message, file=sys.stderr)
    return None
