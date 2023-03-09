from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    word_counter = []
    qsize = len(instance)
    count_line = 0

    for i in range(qsize):
        file = instance.search(i)
        occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line in file["linhas_do_arquivo"]:
            count_line += 1
            if word.lower() in line.lower():
                occurrences["ocorrencias"].append({"linha": count_line})

        if len(occurrences["ocorrencias"]) > 0:
            word_counter.append(occurrences)

    return word_counter


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
