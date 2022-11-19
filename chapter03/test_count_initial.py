from pathlib import Path
from tempfile import TemporaryDirectory
import cards


def test_empty():
    with TemporaryDirectory() as db_dir:  # Test の為、一時 Directory を使えば十分。
        db_path = Path(db_dir)  # Parameter として Database-directory を表す pathlib.Path Object を指定
        db = cards.CardsDB(db_path)  # Database Object を取得。(cards.CardDB() は、Constractor)

        count = db.count()
        db.close()

        assert count == 0
        """
        問題点:
        - .count() を呼び出す前に Database を setup する Code があるが Test自体にはあまり関係がない。
        - assert文の前に db.close() の呼び出しがあるが本来、関数の最後に配置するほうがいいが、そのようにすると assert が失敗した場合に
        呼び出されなくなってしまう。
        """
