def test_tmp_path(tmp_path):  # scope='function'
    file = tmp_path / 'file.txt'
    file.write_text(('Hello'))
    assert file.read_text() == 'Hello'


def test_tmp_path_factory(tmp_path_factory):  # scope='session'
    path = tmp_path_factory.mktemp('sub')  # Directory を取得するために mktemp() を呼び出す必要がある。
    file = path / 'file.txt'
    file.write_text('Hello')
    assert file.read_text() == 'Hello'
