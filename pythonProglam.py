# coding: utf-8
# 値段を計算するプログラム
# import random
# apple_price = 350 #リンゴの単価
# apple_num = random.randint(1,10)  #リンゴの個数
# print("apple`s price:" + str(apple_price) + " yen")
# print("apple`s piece:" + str(apple_num) + " pieces")
# total = apple_price * apple_num
# print("totalprice:" + str(total) + " yen")

# if文
# number = 2
# if number == 1:
#     print("yes!!")
# else:
#     print("no!")

#elifを使用したif文
# number = 2
# if number == 1:
#     print("Yes!!")
# elif number ==  2:  #elifはいくらでも追加できる
#     print("even")
# else:
#     print("no!!")

# #for文
# for i in range(10):
#     print("hello world!!")

# for i in range(5):      #1,10　etc…で数値を指定できる
#     print("hello world!!" + str(i))

# while文
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 1
# while i <= 5:
#     i = i + 1
#     print("hello testmessage")

# whileじゅん繰り下げ
# i = 10  #カウンタ変数を初期化
# while i >=1:
#     print(i)    #繰り返し処理
#     i -= 1      #カウンタ変数を更新

# ループ処理での一例
# import random   #randam関数を使用
# hp = 30         #変数の宣言
# while hp > 0:   #変数が0になるまで指定
#     hit = random.randint(1,10)  #ランダムな戻り値の定義
#     print("slime`s " +str(hit) + " damege") #一つ目の繰り返し処理
#     hp -= hit   #変数が戻り値の数値になるまで繰り返し処理
# print("slime fell down!")   #二つ目の繰り返し処理

#  年齢入力のプルダウン作成
# coding: utf-8
# print("<select name=\'age\'>")
# for age in range(100):
#     print("<option>" + str(age + 1) +"</option>")
# print("</select>")

#標準入力とループ処理
# count = int(input())      #入力画面には数値を入れる
# for i in range(count):
#     print("test message")

#paiza演習2より     https://paiza.jp/works/python3/primer/beginner-python3/4025/2
# coding: utf-8
#標準入力とループ処理
# count1 = int(input())               #１行目の数値を読み込む
# count2 = int(input())               #２行目の数値を読み込む
# for i in range(count1,count2+1):    #２行目の数値はそのままでは＞＝にならないので+1して含める
#     print(i)                        #ループ処理で定義したカウンタ変数を出力

# coding: utf-8
# 西暦年と平成年の対応表を作る
# 1989年から2016年までをループで出力
# ループ内で、各西暦年を平成年に変換
# for seireki in range(1989,2019):
#     print("西暦" + str(seireki) + "年は ", end = "")
#     heisei = seireki - 1988
#     print("平成" + str(heisei) + "年です")

# coding: utf-8
# 特定期間の西暦年と昭和年の対応表を作る
# 1行目：開始年
# 2行目：期間
# 昭和年 = 西暦年 - 1925
# 出力：西暦XXXX年は昭和YY年です
# start = int(input())
# period = int(input())

# for seireki in range(start,start + period):
#     print("西暦" + str(seireki) + "年は", end="")
#     syouwa = seireki - 1925
#     print("昭和" + str(syouwa) + "年です")

#リストの例

# coding: utf-8
# リストを作成する

player_1 = "戦士"          #変数の具体例
player_2 = "魔法使い"      #変数の具体例

print(player_1)            #変数を出力
print(player_2)

team = ["勇者","魔法使い",100,player_1]     #リストの具体例
print(team)                                #リストを出力