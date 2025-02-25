import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

num = 25100
delay = 2123
result = delayed_sqrt(num, delay)
print(f"Квадратный корень {num} после {delay} миллисекунд: {result}")