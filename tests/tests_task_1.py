import pytest
import task_1


@pytest.mark.parametrize(
    "lst, expected",
    (
            [[1, 1, 1, 2, 3], 1],
            [[1, 2, 3, 2, 2], 2]
    )
)
def test_vote(lst, expected):
    actual = task_1.vote(lst)
    assert actual == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
            [10, 10, 10, "Равносторонний треугольник"],
            [11, 5, 11, "Разносторонний треугольник"],
            [5, 5, 7, "Равнобедренный треугольник"]
    )
)
def test_check_triangle(a, b, c, expected):
    actual = task_1.check_triangle(a, b, c)
    assert actual == expected


@pytest.mark.parametrize(
    "login, password, expected",
    (
            ["Admin", "Password", "Доступ ограничен"],
            ['ghb', "odps", "Доступ ограничен"],
            ["admin", "password", "Добро пожаловать"]
    )
)
def test_check_auth(login, password, expected):
    actual = task_1.check_auth(login, password)
    assert actual == expected
