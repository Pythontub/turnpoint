# coding: utf-8
# 値段を計算するプログラム
import random
apple_price = 350 #リンゴの単価
apple_num = random.randint(1,10)  #リンゴの個数
print("apple`s price:" + str(apple_price) + " yen")
print("apple`s piece:" + str(apple_num) + " pieces")
total = apple_price * apple_num
print("totalprice:" + str(total) + " yen")