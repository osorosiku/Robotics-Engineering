from gpiozero import Motor
from signal import pause

motor1 = Motor(forward=18, backward=23)
motor2 = Motor(forward=17, backward=24)
motor3 = Motor(forward=20, backward=21)
motor4 = Motor(forward=27, backward=22)

# モーターを前進方向に回転
while True:
    motor1.forward(1)
    motor2.forward(1)
    motor3.forward(1)
    motor4.forward(1)
