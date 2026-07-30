import pygame
import sys
from gpiozero import Motor
from signal import pause

# Pygameの初期化
pygame.init()

# ジョイスティックの初期化
pygame.joystick.init()

# 利用可能なジョイスティックの数を取得
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
   print("ジョイスティックが見つかりません。")
   sys.exit()

# 0番のジョイスティックを取得
joystick = pygame.joystick.Joystick(0)
joystick.init()


# ゲームループ
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
   
   # 左スティックの入力を取得
   ball_x += joystick.get_axis(0)
   ball_y += joystick.get_axis(1)

   # 右スティックの入力を取得
   ball_x += joystick.get_axis(2)
   ball_y += joystick.get_axis(3)

   # ボタンの入力を取得
   A_button = joystick.get_button(0) # Aボタン
   B_button = joystick.get_button(1) # Bボタン

   # Aボタンでボールが拡大
   if A_button:
       ball_size += 0.5
       print("Aボタンが押されました。ボールのサイズを拡大します。")
