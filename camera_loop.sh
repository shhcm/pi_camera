#!/bin/bash


2>&1 

sleep 30 # Allow some time for service startup

while true; do
   sleep 1;
   python3 /home/pi/projects/camera_make_pic.py;
done

#watch -n 3 "python3 /home/pi/projects/camera_make_pic.py"
