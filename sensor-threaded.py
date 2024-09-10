#!/usr/bin/python3
import time
from gpiozero import DistanceSensor, RGBLED, Buzzer
from threading import Thread
from signal import pause, signal, SIGTERM, SIGHUP

# Define GPIO pins for the sensor, RGB LED, and buzzer
TRIG_PIN = 21
ECHO_PIN = 20
LED_RED_PIN = 24
LED_GREEN_PIN = 17
LED_BLUE_PIN = 23
BUZZER_PIN = 25

# Setup sensor, RGB LED, and buzzer
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN)
rgb_led = RGBLED(LED_RED_PIN, LED_GREEN_PIN, LED_BLUE_PIN)
buzzer = Buzzer(BUZZER_PIN)

# Define distance thresholds
DISTANCE_FAR = 20.0
DISTANCE_MEDIUM = 5.0
active = True

def safe_exit(signum, frame):
    global active
    active = False
    rgb_led.off()
    buzzer.off()
    exit(1)

def read_sensor():
    while active:
        distance = sensor.distance * 100  # Convert to centimeters
        print(f"Distance: {distance:.2f} cm")

        if distance >= DISTANCE_FAR:
            rgb_led.color = (0, 1, 0)  # Green
            buzzer.off()
        elif distance >= DISTANCE_MEDIUM:
            rgb_led.color = (1, 1, 0)  # Yellow
            buzzer.beep(on_time=0.05, off_time=0.05, n=1, background=True)  # Short beep
        else:
            rgb_led.color = (1, 0, 0)  # Red
            buzzer.on()

        time.sleep(0.1)  # Slow down the sensor polling loop

try:
    # Handle termination signals for safe exit
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    # Start the sensor reading thread
    sensor_thread = Thread(target=read_sensor)
    sensor_thread.start()

    # Wait for signals or interruptions
    pause()

except KeyboardInterrupt:
    pass

finally:
    # Ensure proper cleanup on exit
    active = False
    sensor_thread.join()
    rgb_led.off()
    buzzer.off()
