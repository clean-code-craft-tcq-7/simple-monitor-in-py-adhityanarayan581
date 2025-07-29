from time import sleep
import sys

def blink_warning():
  for _ in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    print('Temperature critical!')
    blink_warning()
    return False
  elif pulseRate < 60 or pulseRate > 100:
    print('Pulse Rate is out of range!')
    blink_warning()
    return False
  elif spo2 < 90:
    print('Oxygen Saturation out of range!')
    blink_warning()
    return False
  return True
