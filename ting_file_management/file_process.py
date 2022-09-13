from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    file_text = txt_importer(path_file)
    processed = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_text),
        "linhas_do_arquivo": file_text,
    }

    instance.enqueue(processed)
    print(processed, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    path_file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if 0 <= position < len(instance):
        file_info = instance.search(position)
        print(file_info, file=sys.stdout)
    else:
        print("Posição inválida", file=sys.stderr)
