from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest


@pytest.fixture(scope='session')
def cards_db():
    """
    Database を初期化する Fixture
    Test の Setup として Database を準備する。
    """
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db  # Test関数を実行する Timing.
        db.close()  # Teardown: Test 中に何が起こったとしても必ず実行される。
