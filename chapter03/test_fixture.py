import pytest


@pytest.fixture()  # この関数が Fixture であることを pytest に認識させる修飾子。
def some_data():
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data):  # Test関数の Parameter に Fixture関数の名前を追加すると、Test実行前にその Fixture を実行。
    """Use fixture return value in a test."""
    assert some_data == 42
    """
    Fixture の実行時と Test関数の実行時と例外の扱い方が異なり、Debug 時に役立つ。
    - Test関数実行時の例外 => FAILED になる。
    - Fixtureの実行時の例外 => ERROR になる。
    """
