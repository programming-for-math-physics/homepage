""" md

#* numpy

* numpy は数値計算を行うのに必要な機能を多数揃えたライブラリ(モジュール)
* 特にnumpyの__配列(array)__を使うとベクトルや行列の計算が色々と簡単にできる
* <a href="https://pmp.eidos.ic.i.u-tokyo.ac.jp/slides/pdf/visual_numpy_matplotlib.pdf" target="_blank">Visual Python, Numpy, Matplotlib スライド</a> 3 NumpyとScipy を参照
* <a href="https://numpy.org/doc/stable/"  target="_blank"> 詳細</a>

* 使うためのおまじない(import文)

"""

""" code w """
import numpy as np
""" """

""" md

もちろん "as np" はなくても良いが, 世の中のnumpyについて説明しているページや本はことごとくこのようにしているのでこの授業でもそれに習う

"""

""" md

# 配列の基本

* 配列は数をいくつでも並べたもの.

<img src="img/array.svg" />

* 以下は 1.0, 1.2, 1.4, 1.6, 1.8, 2.0 6つの数を並べた配列を作る

"""

""" code w """
np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
""" """

""" md

* これを見て「リストと何が違うのだ?」と思ったらその疑問はもっともである. おいおいわかるので読み進めて下さい
* 上記は, 文法として新しいことは何もない. 上の式のうち, `[1.0, 1.2, 1.4, 1.6, 1.8, 2.0]`の部分はすでに習ったリスト式であり, np.array(...) はnpモジュールのarrayという関数を呼び出しているに過ぎない
* まとめるとここで重要なのは配列を作るのに, リストを渡してそれを元に配列を作るのが np.array という関数だということ
* 実際以下のように書いても同じことが起きる

"""

""" code w """
l = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
np.array(l)
""" """

""" md

* for文を使えば大きなリストを自在に作ることが出来た
* それと np.array を組み合わせれば大きな配列を自在に作ることが出来ることがわかるだろう
* 例 (表示しきれなくならないよう, 大きさ(n)は控えめにしてある):

"""

""" code w """
n = 10
l = []
for i in range(n):
    l.append(i * i)
np.array(l)
""" """

""" md

* リストを作るのにリスト内包表記が便利だった
* それを使えば色々な配列もスッキリと作れる
* 以下は上記と同じ配列を1行で作る例

"""

""" code w """
np.array([ i * i for i in range(10) ])
""" """

""" md

* もちろん配列もリスト同様, 一つの値であって, 変数に代入したり他の関数にわたしたりできる

"""

""" code w """
x = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
""" """

""" code w """
x
""" """


""" md

# 配列に関する関数・操作

## リストと同じ操作

* 配列とリストは概念的にも似ており, 出来る操作(要素の取り出しや要素の変更など)も似ている
* そしてPythonでは似た操作は同じ表記(関数名)でできるようにことが多く, その意味でますますリストと配列の区別がつきにくい(わかるまでもう少しの辛抱)


* __配列の要素数 (len)__

* リストと同じくlenでその要素数

"""

""" code w """
len(x)
""" """

""" md

* __配列の要素__ 
* $x$[$i$] で配列$x$の$i$番目の要素(0番目から始まる)を取り出せる

"""

""" code w """
x[0]
""" """

""" code w """
x[1]
""" """

""" md 

要素数$n$として$n$以上の数を添え字に指定すると(当然)エラーになる

"""

""" code w """
# error
x[6]
""" """

""" md 

* 一旦作った配列の要素をあとから変更することも出来る 
* 普通に代入文で代入すれば良い

"""

""" code w """
x[1] = 20.0
""" """

""" code w """
x
""" """

""" md 

* 配列を受け取る関数などももちろん書ける
* 以下は配列を受取り, その要素の和を返す関数 sum_of_array

"""

""" code w """
def sum_of_array(a):
    n = len(a)
    s = 0
    for i in range(n):
        s = s + a[i]
    return s

sum_of_array(x)
""" """

""" md

* 実はそんなのは自分で書かなくても最初から備わっている

"""

""" code w """
x.sum()
""" """

""" md

## 配列ならではの操作

* 配列ならではの操作, またはリストと同じ記法でも異なる動作をする操作を述べる

"""

""" md 

* 「配列 + 配列」
は対応する要素を加算してできた値を要素とする新しい配列

"""

""" code w """
x = np.array([1,2,3,4])
y = np.array([0.1, 0.1, 0.1, 0.1])

x + y
""" """

""" md 

* 「配列 * 数」
* 「数 * 配列」
は各要素を「数」倍した新しい配列

"""

""" code w """
x * 4
""" """

""" code w """
4 * x
""" """

""" md 

* 「配列 * 配列」
は対応する要素毎に掛け算をした新しい配列

"""

""" code w """
x * y
""" """

