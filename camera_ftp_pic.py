
import time
import traceback 
from picamera import PiCamera
from time import sleep
from io import BytesIO
from ftplib import FTP
from datetime import datetime
from threading import Thread

ftp_base_dir="/ASMT-2115-01/camera_0/"

def camera_worker():
  camera = PiCamera()
  while True:
    f = BytesIO()
    camera.start_preview()
    sleep(1)
    camera.capture(f, 'jpeg')
    f.seek(0) # Go back to pos 0 of buffer. 
    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    working_dir = datetime.fromtimestamp(time.time()).strftime('%Y%m%d')
    
    try:
       ftp = FTP("SERVER.NAME", "USER", "PASS")
       try: 
          ftp.cwd(ftp_base_dir + working_dir)
       except:
          """ Try to create directory. """
          try:
             ftp.mkd(ftp_base_dir + working_dir)
          except:
             """ Try again. """ 

       sleep(1)

       try:
          ftp.storbinary("STOR " + ftp_base_dir + working_dir + "/" + timestamp + ".jpg", f)
       except:
          traceback.print_exc()
       finally:
          f.close()
          camera.stop_preview()
    except:
       """ Try again. """
    finally:
       ftp.close()

thread = Thread(name="Camera Thread", target=camera_worker)
thread.start()
