from abc import update_abstractmethods
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("Face Recognition System")


        # 1st image
        img=Image.open(r"student images\student1.jpeg")
        img=img.resize((350,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=150)

        #2nd image
        img1=Image.open(r"student images\student2.jpeg")
        img1=img1.resize((350,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=150)


         #bg image
        img4=Image.open(r"student images\images33.jpg")
        img4=img4.resize((1400,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1400,height=700)


        title_lbl=Label(bg_img,text="ATTENDACE",font=("times new roman",25,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1500,height=650)

         #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=690,height=580)

        img_left=Image.open(r"student images\student6.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=100)


        #right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendace Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=660,height=580)

        img_right=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\student7.jpeg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=100)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=50,width=1500,height=650)

        








    if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop() 