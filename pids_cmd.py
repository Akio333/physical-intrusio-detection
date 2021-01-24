
import os
#os.system('conda init zsh')
#os.system('conda activate yolov3-tf2-gpu')
ch = int(input(
    "Select Detection Method : \n 1] Detect \n 2] Register Face "))

if (ch == 1):
    os.chdir('./person-yolov3/')
    os.system(
        'python detect_video.py --video 0 --weights checkpoints/yolov3_5.tf')
    os.chdir('./facerec/')
    os.system('python main.py')
elif (ch == 2):
    os.chdir('./facerec/')
    os.system('python main.py --mode="input"')
else:
    print("Please Enter Correct Choice...")