""" md 

* numpy に備わっているsin, exp, logなどの関数は, 配列に対しても適用でき, それは配列の各要素にそれぞれの関数をかけた配列という意味になる

"""

""" code w """
np.sin(x)
""" """

""" code w """
np.log(x)
""" """

""" md 

* 配列のパワーの源はこれらの, 「配列に対して一見普通の式を書くだけで全要素に対する計算をしてくれる」ことだと言ってよい
* もし np.log(x) と同じことをこれなしで(自分で)やれと言われたら, きっと以下のような関数を自分で書くことになる(新しい配列を作り, xの各要素x[i]のlogを計算)

"""

""" code w """
import math

def np_log(x):
    n = len(x)
    y = np.zeros(n)
    for i in range(n):
        y[i] = math.log(x[i])
    return y

np_log(x)
""" """

""" md 

* リストに出来て配列にできないこともある
* その代表は, 「後から大きさを変更すること」
* リストには append でそれができたが, 配列は出来ない
* 配列の大きさは「生まれた瞬間に決まる」

"""

""" code w """
# error
l = [1,2,3]
l.append(4)
a = np.array([1,2,3])
a.append(4)
""" """

""" md 

ここまでのまとめ

```
import numpy as np
```

* `np.array(リスト)` で配列を作る
* `x[i]` で要素の参照
* `x[i] = 式` で要素の更新
* x * y, x + y, k * x などで各要素ごとに掛け算, 足し算など
* np.sin(x), np.log(x), などで各要素に関数を適用して新しい配列を返す
* 配列の大きさは後から変更できない

"""

""" md

# 配列の作り方色々

* 小さな配列なら np.array([1.0, 1.2, ... ]) のように全要素をプログラム内で並べて作ることもできる
* 大きな配列(100要素以上)を作る場合, まずそのリストをfor文やリスト内包表記で作ればよいのだが, 直接大きな配列を作る方法も色々ある

"""

""" md 

#* zeros(n)

* 0がn個並んだ配列

"""

""" code w """
n = 20
np.zeros(n)
""" """

""" md 

#* ones(n)

* 1がn個並んだ配列

"""

""" code w """
np.ones(n)
""" """

""" md 

#* linspace(a,b,n)

* aからbまで要素数nの等差数列
* 要素が (b-a)/(n-1) の間隔で並ぶことになる
* linspace (linear spaceの略? 線型空間?) という, どうにも覚えにくい名前は, きっと, 「スペース(間隔)が線形にならんでいる」ということなのだろう. 個人的には「スペースが一定」なのだから constspace とでも言うべきじゃないかと思うが

"""

""" code w """
np.linspace(0.2, 4.0, n)
""" """

""" md 

#* arange(a, b, d)

* aからb未満まで間隔dの等差数列
* 要素数は(b - a)/d くらいになるが, 半端が出る場合に誤差ギリギリのところで$\pm 1$する可能性があるので決めつけると危険

"""

""" code w """
np.arange(3.5, 4.0, 0.1)
""" """

""" md 

#* random.random(n)

* n個の乱数の配列

"""

""" code w """
np.random.random(n)
""" """

""" md

# 部分配列(スライス)記法

* 配列の1要素を取り出すのに添字記法($x[i]$)が使えるが似た記法で「複数の要素」を取り出すことが出来る
 * $x[i:j]$ で $x[i], x[i+1], ..., x[j-1]$を同時に取り出せる
* 複数の要素なので結果もまた配列になる
* 複数の要素を同時に更新することも出来る
 * $x[i:j] = ...$ で$x[i], x[i+1], ..., x[j-1]$を同時に更新できる
 * 右辺は同じ要素数の配列(実はリストでも良い)か, 1つの数の場合は全ての要素を同じ値で更新するという意味になる

* $i$:$j$ という式のことを「スライス」と呼ぶ

"""

""" code w """
x = np.linspace(0, 1, 11)
x
""" """

""" md 

* $x[i:j]$ で $i$番目から$j$の一つ手前まで ($(j-i)$要素)

"""

""" code w """
x[1:4]
""" """

""" md

* 左側を省略すると0 (先頭から)の意味
* つまり x[:j] は「最初の$j$要素」

"""

""" code w """
x[:3]
""" """

""" md

* 右側を省略すると要素数 (終わりまで)の意味
* つまり x[i:] は「$i$番目およびそれ以降の要素」

"""

""" code w """
x[3:]
""" """

""" md

* 当然, 両方を省略すると配列まるごとという意味になる

"""

""" code w """
x[:]
""" """

""" md 

* 更新

"""

""" code w """
x[1:4] = 100 * x[1:4]
x
""" """

""" md 

* 右辺はリストでもOK

"""

""" code w """
x[1:4] = [ -10, -20, -30 ]
x
""" """

""" md 

* 左辺と右辺の要素数があわないとエラーになるので注意

"""

