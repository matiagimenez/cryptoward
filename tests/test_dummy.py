from cryptoward.main import sum_two_numbers


def test_should_pass() -> None:
    result = sum_two_numbers(2, 2)
    assert result == 4
