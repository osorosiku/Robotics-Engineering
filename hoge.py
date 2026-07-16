from gpiozero import Motor
from signal import pause

# input1（GPIO17）にプラス、input2（GPIO18）にマイナスを流す
motor = Motor(forward=17, backward=18)

# モーターを後進方向に回転
while True:
    motor.forward(1)
  
