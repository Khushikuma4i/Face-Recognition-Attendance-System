from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        ################   FIRST IMAGE ##################################

        img_top = Image.open(r"student images\image 28.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        ################   SECOND IMAGE ##################################

        img_bottom = Image.open(r"student images\images29.jpg")
        img_bottom = img_bottom.resize((800, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=800, height=700)

        #####################      BUTTON    #############################

        b1_1 = Button(self.root, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 18, "bold"), bg="DARK GREEN", fg="white", command=self.face_recog)
        b1_1.place(x=900, y=680, width=400, height=50)

    #########################  ATTENDANCE   ################################

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    ################## FACE RECOGNITION ################################

    def face_recog(self):
        def draw_boundary(img, classifier, scalefactor, minNeighbors, colors, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="vishalgupta@9123",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()

                if n is not None:
                    n = n[0]  # Extracting the first element from the tuple returned by fetchone()
                    r = r[0]
                    d = d[0]
                    i = i[0]



                if confidence >= 80:
                    cv2.putText(img, f"ID:{i}", (x,y-65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)
                    cv2.putText(img, f"Roll:{r}", (x,y-45), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)
                    cv2.putText(img, f"Name:{n}", (x,y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),2)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Id ", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)

                coord = [x,y,w,h]   

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition ", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
     root = Tk()
     obj = Face_Recognition(root)
     root.mainloop()
