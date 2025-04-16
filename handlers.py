from typing import Union, List

from handlers_constants import (
    HANDLER_NAME,
    LEVEL_DEBUG, LEVEL_INFO, LEVEL_WARNING, LEVEL_ERROR, LEVEL_CRITICAL,
    LEVEL_NAMES, LEVELS
)



def init() -> List[Union[int, List]]:
    return []


def process(data: List[Union[int, List]], in_str: str) -> None:
    _, _, level, *parts = in_str.split()
    if parts[0] == 'django.request:':
        if parts[1] == 'GET':
            handler = parts[2]
        else:
            handler = parts[4]
        for element in data:
            if element[HANDLER_NAME] == handler:
                break
        else:
            element = [handler, 0, 0, 0, 0, 0]
            data.append(element)
        
        for level_name, level_index in zip(LEVEL_NAMES, LEVELS):
            if level == level_name:
                element[level_index] += 1


def merge(data_all: List[List[Union[int, List]]]) -> List[Union[int, List]]:
    result = data_all[0]
    for data in data_all[1:]:
        for element in data:
            for result_element in result:
                if result_element[HANDLER_NAME] == element[HANDLER_NAME]:
                    break
            else:
                result_element = [element[HANDLER_NAME], 0, 0, 0, 0, 0]
                result.append(result_element)
            
            for level in LEVELS:
                result_element[level] += element[level]

    return result


def result(data: List[Union[int, List]]) -> str:
    total_requests = 0
    lines = ['', '']    # Total requests + empty line
    lines.append('HANDLER              ' + ''.join(map(lambda x: x.ljust(10), LEVEL_NAMES)))
    total_debug, total_info, total_warning, total_error, total_critical = 0, 0, 0, 0, 0
    for element in sorted(data, key=lambda x: x[HANDLER_NAME]):
        lines.append(f'{element[HANDLER_NAME]:<21}' + ''.join(map(lambda x: f'{x:<10}', element[1:])))
        total_debug += element[LEVEL_DEBUG]
        total_info += element[LEVEL_INFO]
        total_warning += element[LEVEL_WARNING]
        total_error += element[LEVEL_ERROR]
        total_critical += element[LEVEL_CRITICAL]
        total_requests += sum(element[1:])
    lines.append(f'                     {total_debug:<9} {total_info:<9} {total_warning:<9} {total_error:<9} {total_critical:<9}')
    lines[0] = f'Total requests: {total_requests}'
    return '\n'.join(lines)
