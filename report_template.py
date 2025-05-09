def init():
    """Функция возвращает необходимую для обработки отчета структуру данных."""
    return [0]


def process(data, in_str):
    """Процедура принимает структуру данных и строку лог-файла.
    При обработке строки лог-файла необходимо внести изменения в структуру данных."""
    data[0] += 1


def merge(data_all):
    """Функция принимает массив результатов обработки различных логов и возвращает объединённый результат"""
    result = data_all[0]
    for data in data_all[1:]:
        result[0] += data[0]
    return result


def result(data):
    return f'Total lines: {data[0]}'
