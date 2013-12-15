import RPi.GPIO as io
io.setmode(io.BCM)
 
in1_pin = 4
in2_pin = 17
pwm_pin= 23
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(pwm_pin, io.OUT)

p=io.PWM(pwm_pin, 500)

p.start(0)
p.ChangeDutyCycle(50)

def changeSpeed(value):
	p.ChangeDutyCycle(value)


#def set(property, value):
#    try:
#        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
#        f.write(value)
#        f.close()	
#    except:
#        print("Error writing to: " + property + " value: " + value)
# 
#set("delayed", "0")
#set("mode", "pwm")
#set("frequency", "500")
#set("active", "1")
 
def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)
 
def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
 
clockwise()

 
try:
	while True:
		
		cmd = raw_input("Command PWM duty cycle")
		dutyCy = int(cmd[0]) * 11
		direction=cmd[1]
		changeSpeed(dutyCy)
		if direction == "f":
			clockwise()
		else: 
			counter_clockwise()

except KeyboardInterrupt:
	pass

p.stop()
io.cleanup()
