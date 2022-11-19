# test_driven_python

テスト駆動 Python 第２版 の Hands-on

#### Sample Code

https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/
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

---

## Test の OPP(Object Oriented Programing)の考察

- 基本的には、Test をまとめて実行しやすくする目的のみで利用する。
- Test Class の階層を利用して Helper-method を継承することなど可能だが極力避ける。
  ※ Test-class の継承を使って何か凝ったことをしようとすると、混乱の原因になる。

---

## Test の一部を実行する方法

| 実行する部分               | 構文                                                     |
|----------------------|--------------------------------------------------------|
| Test-method を１つだけ    | `pytest <pass> test_module.py::TestClass::test_method` |
| Class内のすべての Test     | `pytest <pass> test_module.py::TestClass`              |
| Test関数を１つだけ          | `pytest <pass> test_module.py::test_function`          |
| Module内のすべての Test    | `pytest <pass>`                                        |
| Directory内のすべての Test | `pytest -, <pattern>`                                  |

-k flag を and, not, or の３つの Keyword と組み合わせると非常に柔軟な指定が可能になり、実行したい Test を正確に選択できるようになる。
Debug や新しい Test の開発を行なっているときに非常に役立つ。

## Fixture

Test-helper関数。  
実際の Test 関数の実行に先だって（場合によってはその後に）pytest が実行する関数。  
必要であればどのような処理でも実行できる。

### 使用例

- Test で使う Dataset の取得。
- Test を実行する前に System をあらかじめ定めた状態にする。
- 複数の Test で使う Data を準備する。

etc...

### Scope parameter の有効な値

| Parameter の値       | 説明                                                                                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `scope='function'` | Test関数や Method ごとに１回実行される。Setup部分はこの Fixture を使っている Test の前に実行され、Teardown部分はその Test の後に実行される。function は scope parameter が指定されない場合に使われる Defalut の scope. |
| `scope='class`     | Test class ごとに１回実行される。その Test class に Method がいくつ定義されていたとしても、実行されるのは１回だけ。                                                                               |
| `scope='module'`   | Module ごとに１回実行される。その Module に Test関数、Test-method, または他の Fixture がいくつ定義されていたとしても、実行されるのは１回だけ。                                                            |
| `scope='package'`  | Package ごとに１回実行される。その Package に Test関数、Test-method, または他の Fixture がいくつ定義されていたとしても、実行されるのは１回だけ。                                                          |
| `scope='session'`  | Session ごとに１回実行される。pytest command を使って Test を１回実行するのが１回の Session. Session-scope の Fixture を使っている Test-method や Test関数はすべて同じ Setup/Teardown 呼び出しを共有する。   |

※ Fixture が Test-module の中で定義されている場合、

- session-scope
- package-scope

の働きは module-scope とまったく同じになる。Fixture を conftest.py File に配置することで働き方が差別化される。