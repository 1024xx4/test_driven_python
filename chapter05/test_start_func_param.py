import pytest
from cards import Card


@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_start_simple(cards_db, start_state):
    c = Card("second edition", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'
