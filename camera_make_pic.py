import time

from picamera import PiCamera
from datetime import datetime

camera = PiCamera()

camera.start_preview()
time.sleep(4)
timestamp = datetime.fromtimestamp(time.time()).strftime('%y%m%d_%H%M%S')
camera.capture('/var/www/camera/camera_pics/im_' + timestamp + '.jpg')
camera.stop_preview()

