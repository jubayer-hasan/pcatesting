import numpy as np
import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setmode(GPIO.BCM) 
from PIL import Image
import scipy.misc as ms
import os
import glob
import urllib
import requests
import os
import time
import datetime
import PIL
from PIL import Image
yellowLed = 17
yellowLed1 = 27 
blinkTimes = [0,1,2,3,4] 
imageread=[]
mean=[]
originalimage=[]
originalimage1=[]
weight=[]
inputimage=[]
image_vector=[]
input_show=[]
covarience=[]
eigenvector=[]
eigenvalue=[]
originaleigenvector=[]
temp=[]
inputweight=[]
classes =[]
counter=0
totalaccuracy =[]
recall_A=[]
recall_B=[]
recall_C=[]
recall_Five=[]
recall_Point=[]
recall_V=[]
precision_A=[]
precision_B=[]
precision_C=[]
precision_Five=[]
precision_Point=[]
precision_V=[]
considereigenvector=[]
sumofeigenvalue=[]
c=0
#%%
image_url= 'http://192.168.43.188:8080/photo.jpg'
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
path='\Pictures'
basewidth = 100
img = Image.open('image_name.jpg')
hsize = 100
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
dt = str(datetime.datetime.now())
img.save('check/image.jpg') 
print (time.strftime("%H:%M:%S"))
print (time.strftime("%d/%m/%Y"))
img_dimension=28
for image1 in glob.glob('check/*.jpg'):
    img1 = np.array(Image.open(image1).convert('L'))
    img1 = ms.imresize(img1, (100, 100), 'nearest')
    im_array1 = np.array(img1)
    originalimage1.append(im_array1.flatten())
originalimage1=np.array(originalimage1)
mean=np.load('mean10.npy')
mean=np.asarray(mean)     
imageread1=[]
imageread1=np.asarray(originalimage1)
imageread1=imageread1-mean
originaleigenvector=np.load('oev10.npy')
originaleigenvector=np.asarray(originaleigenvector)

classes=np.load('classes10.npy')
classes.tolist()
weight=np.load('tst10.npy')
weight=np.asarray(weight)
for i in range(len(imageread1)) :
   temp=[]
   for j in  range(len(originaleigenvector)):
            value=np.dot(originaleigenvector[j],imageread1[i].T)
            temp.append(value)
   inputweight.append(temp)
inputweight=np.asarray(inputweight)
maxwgt=999999999999999.9999999999
flag=0
distance=[]
idx=[]
idx.append([])
for i in range(len(weight)) :
            value=np.linalg.norm(weight[i]-inputweight[0])
            distance.append(value)
            if maxwgt>=abs(value) and abs(value)<=99999999.999999 :
                flag=1
                ans=classes[i]
                maxwgt=abs(value)
                print(ans,' ',maxwgt,' ',i)
distance=np.asarray(distance)
if flag==1 :
    print(maxwgt,' ',ans)
    if ans==0:
        GPIO.setup(yellowLed, GPIO.OUT) 
        for i in blinkTimes: 
    	    GPIO.output(yellowLed, True)
    	    sleep(1)
    	    GPIO.output(yellowLed, False)
    	    sleep(1)
        GPIO.cleanup() 
    if ans==1:
        GPIO.setup(yellowLed1, GPIO.OUT) 
        for i in blinkTimes: 
    	    GPIO.output(yellowLed1, True)
    	    sleep(1)
    	    GPIO.output(yellowLed1, False)
    	    sleep(1)
        GPIO.cleanup() 
if flag==0 :
    print('Error occured!!!Try again')
