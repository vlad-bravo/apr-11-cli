import pytest

from handlers import init, process, result


def test_init() -> None:
    assert init() == [0, []]


@pytest.mark.parametrize(
    'data, in_str, out_data',
    [
        (
            [0, []],
            '2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]',
            [1, [['/api/v1/reviews/', 0, 1, 0, 0 ,0]]]
        ),
        (
            [0, []],
            '2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data',
            [1, [['/admin/dashboard/', 0, 0, 0, 1, 0]]]
        ),
    ]
)
def test_process(data, in_str: str, out_data) -> None:
    process(data, in_str)
    assert data == out_data


def test_result() -> None:
    data = [
        2,
        [
            ['/api/v1/reviews/', 0, 1, 0, 0 ,0],
            ['/admin/dashboard/', 0, 0, 0, 1, 0]
        ]
    ]
    assert result(data) == """Total requests: 2

HANDLER              DEBUG     INFO      WARNING   ERROR     CRITICAL
/admin/dashboard/    0         0         0         1         0        
/api/v1/reviews/     0         1         0         0         0        
                     0         1         0         1         0        """
