import cards
import pytest


@pytest.fixture(scope='session')
def db(tmp_path_factory):  # 組み込み Fixture tmp_path_factory を使用することで pathlib や tempfile を import する必要がなくなる。
    """CardsDB object connected to a temporary database"""
    db_path = tmp_path_factory.mktemp('cards_db')
    db_ = cards.Cards(db_path)
    yield db_
    db_.close()

