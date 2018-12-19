import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly

#GPIO.setup(3, GPIO.OUT)
#GPIO.setup(5, GPIO.OUT)
#GPIO.setup(8, GPIO.OUT)
#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
try:
    # Main loop
    while True:
        #print rc_time(pin_to_circuit)
        
        with open ('lightData', 'rb') as fp:
            lightList = pickle.load(fp)
        
        if(rc_time(pin_to_circuit) >= 100000):
                if(lightList[0]==1):
                    GPIO.output(3, GPIO.HIGH)
                if(lightList[1]==1):
                    GPIO.output(5, GPIO.HIGH)
                if(lightList[2]==1):
                    GPIO.output(8, GPIO.HIGH)
                if(lightList[3]==1):
                    GPIO.output(11, GPIO.HIGH)
                if(lightList[4]==1):
                    GPIO.output(13, GPIO.HIGH)
        else:
                if(lightList[0]==0):
                    GPIO.output(3, GPIO.LOW)
                if(lightList[1]==0):
                    GPIO.output(5, GPIO.LOW)
                if(lightList[2]==0):
                    GPIO.output(8, GPIO.LOW)
                if(lightList[3]==0):
                    GPIO.output(11, GPIO.LOW)
                if(lightList[4]==0):
                    GPIO.output(13, GPIO.LOW)
                
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()