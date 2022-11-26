import pytest
from cards import Card, InvalidCardId


def test_start(cards_db):
    """
    Start changes state "todo" to "in prog"
    """
    i = cards_db.add_card(Card("foo", state='todo'))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"


def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    any_number = 123  # db は空なので, iD番号はすべて無効
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)
