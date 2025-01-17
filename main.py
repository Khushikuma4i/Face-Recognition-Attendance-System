from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("Face Recognition System")
        # 1st image
        img=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images2.jpg")
        img=img.resize((350,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=150)

        #2nd image
        img1=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\image3.jpg")
        img1=img1.resize((350,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=150)

        #3rd image
        img2=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images18.jpg")
        img2=img2.resize((350,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=700,y=0,width=350,height=150)

        #4th image
        img3=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images13.jpg")
        img3=img3.resize((350,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1050,y=0,width=350,height=150)

        #bg image
        img4=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images33.jpg")
        img4=img4.resize((1400,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1400,height=700)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=35)

        #student buttom
        img5=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images24.jpeg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=250,width=170,height=35)

       
        #Face detector buttom
        img6=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images11.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
       
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=250,width=170,height=35)

        #Attendence buttom
        img7=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images12.jpg")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
       
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=250,width=170,height=35)


        #Help Desk
        img8=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images30.jpeg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
       
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=250,width=170,height=35)



        #Train buttom
        img9=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images29.jpeg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
       
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=320,width=170,height=170)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=470,width=170,height=35)

        #photo buttom
        img10=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images28.jpeg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
       
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=320,width=170,height=170)

        b1_1=Button(bg_img,text="Images",cursor="hand2",command=self.open_img,font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=470,width=170,height=35)

        #Developer
        img11=Image.open(r"C:\Users\vg180\OneDrive\Desktop\face recognition attendance system\student images\images25.jpeg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
       
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=320,width=170,height=170)

        b1_1=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=470,width=170,height=35)


        # logout buttom
        img12=Image.open(r"student images\logout.jpg")
        img12=img12.resize((150,150),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
       
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1100,y=320,width=170,height=170)

        b1_1=Button(bg_img,text="Logout",cursor="hand2",font=("times new roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=470,width=170,height=35)


    def open_img(self):
        os.startfile("data")    


    #**************************Function button****************


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)    


    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()






