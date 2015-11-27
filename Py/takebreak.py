#This program play a video on the internet every 2 hours, for 3 times.
#Udacity "Programming Foundations with Python" first project
#By xiaozhenliu@github On 2015-11-27

import time
import webbrowser

for i in range(3):
    time.sleep(2*60*60)
    webbrowser.open("http://v.qq.com/cover/a/alfc02ro10bbv8b.html?vid=l0010qr0bOQ")
