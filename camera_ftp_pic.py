import time
from picamera import PiCamera
from time import sleep
from io import BytesIO
from ftplib import FTP
from datetime import datetime
from threading import Thread

def camera_worker():
  camera = PiCamera()
  while True:
    f = BytesIO()
    camera.start_preview()
    sleep(4)
    camera.capture(f, 'jpeg')
    f.seek(0) # Go back to pos 0 of buffer. 
    timestamp = datetime.fromtimestamp(time.time()).strftime('%y%m%d_%H%M%S')
    
    try: 
       ftp = FTP("FTP_HOST", "FTP_USER", "FTP_PASSWORD")
       ftp.storbinary("STOR /PATH/TO/IMAGES/" + timestamp + ".jpg", f)
       ftp.close()
    except:
       print("FTP failed:\nType: " + sys.exc_info()[0]
             + "\nValue: " + sys.exc_info()[1]
             + "\nTraceback " + sys.exc_info()[2])
    finally:
       f.close()
       camera.stop_preview()

thread = Thread(name="Camera Thread", target=camera_worker)
thread.start()