""" code """
# error
x[1:4] = 10 * x[2:6]
""" """

""" md 

* 右辺が1つの数の場合, 左辺の全要素をそれで更新という意味になる

"""

""" code w """
x[1:4] = 100
x
""" """


""" md

# 2次元配列, 3次元配列, 多次元配列

* これまで扱ってきた配列は1次元の配列
* 実は任意次元の配列を作ることが出来る
* 例えば1次元配列はある時点における棒の温度分布とか, 糸の上を伝わる波の振幅を表すのに使える. またある一つの数の時系列を全て記録するのにも使える
* ある平面上の温度分布, 平面を伝わる波, 糸の上を伝わる波の時系列を全て記録するには2次元の配列が必要になることが想像できるだろう
* 1次元配列にまつわる関数名や記法を覚えれば, 2次元以上の配列でどうすればよいかは容易に想像がつく

"""

""" md

## 多次元配列を作る

"""

""" md 

#* np.array(リストのリスト)

"""

""" code w """
np.array([ [1,2,3], [4,5,6] ])
""" """

""" md 

* 上記の`[ [1,2,3], [4,5,6] ]`は「リストのリスト」
* リストの要素は何でも良いのだからこういうことが書けても当然

"""


""" md 

#* zeros

* 全部0

"""

""" md

* 0が 2x3 並んだ2次元の配列
"""

""" code w """
np.zeros((2,3))
""" """

""" md

* 0が 2x3x4 並んだ3次元の配列
"""

""" code w """
np.zeros((2,3,4))
""" """


""" md 

#* ones 

* 全部1

"""

""" code w """
np.ones((2,3))
""" """

""" code w """
np.ones((2,3,4))
""" """

""" md 

#* random

* 乱数

"""

""" code w """
np.random.random((2,3))
""" """

""" md 

#* reshape

* 配列の形を変形
* 例えば 3x4 の配列を 4x3 にしたり 2x2x3 にしたり, 合計要素数が変わらない範囲で, 変形が可能
* 一旦1次元の配列を作ってからそれを2次元に変形するというのは多次元配列を作ると気に割とよく使うパターン

"""

""" code w """
np.arange(0, 15, 1).reshape((3,5))
""" """

""" md 

* reshapeは一般に, 任意の配列を, それと同数の要素数を持つ任意の次元の配列に変形することが出来る

"""

""" code w """
np.array([ [1,2,3], [4,5,6] ]).reshape((3,2))
""" """

""" md

## 多次元配列の len と shape

"""

""" md

* もちろん多次元配列に対しても len という関数が使えるが, それが返すのは, 「最初の軸に沿った要素数」であり, 全ての要素数ではないので注意

"""

""" code w """
a = np.zeros((5,8))  # 5x8 の配列
len(a)               # (40ではなく) 5
""" """

""" md

* 全要素数は a.size
* 各軸の要素数は a.shape

"""

""" code w """
a.size
""" """

""" code w """
a.shape
""" """

""" md 

* なおここで返された (2,3) という値は, 説明を省略した「タプル」というものなのだが, さしあたり以下のようにして各要素を取り出せることだけを覚えておけば事足りる

"""

""" code w """
m,n = a.shape
""" """

""" code w """
m
""" """

""" code w """
n
""" """

""" md

## 要素とスライス

"""

""" md

* 2次元配列であれば$x[i,j]$, 3次元配列であれば$x[i,j,k]$のように, 添字を複数指定することで1要素を取り出せる
* ある添字を1つの数ではなくスライスにすれば, ある範囲の要素を取り出すことが出来る. 要するに任意の矩形を切り取ることが出来る
* 要素や範囲の更新を行うことが出来るのも, 改めて説明の必要はないくらいだろう

"""

""" code w """
a = np.arange(0, 40, 1).reshape((5,8))
a
""" """

""" md 

* 1要素の取り出し. 当然ながら2次元配列であれば2つの添字, 3次元配列であれば3つの添字で一要素を指定する

"""

""" code w """
a[1,2]
""" """

""" md 

* 矩形の取り出し. それぞれの添字をスライスにすれば矩形を取り出すことが出来る

"""

""" code w """
a[2:4,3:6]
""" """

""" md 

* とくに2つめの軸のスライスを : にすれば行まるごとということになるし, 1つめを : にすれば列まるごとということになる

"""

""" code w """
a[2,:]
""" """

""" code w """
a[:,2]
""" """

""" md 

* 2次元配列にも sum が使える

"""

""" code w """
a.sum()
""" """

""" md 

* axis= という引数を渡すことで, どちらの軸に沿って和を取るかを指定できる
* a.sum(axis=0) は最初の軸に沿って和を取る --- a[0,j] + ... + a[4,j] を各jに対して計算する --- ということになる

"""

""" code w """
a.sum(axis=0)
""" """

""" code w """
a.sum(axis=1)
""" """
