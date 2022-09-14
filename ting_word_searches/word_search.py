def exists_word(word, instance):
    """Aqui irá sua implementação"""
    lines_numbers = []
    files_list = []
    for file in instance.data:
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                lines_numbers.append({"linha": i + 1})
        files_list.append({
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": lines_numbers,
            "palavra": word,
        })
    if len(lines_numbers) == 0:
        return []
    else:
        print(files_list)
        return files_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    lines_numbers = []
    files_list = []
    for file in instance.data:
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                lines_numbers.append({"linha": i + 1, "conteudo": line})
        files_list.append({
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": lines_numbers,
            "palavra": word,
        })
    if len(lines_numbers) == 0:
        return []
    else:
        print(files_list)
        return files_list

