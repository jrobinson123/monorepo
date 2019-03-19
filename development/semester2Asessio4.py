
from PIL import Image
import cv2
import numpy as np
import imutils



sampleImage = Image.open("sampleJonah.jpg")
#sampleImage = imutils.resize(sampleImage,width=360)

px = sampleImage.load()
#sampleImage = cv2.resize(px,width=360)


shape = np.shape(sampleImage)

height = shape[0]
width = shape[1]
channels = shape[2]
arr = [[x,y] for x in range(width) for y in range(height) ]

mask = Image.new(mode="1",size=(width,height),color=0)
pmask = mask.load()

for x in range(width):
   for y in range(height):
       weightedValue = int(px[x,y][0]*.299+px[x,y][1]*.587+px[x,y][2]*.114)/3
       px[x,y] =(int(weightedValue),int(weightedValue),int(weightedValue))

#sampleImage.show()

for x in range(width):
   for y in range(height):
       #weightedValue = int(px[x,y][0]+px[x,y][1]+px[x,y][2])/3
       if(x>1 and x<width-1 and y>1 and y<height-1):
          # blurAverage = (px[x+1,y][0]+px[x-1,y][0]+px[x,y+1][0]+px[x,y-1][0])/4
          # firstDifference = abs((px[x,y][0]+px[x+1,y][0])/2)
          # secondDifference = abs((px[x,y][0]+px[x-1,y][0])/2)
          # thirdDifference = abs((px[x,y][0]+px[x,y+1][0])/2)
          # forthDifference = abs((px[x,y][0]+px[x,y-1][0])/2)
          firstDifference = abs((px[x,y][0]-px[x+1,y][0]))
          secondDifference = abs((px[x,y][0]-px[x-1,y][0]))
          thirdDifference = abs((px[x,y][0]-px[x,y+1][0]))
          forthDifference = abs((px[x,y][0]-px[x,y-1][0]))

        #  totalDifference = firstDifference + secondDifference + thirdDifference + forthDifference
          if(firstDifference > 50 ):
              mask[x,y] = 0
          elif(secondDifference > 50 ):
              mask[x,y] = 0
          elif(thirdDifference > 50 ):
              mask[x,y] = 0
          elif(forthDifference > 50 ):
              mask[x,y] = 0
          else:
              mask[x,y] = 1



          # if totalDifference>300:
          #     px[x,y] =(255,0,0)
          # elif totalDifference>200:
          #      px[x,y] =(200,0,0)
          # elif totalDifference>100:
          #      px[x,y] =(100,0,0)
          # elif totalDifference<100:
          #    px[x,y] =(50,0,0)


           #print(blurAverage)




sampleImage.show()

cv2.waitKey(0)
