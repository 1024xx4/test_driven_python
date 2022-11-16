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

---

## Test を作成する際の構造の考え方

Test を構造化すると

- Test関数が整理された状態が保たれる。
- Test の対象が１つの振る舞いに絞られる。
- １つの初期状態に焦点を合わせると、同じ Action を使って Test する必要があるかもしれない他の状態について検討しやすくなる。
- １つの理想的な結果に焦点を合わせると、失敗状態や Error状態など、それ以外に予想される結果について考えるのに役立つ。

### 1. Given / Arrange

Test を駆動するときの初期状態。Action を実行するために Data または環境を整える。

### 2. When / Act

ある Action を実行する。その振る舞いが正しいかどうかを確認することが Test の焦点となる。

### 3. Then / Assert

結果、または最終状態の期待値。Test の最後に、Action の結果が期待どおりの振る舞いになったことを確認する。
