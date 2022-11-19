import pytest
import cards


def test_no_path_raises():
    with pytest.raises(TypeError):  # Code-block の何かが TypeError例外を発生させるはずことを意味する。
        cards.CardsDB()
        # 例外が発生しない場合、Test に失敗する
        # 指定した例外と異なる例外が発生した場合も Test は失敗する。


def test_raises_with_info():
    match_regex = 'missing 1 .* positional argument'
    with pytest.raises(TypeError, match=match_regex):  # match= は、正規表現を受け取って例外Message と照合する。
        cards.CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:  # Custom例外の場合は、as *** と変数名を使って例外の Parameter に関する情報を取得する。
        cards.CardsDB()
    expected = 'missing 1 required positional argument'
    assert expected in str(exc_info.value)
    # exe_info のObject型は、ExceptionInfo になる。
