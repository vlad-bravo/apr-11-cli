from typing import Union, List


def init() -> List[Union[int, List]]:
    return [0, []]


def process(data: List[Union[int, List]], in_str: str) -> None:
    _, _, level, *parts = in_str.split()
    if parts[0] == 'django.request:':
        if parts[1] == 'GET':
            handler = parts[2]
        else:
            handler = parts[4]
        for element in data[1]:
            if element[0] == handler:
                break
        else:
            element = [handler, 0, 0, 0, 0, 0]
            data[1].append(element)
        if level == 'DEBUG':
            element[1] += 1
        elif level == 'INFO':
            element[2] += 1
        elif level == 'WARNING':
            element[3] += 1
        elif level == 'ERROR':
            element[4] += 1
        elif level == 'CRITICAL':
            element[5] += 1
        data[0] += 1


def result(data: List[Union[int, List]]) -> str:
    lines = [f'Total requests: {data[0]}']
    lines.append('')
    lines.append('HANDLER              DEBUG     INFO      WARNING   ERROR     CRITICAL')
    total_debug, total_info, total_warning, total_error, total_critical = 0, 0, 0, 0, 0
    for element in sorted(data[1], key=lambda x: x[0]):
        lines.append(f'{element[0]:<20} {element[1]:<9} {element[2]:<9} {element[3]:<9} {element[4]:<9} {element[5]:<9}')
        total_debug += element[1]
        total_info += element[2]
        total_warning += element[3]
        total_error += element[4]
        total_critical += element[5]
    lines.append(f'                     {total_debug:<9} {total_info:<9} {total_warning:<9} {total_error:<9} {total_critical:<9}')
    return '\n'.join(lines)
