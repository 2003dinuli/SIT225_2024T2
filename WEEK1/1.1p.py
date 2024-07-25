import serial
import time
import random

# Set up the serial connection (adjust 'COM3' to your port)
ser = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for the serial connection to initialize

while True:
    # Step 1: Generate a random number and send it to Arduino
    send_number = random.randint(1, 10)
    print(f"{time.ctime()}: Sending number to Arduino: {send_number}")
    ser.write(f"{send_number}\n".encode())

    # Step 2: Wait for Arduino to blink the LED
    time.sleep(1)

    # Step 3: Read the number sent by Arduino
    while ser.in_waiting == 0:
        time.sleep(0.1)
    received_number = int(ser.readline().decode().strip())
    print(f"{time.ctime()}: Received number from Arduino: {received_number}")

    # Step 4: Wait for the specified number of seconds
    print(f"{time.ctime()}: Sleeping for {received_number} seconds")
    time.sleep(received_number)
    print(f"{time.ctime()}: Sleeping done")
