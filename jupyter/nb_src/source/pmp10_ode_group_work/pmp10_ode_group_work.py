""" md

#* 物理シミュレーション + アニメーション のグループワーク

"""

""" md 

#*P 課題

pmp09やスライドを参考にしながら, グループ共同で以下を行え

* 以下のスペックを満たす問題をひとつ, グループで設定する
* それをシミュレートして, アニメーションする
* 問題のスペック(以下を満たす問題を自分たちで設定)
  * 物体(質点)が2個以上登場する(まずは2個で良い)
  * 物体に「なんらかの力」が働く. 好きに設定する. 物理法則に忠実かどうかは自由
    * 物体間の引力? 斥力? 距離との関係
    * 重力
    * 衝突
    * 抵抗(速度に比例, 速度の2乗に比例? ご自由に?)
    * どこかからバネのようなもので引かれている? 磁石みたいなもの?
    * ランダムな力
    * 要するに何でも良い
    * etc.
* ルール: グループで作業をすること. そのために,
  * 誰がコードを書くかを決める(必ず一人に決める. pmp09とかが完成している人は遠慮する :-)
  * その人の画面を共有する
  * 残りの人はそれに, 手出しではなく, 口出しをする
  * 途中でバトンタッチしても良い(コピペしたければ他の人のシートにアクセスするのがよいでしょう. パスワードは一時的にいつものシートに復活させておきました)
  * 今日の趣旨はあくまでアニメーションまでやってみること. 問題設定に時間をかける必要はない. 5-10分で決めて始めてください
  * 授業のラスト30分に出来たものを見せられるようにする

* 以下も参考に
  * 授業HPの 微分方程式スライド
  * 授業HPの Visual Python, Numpy, Matplotlib スライド


"""

""" code """

""" """

""" code """
# VPythonが動くかどうかのチェック用.
# アニメーションがうまく出なかったら, Kernel -> Restart and Clear Output をしてからこのセルを実行してみてください
# それでダメなら連絡ください

from vpython import *
sphere()

""" """
