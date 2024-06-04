from JES import *

def addFace(fileName, color1, color2):
  myPic = makePicture(fileName)
  print(getWidth(myPic))
  print(getHeight(myPic))
  addOvalFilled(myPic, 50, 60, 30, 50, color1)
  addOvalFilled(myPic, 60, 70, 15, 25, color2)
  
  addOvalFilled(myPic, 120, 60, 30, 50, color1)
  addOvalFilled(myPic, 130, 70, 15, 25, color2)
  #addLine(myPic, 0, 210, 210, 210, red)
  writePictureTo(myPic, "output.jpg")


#add "*name of file*.jpg" into the ( ) to change the face, add colors to change the colors of the eyes
addFace("emojiGirl.jpg", green, red)

def fun1(picture):
  for p in getPixels(picture):
    value = getRed(p)
    setRed(p, value * 2)

myPic = makePicture("face.jpg")
fun1(myPic)
writePictureTo(myPic, "fun1Results.jpg")