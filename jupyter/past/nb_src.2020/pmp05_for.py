

""" md

# {C.inc_section}. for文

 * for文は同じ文を何度も繰り返し実行する文で, 関数を定義できる機能と合わせてプログラム言語の最重要機能
 * 「同じ文を何度も繰り返し」実行と言っても全く同じ計算を何度も繰り返しても意味がない. 「変数」を使うと, 同じ文でも異なる計算ができる. 
 * もう一つの重要な文が if文. 条件によってことなる動作をさせたい時に使う
 * 関数定義, for, ifを使いこなせばかなりのことができるようになる
 * この節では for 文を練習する

"""

""" md

# {C.section}-{C.inc_subsection}. 基本

for文の一番簡単な例は以下

"""

""" exec-code-box """
for i in range(2, 7):
    print(i)


""" md

__for文の文法:__

```
for 名前 in range ( 式1 , 式2 ) : 
    文1
    ...
    文m
```

 * __文法上の注意:__
  * 関数定義と同様, for文の中身は字下げをする必要がある
  * 複数の文 (文1 ... 文m)を並べることができるがその場合は同じだけ字下げをする

 * __for文の意味(実行規則):__
  * まず式1と式2が計算される. 結果をそれぞれa, bとする
  * a, bはともに整数でなくてはならない. そうでなければエラーになる
  * 「名前(変数)」をa, a+1, a+2, ... b-1 (a以上b未満)として文1 ... 文m が繰り返し(つまり(b - a)回)実行される

"""

""" md
したがって

```
for i in range(2, 7):
    print(i)
```

を実行すると,
```
print(2)
print(3)
print(4)
print(5)
print(6)
```

を実行したのと同じことになる.

"""

""" md

なお, 式1 (と ,)を省略することもでき, その場合は式1は0の意味になる.  つまり

```
for 名前 in range (式) : 
    文1
    ...
    文m
```

は

```
for 名前 in range (0, 式) : 
    文1
    ...
    文m
```

の意味. 

"""

""" md

__for文にまつわる用語:__

```
for 名前 in range ( 式1, 式2 ) : 
    文1
    ...
    文m
```

において,

 * 文1, ..., 文m のことをfor文の「本体」という
 * プログラミング言語ではfor文に限らず, 同じ文を繰り返し実行する文が他にもある. これらのことを一般に「ループ」とも言う. 「ループ」を使いこなせるようになることはプログラミング言語になれることの多くの部分を占める

"""

""" md

__for 文を実行しながら, 変数を更新していき, 終了時にその変数に答えが入っているようにする__ というパターンが非常に多く現れる. 

例えば以下は 0 + 1 + 2 + ... + 99 を計算する for 文である(以下を実行すると s に答えが格納される).

"""

""" exec-code-box """
s = 0
for i in range(100):
    s += i

""" exec-code-box """
s
    
""" md

関数を使えば「100」の部分をパラメータにすることが出来, 以下は, nが与えられたら, 0 + 1 + ... + (n-1) を計算する関数である.

"""

""" exec-code-box """
def sum_to_n(n):
    s = 0
    for i in range(n):
        s += i
    return s

""" exec-code-box """
sum_to_n(100)

""" exec-code-box """
sum_to_n(1000)

""" md 

繰り返しは同じ文を一度書くだけで何度も実行できるようになるので, 100回同じ文を実行するのに同じ文を100回書かなくて済む, というご利益もあるのだが, もっと大事なことは, 繰り返し__回数自身をパラメータにできる__ (nを与えられたらn回繰り返すとか, 答えを求めるのに必要な回数だけ繰り返すなど)というところ. この機能がないと, 「与えられたnに対し 0 + 1 + ... + (n-1) を計算する」関数を書くことは困難である.

"""

