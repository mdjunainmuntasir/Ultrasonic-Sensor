# Ultrasonic-Sensor
https://www.youtube.com/@MDJUNAINMUNTASIR 
Display the sensor reading in centimetres in terminal, 10 times a second. Use an f-string to format
the terminal output to 2 decimal points.
3. Declare the LEDs in the program. You can use regular LEDs (controlled by gpiozero) for basic lab
credit, or use a RGB LED (controlled by gpiozero RGBLED class), instead of three LEDs for higher lab
credit.
Please have a look at the gpiozero API for RGBLED class details: https://tinyurl.com/2254784b
4. Use one if-elif-else structure to handle the LED/RGBLED functionality without using compound
logical statements (and/or keywords). Consider the following pseudo-code:
read_sensor function (run as a thread):
while sensor is active:
read distance
if distance is long:
activate green LED, deactivate yellow and red LEDs
turn off buzzer
else distance is medium:
activate yellow LED, deactivate green and red LEDs
beep buzzer once (bonus: if buzzer not muted)
else:
activate red LED, deactivate green and yellow LEDs
turn on buzzer 
