import os

path='/var/www/camera/camera_pics/'
ctime_file_list = [{'ctime':os.path.getctime(path + f), 'filename':f} for f in os.listdir(path) if os.path.isfile(path + f)]

print(ctime_file_list)
print("SORTED:")
sorted_ctime_file_list = sorted(ctime_file_list, key=lambda ctime_file: ctime_file.get('ctime'))

print(sorted_ctime_file_list)

print("first 20 files")

print(sorted_ctime_file_list[:20])
