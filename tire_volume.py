import math
from datetime import datetime
current_date_and_time = datetime.now()
print(f'{current_date_and_time:%y-%m-%d}')
w = float(input('Enter the width of the tire in mm (ex. 205): '))
a = float(input('Enter the aspect ratio of the tire (ex 60): '))
d = float(input('Enter the diameter of the wheel in inches (ex 15): '))
def tire_volume(w, a, d):
    return (math.pi * w**2 * a) * (w * a + (2540 * d)) /10000000000
v = tire_volume(w, a, d)
print(f'The approximate volume is {v:.2f} liters')
f = open("volumes.txt","a")
f.write(f"{current_date_and_time:%y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n")
f.close()