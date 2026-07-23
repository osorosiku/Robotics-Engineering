from gpiozero import Motor
from signal import pause

motor1 = Motor(forward=18, backward=23)
motor2 = Motor(forward=27, backward=22)
motor3 = Motor(forward=17, backward=24)
motor4 = Motor(forward=25, backward=8)

# モーターを前方向に回転
while True:
    motor1.forward(1)
    motor2.forward(1)
    motor3.forward(1)
    motor4.forward(1)