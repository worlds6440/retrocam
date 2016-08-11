import RPi.GPIO as GPIO
import picamera
import time
import os

shutter_button = 13
power_button = 19

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

# Configure GPIO pins pullup resistors
GPIO.setup(shutter_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(power_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Start camera
camera = picamera.PiCamera()

# Configure camera
# camera.hflip = True
# camera.vflip = True
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

def shutter_pressed(channel):
    """ Detect shutter button pressed """
    global camera
    # Sleep a very short time to allow shutters to open
    time.sleep(0.8)
    folder = 'images/'
    #time_str =  time.strftime("%d-%m-%Y_%H-%M-%S", time.gmtime())
    time_str =  time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    filename = folder + time_str + '.jpg'
    camera.capture(filename)


def power_off(channel):
    """ Detect power off button """
    os.system("sudo shutdown -h now")


# Configure GPIO Event for power button
GPIO.add_event_detect(shutter_button, GPIO.RISING, callback=shutter_pressed, bouncetime=300)
GPIO.add_event_detect(power_button, GPIO.RISING, callback=power_off, bouncetime=300)

try:
    while True:
        # Do nothing whilst we wait for button events
        time.sleep(0.5)
except:
    print("Handle Errors")
finally:
    GPIO.cleanup()
