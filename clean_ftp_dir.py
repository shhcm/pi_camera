import traceback
#import ftputil
from ftplib import FTP
# Try ftputil instead

ftp_base_dir="/ASMT-2115-01/camera_0/"
max_dirs=7


try:
  ftp = FTP("HOST", "USER", "PASS")
  ftp_del = FTP("HOST", "USER", "PASS") # Instance ftp blocks during LIST operation.
  dir_list=[]

  try:
    ftp.cwd(ftp_base_dir)
    dir_list = sorted(ftp.nlst())
    print("Directories: " + str(dir_list))
    excess_dirs = len(dir_list) - max_dirs

    
    if excess_dirs > 0:
      excess_dir_list = dir_list[0:excess_dirs]
      print("Removing directories" + str(excess_dir_list))
      
      for excess_dir in excess_dir_list:
        
        path=ftp_base_dir + excess_dir
        
        def delete_file(file_listing, path_to_file=path, ftp_inst_del=ftp_del):
#          print("Trying to delete " + file_listing)
#          print("Using ftp " + str(ftp))
          file = path+"/"+file_listing.split()[-1]
          cmd = "DELE " + file
#          print(cmd)
          ftp_inst_del.sendcmd(cmd) 

        ftp.cwd(excess_dir)
        print("Removing files in " + excess_dir)
        ftp.retrlines("LIST", delete_file) # Blocks until callback finished.
        ftp.cwd("..")
        ftp.rmd(excess_dir)
       
  except:
    """ Try again next time. """
    traceback.print_exc()
    ftp.close()
except:
  traceback.print_exc()
