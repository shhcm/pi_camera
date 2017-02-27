import os

path = '/var/www/camera/camera_pics/'
pic_arch_size = sum(os.path.getsize(path + f) for f in os.listdir(path) if os.path.isfile(path + f))
print('Pic archive size: ' + str(pic_arch_size) + ' bytes.')

if pic_arch_size > 10000000000: # 10 Gig
   os.system('shutdown now -h')
