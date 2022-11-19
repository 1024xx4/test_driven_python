from cards import Card


def test_to_dict():
    # GIVEN a Crad object with known contents.
    # 前提: 既知の値が設定された Card object が与えられたとすれば
    c1 = Card('something', 'brian', 'todo', 123)

    # WHEN we call to_dict() on the object.
    # もし：この Object で to_dict()を呼び出したときに
    c2 = c1.to_dict()

    # THEN the result will be a dictionary with known content.
    # ならば: 既知の値が設定された Dictionary が返される
    c2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123,
    }
    assert c2 == c2_expected

