from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
  def __init__(self,window):
    self.window=window
    self.window.title("Register")
    self.window.geometry('1530x700+0+0')

    #variables
    self.var_fname=StringVar()
    self.var_lname=StringVar()
    self.var_email=StringVar()
    self.var_contact=StringVar()
    self.var_security_question=StringVar()
    self.var_security_answer=StringVar()
    self.var_password=StringVar()
    self.var_confirm_password=StringVar()

    #background image
    img_background=Image.open("background login.jpg")
    img_background=img_background.resize((1530,700))
    self.photo_background=ImageTk.PhotoImage(img_background)
    self.background=Label(self.window,image=self.photo_background)
    self.background.place(x=0,y=0,relwidth=1,relheight=1)


    #frame and image
    frame=Frame(self.window,bg="black")
    frame.place(x=150,y=120,width=360,height=450)

    img_clipboard=Image.open("clipboard.jpg")
    img_clipboard=img_clipboard.resize((300,390))
    self.photo_clipboard=ImageTk.PhotoImage(img_clipboard)
    self.clipboard=Label(frame,image=self.photo_clipboard)
    self.clipboard.place(x=30,y=30)

    frame2=Frame(self.window,bg="black")
    frame2.place(x=510,y=120,width=720,height=450)

    register_label=Label(frame2,text="Register Here",font=("times new roman",20,"bold"),bg="black",fg="#7EC8E3")
    register_label.place(x=20,y=25)

    #labels and entry fields

    #firstname
    firstname=Label(frame2,text="First Name: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    firstname.place(x=20,y=90)

    self.textfirstname=ttk.Entry(frame2,textvariable=self.var_fname,font=("times new roman",13,"bold"))
    self.textfirstname.place(x=20,y=120,width=270)

    #lastname
    lastname=Label(frame2,text="Last Name: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    lastname.place(x=370,y=90)

    self.textlastname=ttk.Entry(frame2,textvariable=self.var_lname,font=("times new roman",13,"bold"))
    self.textlastname.place(x=370,y=120,width=270)

    #email
    email=Label(frame2,text="Email ID: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    email.place(x=20,y=160)

    self.textemail=ttk.Entry(frame2,textvariable=self.var_email,font=("times new roman",13,"bold"))
    self.textemail.place(x=20,y=190,width=270)

    #contact
    contact=Label(frame2,text="Contact: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    contact.place(x=370,y=160)

    self.textcontact=ttk.Entry(frame2,textvariable=self.var_contact,font=("times new roman",13,"bold"))
    self.textcontact.place(x=370,y=190,width=270)

    #security question
    security_ques=Label(frame2,text="Security Question: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    security_ques.place(x=20,y=230)

    self.combo_security=ttk.Combobox(frame2,textvariable=self.var_security_question,font=("times new roman",10,"bold"),state="readonly")
    self.combo_security['values']=['Your birthplace','Your first pet','Your first school']
    self.combo_security.set("Select security question")
    self.combo_security.place(x=20,y=260,height=28,width=270)

    #security answer
    security_ans=Label(frame2,text="Security Answer: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    security_ans.place(x=370,y=230)

    self.textsecurity_ans=ttk.Entry(frame2,textvariable=self.var_security_answer,font=("times new roman",13,"bold"))
    self.textsecurity_ans.place(x=370,y=260,width=270)

    #password
    password=Label(frame2,text="Password: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    password.place(x=20,y=300)

    self.textpassword=ttk.Entry(frame2,textvariable=self.var_password,font=("times new roman",13,"bold"))
    self.textpassword.place(x=20,y=330,width=270)

    #confirm password
    confirm_password=Label(frame2,text="Confirm Password: ",font=("times new roman",13,"bold"),fg="white",bg="black")
    confirm_password.place(x=370,y=300)

    self.textconfirm_password=ttk.Entry(frame2,textvariable=self.var_confirm_password,font=("times new roman",13,"bold"))
    self.textconfirm_password.place(x=370,y=330,width=270)

    #register button
    register_button=Button(frame2,command=self.register_data,text="Register",relief=RIDGE,font=("times new roman",13,"bold"),bg="#7EC8E3",fg="black")
    register_button.place(x=370,y=380,width=140)

    #login button
    login_button=Button(frame2,text="Login Now",relief=RIDGE,font=("times new roman",13,"bold"),bg="#145DA0",fg="black")
    login_button.place(x=20,y=380,width=140)

  def register_data(self):
    if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_question.get()=="Select security question" or self.var_security_answer=="" or self.var_password=="":
      messagebox.showerror("Error"," All fields are required.")
    elif len(self.var_contact.get()) != 10:
      messagebox.showerror("Error","Enter valid contact.")
    elif self.var_password.get() != self.var_confirm_password.get():
      messagebox.showerror("Error","Confirm your password correctly")
    else:
      conn=mysql.connector.connect(host="localhost",username="root",password="Qmwn@/#)$(1",database="management")
      cur=conn.cursor()
      query=('select * from register where email=%s')
      value=(self.var_email.get(),)
      cur.execute(query,value)
      row=cur.fetchone()
      if row != None:
        messagebox.showerror("Error","Email already in use. Please register with another email.")
      else:
        cur.execute('insert into register values (%s,%s,%s,%s,%s,%s,%s)', (self.var_fname.get(),self.var_lname.get(),self.var_email.get(),self.var_contact.get(),self.var_security_question.get(),self.var_security_answer.get(),self.var_password.get()))
        messagebox.showinfo("Success","Registered successfully.")
      conn.commit()
      conn.close()
      
    


    


if __name__=="__main__":
  window=Tk()
  app=Register(window)
  window.mainloop()