""" md

# for 文を使って「やりたい計算」をするときの考え方

例題として, 「nを与えられたらn!」を計算する関数 fact(n) を書いてみよう.
つまり,

> fact(n) = 1 * 2 * ... * n

この右辺をこのままではプログラムに出来ない理由は, ... が含まれているからで, ... を「同じ文の繰り返し」に焼き直すことが for文への翻訳ということになる. 

自分が紙の上でどう, 20! を計算するかを思い浮かべてみると良い. すると

```
  1 * 1 -> 1
  1 * 2 -> 2
  2 * 3 -> 6
  6 * 4 -> 24
 24 * 5 -> 120
120 * 6 -> 720
720 * 7 -> 5040 
    ...

これ以上は真面目に計算する気も起きなくなるし, そもそもやっても意味がないので, ??? で記す

5040 *  8 -> ???
 ??? *  9 -> ???
 ??? * 10 -> ???
 ??? * 11 -> ???
 ??? * 12 -> ???
     ...
 ??? * 19 -> ???
 ??? * 20 -> ??? <- これが答え

```

ということをやっている. これが「(値こそ違うものの)同じ計算を繰り返している」ことを見抜くのはたやすいと思う. 

また, 特に後半の, ??? を含んだ計算を見ると, それらは変数を使って「同じ文」を繰り返しているだけだと容易にわかる. つまり,

```
 ??? * i -> ???
```

という計算, きちんとした Python の文として書けば,

```
 ??? = ??? * i
```

という代入文を, i = 1, 2, ..., n まで変えながら実行しているだけであると見抜ける.

??? は変数名として合法ではないので, pとでもしよう.

そこで求めたい関数の骨格は,

"""

""" exec-code-box """
def fact(n):
    for i in range(1, n+1):
        p = p * i
    return p

""" md
このプログラムは 80% 正しいのだが残念ながら実行すると以下のエラーになる

"""

""" error-code

fact(5)

"""

""" md

それは,

```
        p = p * i
```

を「初めて」つまり i = 1 で実行する時に, まだpに一度も代入されていないことから来るエラーである. 上記の計算のはじめに戻ると,

```
  1 * 1 -> 1
  1 * 2 -> 2
  2 * 3 -> 6
```

1行目の「最初の1」を設定してやることが必要である. そこで, for 文に突入する前に,

```
p = 1
```

を実行しておく. 以下が正解

"""

