import RPi.GPIO as io
io.setmode(io.BCM)
 
in1_pin = 4
in2_pin = 17
pwm_pin= 23
in3_pin = 24
in4_pin = 25
pwm2_pin = 22
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(pwm_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(pwm2_pin, io.OUT)
p=io.PWM(pwm_pin, 500)
q=io.PWM(pwm2_pin, 500)


p.start(0)
p.ChangeDutyCycle(50)
q.start(0)
q.ChangeDutyCycle(50)

def changeSpeed(value1, value2 ):
	p.ChangeDutyCycle(value1)
	q.ChangeDutyCycle(value2)


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

def orario():
	io.output(in3_pin,True)
	io.output(in4_pin,False)
	
def antiorario():
	io.output(in3_pin,False)
	io.output(in4_pin,True)
	
clockwise()
orario()

 
try:
	while True:
		
		cmd = raw_input("Command PWM duty cycle")
		dutyCy1 = int(cmd[0]) * 11
		dutyCy2 = int(cmd[1]) * 11
		direction=cmd[2]
		direction2=cmd[3]
		changeSpeed(dutyCy1,dutyCy2)
		if direction == "f":
			clockwise()
		else: 
			counter_clockwise()
		if direction2 == "f":
			orario()
		else:
			antiorario()

except KeyboardInterrupt:
	pass

p.stop()
io.cleanup()
