import sys
import cv2
import pygame
import numpy as np
from ultralytics import YOLO
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

# モーターの定義
motor1 = Motor(forward=18, backward=23)
motor2 = Motor(forward=17, backward=24)
motor3 = Motor(forward=20, backward=21)
motor4 = Motor(forward=27, backward=22)

#モーター制御
def forward():
   motor1.forward(1)
   motor2.forward(1)
   motor3.forward(1)
   motor4.forward(1)

def backward():
   motor1.backward(1)
   motor2.backward(1)
   motor3.backward(1)
   motor4.backward(1)

def left():
   motor1.forward(1)
   motor2.backward(1)
   motor3.forward(1)
   motor4.backward(1)

def right():
   motor1.backward(1)
   motor2.forward(1)
   motor3.backward(1)
   motor4.forward(1)

def left_forward():
   motor1.forward(1)
   motor2.stop()
   motor3.forward(1)
   motor4.stop()

def right_forward():
   motor1.stop()
   motor2.forward(1)
   motor3.stop()
   motor4.forward(1)

def left_backward():
   motor1.backward(1)
   motor2.stop()
   motor3.backward(1)
   motor4.stop()

def right_backward():
   motor1.stop()
   motor2.backward(1)
   motor3.stop()
   motor4.backward(1)

def stop():
   motor1.stop()
   motor2.stop()
   motor3.stop()
   motor4.stop()

# ループ周期調整用のクロック(負荷対策であった方が良いらしい)
clock = pygame.time.Clock()

# motorへの入力確認
while True:
   
   # 入力確認
   pygame.event.pump()
   
   around = joystick.get_axis(1)
   turn = joystick.get_axis(0)

   # 入力によっての動作管理
   if around <= -0.2 and turn <= -0.2:
      left_forward()
   elif around <= -0.2 and turn >= 0.2:
      right_forward()
   elif around >= 0.2 and turn <= -0.2:
      left_backward()
   elif around >= 0.2 and turn >= 0.2:
      right_backward()
   elif around <= -0.5:
      forward()
   elif around >= 0.5:
      backward()
   elif turn <= -0.5:
      left()
   elif turn >= 0.5:
      right()  
   else:
      stop()
   # CPU使用率を抑えるために短い待機を入れる(負荷対策であった方が良いらしい)
   clock.tick(30)