""" exec-code-box """
def fact(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

""" exec-code-box """
fact(1)

""" exec-code-box """
fact(2)

""" exec-code-box """
fact(3)

""" exec-code-box """
fact(4)

""" exec-code-box """
fact(5)

""" md


__このようなプログラムは「超頻出パターン」.__ 

具体的には

 1. ループ実行前に変数の初期値をセット
 1. ループ中 (for文の本体中)で, 変数を繰り返し更新する
 1. ループ終了時に変数に求めたい答えが残っている

というパターン.
こういうものを書けるようになることはプログラムによる計算になれることの多くの部分を占める.

そして, 「for文の中で繰り返し更新される変数」が出てきたら, 99%, for文実行に先立って初期値を代入しておく必要があるので, for文を書いているときは反射的に「初期値を代入しなくてよいか?」と気をつけるようになって下さい.

"""

""" md

# 問題 {C.inc_problem} : 漸化式

実数$a$, $b$, $c$と整数$n$を受取り,

$$ x_0 = c $$
$$ x_n = a x_{{n-1}} + b $$

で定まる数列 ${{x_n}}$ の 第$n$項 ($x_n$)を求める関数 linrec(a,b,c,n) を書け.

"""

""" write-code-box """

""" answer-code-box """
def linrec(a, b, c, n):
    x = c
    for i in range(n):
        x = a * x + b
    return x


""" test-code-box """
# a が1ならただの等差数列
assert(linrec(1,1,0,100) == 100), (linrec(1,1,0,100), 100)
# b が0ならただの等比数列
assert(linrec(3,0,1,10) == 3 ** 10), (linrec(3,0,1,10), 3 ** 10)

def check_linrec(a, b, c):
    # |a| < 1 の場合, ax+b = x の解に収束する
    n = 1000000
    x_inf = linrec(a, b, c, n)
    assert(abs(a * x_inf + b - x_inf) < 1.0e-6), (x_inf, a * x_inf + b)

check_linrec(0.875, 1.0, 1.0)
print("OK")

""" md 

for文で変数を繰り返し更新するという計算は, ほとんど漸化式の計算そのものと言っても良い.  一般に,

```
x = c
for i in range(n):
    x = f(x)
```

という計算をした結果, for文終了後にxに格納されるのは, 

$$ x_0 = c $$
$$ x_{{i+1}} = f(x_i) \quad\quad\quad (\dagger) $$

で定まる数列の$x_n$そのものである(※). それは以下のように考えればすぐにわかる(数学的帰納法).

 * $n=0$のとき主張(※)は正しい: 実際プログラムの方では, for文は一回も繰り返さないので終了後にx=cを満たしている. それは実際$x_0$と等しい.
 * $n=k$まで主張(※)が正しかったとする. すなわち
```
x = c
for i in range(k):
    x = f(x)
```
は終了後にx=$x_k$を満たしているとする.
すると,
```
x = c
for i in range(k+1):
    x = f(x)
```
が終了した際にxに残る値は明らかに$f(x_k)$で, すなわちそれは$x_{{k+1}}$である. 故に主張(※)は$n = k+1$の場合も正しい

だから, 求めたい値を for 文に翻訳するのに, 前述したような, 計算の過程をイメージする代わりに, 求めたい値を($\dagger$)の形式の漸化式で書いてみるというのは良い手段である. なお, 上記では 

$$ x_{{i+1}} = f(x_i) $$

という形式の漸化式, つまり, $x_{{i+1}}$が$x_i$だけで(直接$i$によらず)決まる式を書いたが, 漸化式が

$$ x_{{i+1}} = f(x_i, i) $$

という形式(右辺に$i$が直接含まれる)をしていても同じことである.

例えば$n$を与えられて

$$  0 + 1 + ... + (n-1) $$

を計算するプログラムを書けと言われたら以下のように考えれば良い.

 * 上記を $s_n$ とするとそれは以下の漸化式を満たす

$$ s_0 = 0 $$
$$ s_{{i+1}} = s_i + i $$

ゆえに,

```
def sum_to_n(n):
  s = 0
  for i in range(n):
    s = s + i
  return s
```

でそれが計算できる.

"""

""" md

しつこいようだがもう一つの例題として, $n$を与えられて $n!$

$$ 1 \cdot 2 \cdot \cdots \cdot n $$

を計算するプログラムを書けと言われたら以下のように考えれば良い.

 * 上記を $p_n$ とすると

$$ p_0 = 1 $$
$$ p_{{i+1}} = p_i \cdot (i + 1) $$

である. 故に以下が答え

```
def fact(n):
    p = 1
    for i in range(n):
        p = p * (i + 1)
    return p
```

"""

""" md

# 問題 {C.inc_problem} 

次で定まる数列の第$n$項を計算する関数sqrt3(c, n)を書け．

$$ \begin{{array}}{{rcl}}
a_0 & = & c, \\
a_{{n+1}} & = & \frac{{1}}{{3}} \left(2a_{{n}} + \frac{{c}}{{a_{{n}}^2}}\right) \;\; (n > 0).
\end{{array}} $$

これは$\sqrt[3]{{c}}$に収束する数列で, 
ある程度大きな$n$に対して, 
a($c$, $n$)を計算すればそれが, $\sqrt[3]{{c}}$の近似値となる.

a($c$, $n$)を3乗して, 結果がほぼ$c$と同じになるか確かめよ．

"""

""" write-code-box """

""" answer-code-box """
def sqrt3(c, n):
    x = c
    for i in range(n):
        x = (2 * x + c / (x * x)) / 3
    return x

""" test-code-box """
assert(sqrt3(27, 100) == 3), sqrt3(27, 100)
assert(abs(sqrt3(10, 100) ** 3 - 10) < 1.0e-5), sqrt3(10, 100)


""" md

以降の練習のため, 

for文を一回繰り返す毎に
$a_i$の値を表示するprint文を挿入して，
$\sqrt[3]{{c}}$に収束していく様子を表示してみよ.

ただし$n$は小さな値(10とか)で実行すること
(さもないとブラウザの出力がprint文による表示で埋め尽くされてしまう).

これは，計算結果が思うようにでない場合の最も基本的な調査手段．
"""

""" md

__参考:__ 一般に, $f(x) = 0$の解を求めるのに以下のニュートン法が用いられる.

$$ \begin{{array}}{{rcl}} a_0 & = & c, \\ a_{{n+1}} & = & a_n - f(a_n)/f'(a_n) \;\; (n > 0). \end{{array}} $$

これが__収束するならば__, $x = x - f(x)/f'(x)$を満たす$x$,  
すなわち$f(x) = 0$を満たす$x$に収束することは明らか. 
本問はこれを, $f(x) = x^3 - c$に適用したものである.

ただし, 収束するとは限らないので無条件に使えるわけではない.

"""

""" md

# 問題 {C.inc_problem}: 積分

積分
$$ \int_a^b f(x)\,dx $$
の定義は以下のようなものである.

 * 区間$[a,b]$を$n$分割する. つまり$a = x_0 < x_1 < \cdots < x_{{n-1}} < x_n = b$ となるように$x_i$を選ぶ. $x_{{i+1}} - x_i = \Delta x_i$ と書く.
 * そのもとで和
$$\sum_{{i=0}}^{{n-1}} f(x_i) \Delta x_i$$
を作る
 * $|\Delta x_i| \rightarrow 0$のとき上記の和が常に一定値$S$に収束するならば, $f$が$[a,b]$で__積分可能__と言って, $S$を求める積分値と定義する

堅苦しい部分を抜きにすると, 要するに, $[a,b]$を充分細かく分割して, $f(x) \Delta x$の和を作ればそれが($f$が$[a,b]$で積分可能ならば)積分の近似値になっている, ということである.

手計算で積分をするとき, 被積分関数の原子関数(微分すると被積分関数になる関数)を発見的に求める必要があったが, 計算機で近似値を計算するときは, 上記の定義式にそのまましたがって, $[a,b]$内に点を多数とり, 実際に上記の和を計算する. 点を取る際も, もっとも単純に$n$等分するのが普通.

"""
""" md

上記の定義に従い, 積分

$$ \int_a^b \sqrt{{1-x^2}}\,dx $$

の近似値を, $[a,b]$を$n$等分して計算する関数 int_circle(a, b, n) を書け(ただし$0 \leq a \leq b \leq 1$を仮定して良い.

"""

""" write-code-box """

""" answer-code-box """
import math

def int_circle(a, b, n):
    s = 0
    dx = (b - a) / n
    for i in range(n):
        x = a + i * dx
        s += (1-x*x)**0.5 * dx
    return s

""" test-code-box """
assert(abs(int_circle(0, 1, 100000) * 4 - math.pi) < 1.0e-4), int_circle(0, 1, 100000)


""" md

# 問題 {C.inc_problem}: 関数をとる関数

もし前問に引き続き,

$$ \int_a^b \log x\,dx $$

とか

$$ \int_a^b \sqrt{{1+x^3}} x\,dx $$

を求めよと言われたらどうするか?

おそらく, 先程のプログラム int_circle をほんの少しだけ書き換えて, 
被積分関数を計算するところだけを変更することだろう.

そうすると, どうせ変更するのであれば「被積分関数」自身をパラメータとして受け取って, 
どんな被積分関数でも積分できる一つのPython関数を書けないものだろうかと思いたくなる.

実際Pythonでは, それは難なくできる. Python関数はパラメータとして関数を受け取ることが出来, パラメータとして受け取った関数を呼び出すのに何も特別な記法は必要ない. 例えば以下は関数 f とその入力xを受取り, f(f(x)) を計算する関数.

"""

""" exec-code-box """
def app2(f, x):
    return f(f(x))

""" md

このfとして渡すべきものは, 当然Python関数である. 最初から組み込まれた{{\tt math.sin}}, {{\tt math.cos}} などでもよいし, 自分で定義したものでも良い.

"""

""" exec-code-box """
app2(math.sin, 1)

""" exec-code-box """
app2(math.exp, 1)

""" exec-code-box """
def my_fun(x):
    return x ** x

app2(my_fun, 2)


""" md

被積分関数$f$と$a$, $b$が与えられたら,

$$ \int_a^b f(x)\,dx $$

の近似値を, $[a,b]$を$n$等分して計算する関数 integral(f, a, b, n) を書け(ただし$f$は$\leq a \leq x \leq b $で定義されているものと仮定して良い.

"""

""" write-code-box """

""" answer-code-box """
def integral(f, a, b, n):
    s = 0
    dx = (b - a) / n
    for i in range(n):
        x = a + i * dx
        s += f(x) * dx
    return s


""" test-code-box """
assert(abs(integral(math.sin, 0, math.pi/2, 1000000) - 1) < 1.0e-4), integral(math.sin, 0, math.pi/2, 1000000)
assert(abs(integral(math.exp, 0, 1, 1000000) - (math.e - 1)) < 1.0e-4), integral(math.exp, 0, 1, 1000000)

def some_func(x):
    return x * x * x + x * x + x + 1

assert(abs(integral(some_func, 0, 1, 1000000) - 2.083331833333774) < 1.0e-5)
