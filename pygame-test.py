import pygame
import sys
from gpiozero import Motor
from signal import pause

# Pygameの初期化
pygame.init()

# ゲームウィンドウのサイズ
width, height = 800, 600

# ボールの初期位置と速度
ball_x, ball_y = width // 2, height // 2
ball_speed = 5

# ボールのサイズ
ball_size = 20

# ゲームウィンドウの作成
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball Game")

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

   # Bボタンでボールが縮小
   if B_button:
       ball_size -= 0.5

   # 画面外に出ないように制御
   ball_x = max(0, min(ball_x, width))
   ball_y = max(0, min(ball_y, height))

   ball_size = max(min(ball_size, 30.0) ,10.0)

   # 描画処理
   screen.fill((255, 255, 255))  # ゲームウィンドウを白で塗りつぶす
   pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_size)  # 青いボールを描画

   # 画面更新
   pygame.display.flip()

   # フレームレートの制御
   pygame.time.Clock().tick(60)