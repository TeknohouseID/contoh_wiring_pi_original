import wiringpi

# One of the following MUST be called before using IO functions:
wiringpi.wiringPiSetup()      # For sequential pin numbering
# OR
#wiringpi.wiringPiSetupSys()   # For /sys/class/gpio with GPIO pin numbering
# OR
#wiringpi.wiringPiSetupGpio()  # For GPIO pin numbering

wiringpi.pinMode(7, 1)       # Set pin 7 wPi to 1 ( OUTPUT )
wiringpi.digitalWrite(7, 1)  # Write 1 ( HIGH ) to pin 7
wiringpi.digitalRead(7)      # Read pin 7
