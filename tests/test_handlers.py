import pytest

from handlers import init, process, merge, result


def test_init() -> None:
    assert init() == []


@pytest.mark.parametrize(
    'data, in_str, out_data',
    [
        (
            [],
            '2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]',
            [['/api/v1/reviews/', 0, 1, 0, 0, 0]]
        ),
        (
            [],
            '2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data',
            [['/admin/dashboard/', 0, 0, 0, 1, 0]]
        ),
    ]
)
def test_process(data, in_str: str, out_data) -> None:
    process(data, in_str)
    assert data == out_data


def test_merge() -> None:
    data_all = [
        [
            ['/admin/login/', 0, 1, 0, 0, 0],
            ['/admin/dashboard/', 1, 0, 0, 0, 0]
        ],
        [
            ['/api/v1/orders/', 0, 0, 1, 0, 0],
            ['/api/v1/checkout/', 0, 0, 0, 1, 0],
            ['/admin/login/', 0, 0, 0, 0, 1]
        ]
    ]
    data = [
        ['/admin/login/', 0, 1, 0, 0, 1],
        ['/admin/dashboard/', 1, 0, 0, 0, 0],
        ['/api/v1/orders/', 0, 0, 1, 0, 0],
        ['/api/v1/checkout/', 0, 0, 0, 1, 0]
    ]
    assert merge(data_all) == data


def test_result() -> None:
    data = [
        ['/api/v1/reviews/', 0, 1, 0, 0, 0],
        ['/admin/dashboard/', 0, 0, 0, 1, 0]
    ]
    assert result(data) == """Total requests: 2

HANDLER              DEBUG     INFO      WARNING   ERROR     CRITICAL  
/admin/dashboard/    0         0         0         1         0         
/api/v1/reviews/     0         1         0         0         0         
                     0         1         0         1         0        """
