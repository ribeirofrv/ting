from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):

    for item in range(len(instance)):
        file = instance.search(item)["nome_do_arquivo"]
        if file == path_file:
            return

    lines = txt_importer(path_file)
    num_lines = len(lines)
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": num_lines,
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_data)
    print(file_data)


def remove(instance: Queue):
    if instance:
        path_file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    pass
