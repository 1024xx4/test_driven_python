# test_driven_python
テスト駆動 Python 第２版 の Hands-on 

---
## Test の結果
| 表示          | 内容                                                     | 備考                                                   |
|-------------|--------------------------------------------------------|------------------------------------------------------|
| PASSED (.)  | Test が正常に実行されたことを意味する。                                 |                                                      |
| FAILED (F)  | Test が正常に実行されなかったことを意味する。                              |                                                      |
| SKIPPED (s) | この Test が Skip されたことを意味する。                             | `@pytest.mark.skip()` または `@pytest.mark.skipf()` を使う |
 | XFAIL (x)   | 失敗するはずの Test が実行され、想定どおりに失敗したことを意味する。                  | `@pytest.mark.xfail()` を使う                           |
| XPASS (X)   | xfail Maker が付いた Test の実行が想定に反して成功したことを意味する。           |                                                      |
| ERROR (E)   | 例外が Test関数の実行中ではなく Fixture または Hook関数の実行中に発生したことを意味する。 |                                                      |

### Tset で使用する Sample Application の Source-code
[https://media.pragprog.com/titles/bopytest2/code/bopytest2-code.zip](https://media.pragprog.com/titles/bopytest2/code/bopytest2-code.zip)

