import cv2
import sys
import os

userName=str(input("please enter the username for this record "))
images_path=os.path.join(os.getcwd(),"dataset",userName)
if not os.path.isdir(images_path):
    os.makedirs(images_path)

image_counter=0

cam=cv2.VideoCapture(0)
classefier=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
if cam.isOpened()==False:
    print("the app will close ")
    sys.exit(1)
while True:
    image_Validator,Image=cam.read()
    if image_Validator:
        gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
        faces=classefier.detectMultiScale(gray)
        if len(faces)==1:
            x,y,w,h=faces[0]
            print(faces)
            print(x,y,w,h,y+h,x+w)
            sub_image=Image[y:y+h,x:x+w,:]
            file_name=os.path.join(images_path,"image_{}.png".format(image_counter))
            cv2.imwrite(file_name,sub_image)
            image_counter+=1
            if image_counter==15:
                break
            cv2.imshow("face",sub_image)
        cv2.imshow("window",Image)

    Key=cv2.waitKey(50)
    if Key==ord("q"):
        break

cam.release()
