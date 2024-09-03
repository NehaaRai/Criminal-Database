from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


def main():
  win=Tk()
  app=login_window(win)
  win.mainloop()


class login_window:
  def __init__(self,window):
    self.window=window
    self.window.title("Login")
    self.window.geometry('1530x700+0+0')

    #background image
    img_logo=Image.open("background login.jpg")
    img_logo=img_logo.resize((1530,700))
    self.photo_logo=ImageTk.PhotoImage(img_logo)
    self.logo=Label(self.window,image=self.photo_logo)
    self.logo.place(x=0,y=0,relwidth=1,relheight=1)

    frame=Frame(self.window,bg="black")
    frame.place(x=530,y=125,width=340,height=450)

    img1=Image.open("login icon.png")
    img1=img1.resize((80,80))
    self.photo1=ImageTk.PhotoImage(img1)
    label_img1=Label(image=self.photo1,bg="black")
    label_img1.place(x=665,y=140)

    get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
    get_str.place(x=100,y=100)

    #labels and entry fields

    #username
    username=Label(frame,text="Email: ",font=("times new roman",15,"bold"),fg="white",bg="black")
    username.place(x=60,y=160)

    self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
    self.textuser.place(x=30,y=190,width=270)

    user=Image.open("user.png")
    user=user.resize((20,20))
    self.user1=ImageTk.PhotoImage(user)
    label_user=Label(frame,image=self.user1,bg="black")
    label_user.place(x=35,y=160)

    #password
    password=Label(frame,text="Password: ",font=("times new roman",15,"bold"),fg="white",bg="black")
    password.place(x=60,y=230)

    self.textpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
    self.textpassword.place(x=30,y=260,width=270)

    password=Image.open("password.jpg")
    password=password.resize((25,25))
    self.password1=ImageTk.PhotoImage(password)
    label_password=Label(frame,image=self.password1,bg="black")
    label_password.place(x=32,y=230)

    #login button
    login_button=Button(frame,command=self.login,text="Login Now",relief=RIDGE,font=("times new roman",15,"bold"),activeforeground="white",activebackground="#AEBDC7")
    login_button.place(x=100,y=320,width=140)

    #register button
    register_button=Button(frame,command=self.register_window,text="New User Register",borderwidth=0,font=("times new roman",10,"bold"),bg="black",fg="white",activebackground="black")
    register_button.place(x=0,y=390,width=170)

    #forgot button
    forgot_button=Button(frame,command=self.forgot_password_window,text="Forgot Password",borderwidth=0,font=("times new roman",10,"bold"),bg="black",fg="white",activebackground="black")
    forgot_button.place(x=0,y=410,width=160)

  def register_window(self):
    self.new_window=Toplevel(self.window)
    self.app=Register(self.new_window)

  def login(self):
    if self.textuser.get()=="" or self.textpassword=="":
      messagebox.showerror("Error","All fields are required.")
    elif self.textuser.get()=="a" and self.textpassword=="a":
      messagebox.showerror("Successful","All fields are required.")
    else:
      #messagebox.showerror("Invalid","Invalid username or password")
      conn=mysql.connector.connect(host="localhost",username="root",password="Qmwn@/#)$(1",database="management")
      cur=conn.cursor()
      query=('select * from register where email=%s and password=%s')
      value=(self.textuser.get(),self.textpassword.get(),)
      cur.execute(query,value)
      row=cur.fetchone()
      if row == None:
        messagebox.showerror("Error","Invalid username or password.")
      else:
        open_main=messagebox.askyesno("Ask","Access only admin?")
        if open_main>0:
          self.new_window=Toplevel(self.window)
          self.app=Criminal(self.new_window)
        else:
          if not open_main:
            return
      conn.commit()
      conn.close()

  #reset password function
  def reset_password(self):
    if self.combo_security.get()=="Select security question":
      messagebox.showerror("Error","Select security question.",parent=self.root2)
    elif self.textsecurity_ans.get()=="":
      messagebox.showerror("Error","Provide security answer.",parent=self.root2)
    elif self.textnew_password.get()=="":
      messagebox.showerror("Error","Provide new password.",parent=self.root2)
    else:
      conn=mysql.connector.connect(host="localhost",username="root",password="Qmwn@/#)$(1",database="management")
      cur=conn.cursor()
      query=('select * from register where email=%s and security_question=%s and security_answer=%s')
      value=(self.textuser.get(),self.combo_security.get(),self.textsecurity_ans.get())
      cur.execute(query,value)
      row=cur.fetchone()
      if row == None:
        messagebox.showerror("Error","Enter correct details.",parent=self.root2)
      else:
        query=('update register set password=%s where email=%s')
        value=(self.textnew_password.get(),self.textuser.get())
        cur.execute(query,value)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Your password has been reset.")

  #forgot password function
  def forgot_password_window(self):
    if self.textuser.get()=="":
      messagebox.showerror("Error","Please enter email.")
    else:  
      conn=mysql.connector.connect(host="localhost",username="root",password="Qmwn@/#)$(1",database="management")
      cur=conn.cursor()
      query=('select * from register where email=%s')
      value=(self.textuser.get(),)
      cur.execute(query,value)
      row=cur.fetchone()
      if row == None:
        messagebox.showerror("Error","Enter valid email.")
      else:
        conn.close()
        self.root2=Toplevel()
        self.root2.title("Forgot Password")
        self.root2.geometry('340x450+530+125')

        l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="#7EC8E3")
        l.place(x=10,y=20,relwidth=1)

        #forgot password security question
        security_ques=Label(self.root2,text="Security Question: ",font=("times new roman",13,"bold"),fg="black")
        security_ques.place(x=25,y=80)

        self.combo_security=ttk.Combobox(self.root2,font=("times new roman",10,"bold"),state="readonly")
        self.combo_security['values']=['Your birthplace','Your first pet','Your first school']
        self.combo_security.set("Select security question")
        self.combo_security.place(x=25,y=110,height=28,width=270)

        #forgot password security answer
        security_ans=Label(self.root2,text="Security Answer: ",font=("times new roman",13,"bold"),fg="black")
        security_ans.place(x=25,y=150)

        self.textsecurity_ans=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
        self.textsecurity_ans.place(x=25,y=180,width=270)

        #new password
        new_password=Label(self.root2,text="New Password: ",font=("times new roman",13,"bold"),fg="black")
        new_password.place(x=25,y=220)

        self.textnew_password=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
        self.textnew_password.place(x=25,y=250,width=270)

        #change password button
        forgot_button=Button(self.root2,command=self.reset_password,text="Change Password",borderwidth=0,font=("times new roman",13,"bold"),bg="#7EC8E3",fg="black",activebackground="black")
        forgot_button.place(x=85,y=300,width=160)
 

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
    login_button=Button(frame2,command=self.return_to_login,text="Login Now",relief=RIDGE,font=("times new roman",13,"bold"),bg="#145DA0",fg="black")
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

  def return_to_login(self):
     self.window.destroy


class Criminal:
  def __init__(self,window):
    self.window=window
    self.window.geometry('1530x700+0+0')
    self.window.title("Criminal Management System")


    #variables
    self.var_case_id=StringVar()
    self.var_criminal_name=StringVar()
    self.var_criminal_id=StringVar()
    self.var_dob=StringVar()
    self.var_age=StringVar()
    self.var_address=StringVar()
    self.var_doc=StringVar()
    self.var_doa=StringVar()
    self.var_father=StringVar()
    self.var_mother=StringVar()
    self.var_crime_type=StringVar()
    self.var_occupation=StringVar()
    self.var_gender=StringVar()
    self.var_wanted=StringVar()

    label_title=Label(self.window,text="Criminal Management System Software",font=("new times roman",40,"bold"),bg="black",fg="gold")
    label_title.place(x=0,y=0,width=1530,height=60)

    # logo
    img_logo=Image.open("logo.png")
    img_logo=img_logo.resize((50,50))
    self.photo_logo=ImageTk.PhotoImage(img_logo)
    self.logo=Label(self.window,image=self.photo_logo)
    self.logo.place(x=170,y=5,width=50,height=50)

    # image frame
    img_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
    img_frame.place(x=0,y=60,width=1530,height=120)

    # fbi1 image
    img_fbi1=Image.open("fbi-databases.jpg")
    img_fbi1=img_fbi1.resize((765,120))
    self.photo_fbi1=ImageTk.PhotoImage(img_fbi1)
    self.fbi1=Label(img_frame,image=self.photo_fbi1)
    self.fbi1.place(x=-45,y=5,width=765,height=120)

    # fbi2 image
    img_fbi2=Image.open("fbi-databases.jpg")
    img_fbi2=img_fbi2.resize((765,120))
    self.photo_fbi2=ImageTk.PhotoImage(img_fbi2)
    self.fbi2=Label(img_frame,image=self.photo_fbi2)
    self.fbi2.place(x=650,y=5,width=765,height=120)

    # main frame
    main_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
    main_frame.place(x=10,y=185,width=1350,height=505)

    #upper frame
    upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Criminal Information",font=("times new roman",15,"bold"),fg="blue")
    upper_frame.place(x=10,y=5,width=1325,height=240)

    #labels entry

    #case id
    caseid=Label(upper_frame,text="Case ID: ",font=("arial",11,"bold"),bg="white",fg="black")
    caseid.grid(row=0,column=0,padx=8,pady=5,sticky="W")

    caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=20,font=("arial",11,"bold"))
    caseentry.grid(row=0,column=1,pady=5,sticky="W")

    #criminal name
    criminal_name=Label(upper_frame,text="Criminal Name: ",font=("arial",11,"bold"),bg="white",fg="black")
    criminal_name.grid(row=0,column=2,padx=20,pady=5,sticky="W")

    criminal_nameentry=ttk.Entry(upper_frame,textvariable=self.var_criminal_name,width=20,font=("arial",11,"bold"))
    criminal_nameentry.grid(row=0,column=3,pady=5,sticky="W")

    #criminal id
    criminalid=Label(upper_frame,text="Criminal ID: ",font=("arial",11,"bold"),bg="white",fg="black")
    criminalid.grid(row=0,column=4,padx=20,pady=5,sticky="W")

    criminal_identry=ttk.Entry(upper_frame,textvariable=self.var_criminal_id,width=20,font=("arial",11,"bold"))
    criminal_identry.grid(row=0,column=5,pady=5,sticky="W")

    #dob
    dob=Label(upper_frame,text="Date of Birth: ",font=("arial",11,"bold"),bg="white",fg="black")
    dob.grid(row=0,column=6,padx=20,pady=5,sticky="W")

    #dob_cal = DateEntry(upper_frame, textvariable=self.var_dob,width= 24, background= "magenta3", foreground= "white",bd=2,date_pattern="yyyy-mm-dd")
    #dob_cal.grid(row=0,column=7,pady=5,sticky=W)

    dobentry=ttk.Entry(upper_frame,textvariable=self.var_dob,width=20,font=("arial",11,"bold"))
    dobentry.grid(row=0,column=7,pady=5,sticky="W")

    #age
    age=Label(upper_frame,text="Age: ",font=("arial",11,"bold"),bg="white",fg="black")
    age.grid(row=1,column=0,padx=8,pady=2,sticky="W")

    ageentry=ttk.Entry(upper_frame,textvariable=self.var_age,width=20,font=("arial",11,"bold"))
    ageentry.grid(row=1,column=1,pady=2,sticky="W")

    #address
    address=Label(upper_frame,text="Address: ",font=("arial",11,"bold"),bg="white",fg="black")
    address.grid(row=1,column=2,padx=20,pady=2,sticky="W")

    addressentry=ttk.Entry(upper_frame,textvariable=self.var_address,width=20,font=("arial",11,"bold"))
    addressentry.grid(row=1,column=3,pady=12,sticky="W")

    #doc
    doc=Label(upper_frame,text="Date of Crime: ",font=("arial",11,"bold"),bg="white",fg="black")
    doc.grid(row=1,column=4,padx=20,pady=2,sticky="W")

    #doc_cal = DateEntry(upper_frame, textvariable=self.var_doc,width= 24, background= "magenta3", foreground= "white",bd=2,date_pattern="yyyy-mm-dd")
    #doc_cal.grid(row=1,column=5,pady=2,sticky=W)

    docentry=ttk.Entry(upper_frame,textvariable=self.var_doc,width=20,font=("arial",11,"bold"))
    docentry.grid(row=1,column=5,pady=2,sticky="W")

    #doa
    doa=Label(upper_frame,text="Date of Arrest: ",font=("arial",11,"bold"),bg="white",fg="black")
    doa.grid(row=1,column=6,padx=20,pady=2,sticky="W")

    #doa_cal = DateEntry(upper_frame, textvariable=self.var_doa,width= 24, background= "magenta3", foreground= "white",bd=2,date_pattern="yyyy-mm-dd")
    #doa_cal.grid(row=1,column=7,pady=2,sticky=W)

    doaentry=ttk.Entry(upper_frame,textvariable=self.var_doa,width=20,font=("arial",11,"bold"))
    doaentry.grid(row=1,column=7,pady=2,sticky="W")

    #father
    father=Label(upper_frame,text="Father's Name: ",font=("arial",11,"bold"),bg="white",fg="black")
    father.grid(row=2,column=0,padx=8,pady=2,sticky="W")

    fatherentry=ttk.Entry(upper_frame,textvariable=self.var_father,width=20,font=("arial",11,"bold"))
    fatherentry.grid(row=2,column=1,pady=2,sticky="W")

    #mother
    mother=Label(upper_frame,text="Mother's Name: ",font=("arial",11,"bold"),bg="white",fg="black")
    mother.grid(row=2,column=2,padx=20,pady=2,sticky="W")

    motherentry=ttk.Entry(upper_frame,textvariable=self.var_mother,width=20,font=("arial",11,"bold"))
    motherentry.grid(row=2,column=3,pady=2,sticky="W")

    #crime type
    ctype=Label(upper_frame,text="Crime Type: ",font=("arial",11,"bold"),bg="white",fg="black")
    ctype.grid(row=2,column=4,padx=20,pady=2,sticky="W")

    ctypeentry=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=20,font=("arial",11,"bold"))
    ctypeentry.grid(row=2,column=5,pady=2,sticky="W")

    #occupation
    occupation=Label(upper_frame,text="Occupation: ",font=("arial",11,"bold"),bg="white",fg="black")
    occupation.grid(row=2,column=6,padx=20,pady=2,sticky="W")

    occupationentry=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=20,font=("arial",11,"bold"))
    occupationentry.grid(row=2,column=7,pady=2,sticky="W")

    #gender
    gender=Label(upper_frame,text="Gender: ",font=("arial",11,"bold"),bg="white",fg="black")
    gender.grid(row=3,column=0,padx=8,pady=10,sticky="W")

    radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
    radio_frame_gender.place(x=131,y=123,height=28,width=167)

    male=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Male",value="Male",font=("arial",9,"bold"),bg="white")
    male.grid(row=0,column=0,padx=5,sticky=W)
    female=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Female",value="Female",font=("arial",9,"bold"),bg="white")
    female.grid(row=0,column=1,padx=5,sticky=W)

    #most wanted
    wanted=Label(upper_frame,text="Most Wanted: ",font=("arial",11,"bold"),bg="white",fg="black")
    wanted.grid(row=3,column=2,padx=20,pady=10,sticky="W")

    radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
    radio_frame_wanted.place(x=458,y=123,height=28,width=167)

    yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="Yes",value="Yes",font=("arial",9,"bold"),bg="white")
    yes.grid(row=0,column=0,padx=5,sticky=W)
    no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="No",value="No",font=("arial",9,"bold"),bg="white")
    no.grid(row=0,column=1,padx=5,sticky=W)

    #buttons
    button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
    button_frame.place(x=10,y=165,height=40,width=472)

    # add button
    btn_add=Button(button_frame,command=self.add_data,text="Save Record",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_add.grid(row=0,column=0,padx=7,pady=5)

    # update button
    btn_update=Button(button_frame,command=self.update_data,text="Update Record",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_update.grid(row=0,column=1,padx=3,pady=5)

    # delete button
    btn_delete=Button(button_frame,command=self.delete_data,text="Delete Record",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_delete.grid(row=0,column=2,padx=3,pady=5)

    # clear button
    btn_clear=Button(button_frame,command=self.clear_data,text="Clear Record",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_clear.grid(row=0,column=3,padx=3,pady=5)



    #lower frame
    lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Criminal Database",font=("times new roman",15,"bold"),fg="blue")
    lower_frame.place(x=10,y=245,width=1325,height=250)

    #search frame
    search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg="white",text="Search Criminal Record",font=("times new roman",11,"bold"),fg="blue")
    search_frame.place(x=5,y=0,width=1312,height=60)

    search_by=Label(search_frame,text="Search By: ",font=("arial",11,"bold"),bg="red",fg="white")
    search_by.grid(row=0,column=0,padx=5,pady=5,sticky="W")

    #combo box
    self.var_com_search=StringVar()
    combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state="readonly")
    combo_search_box["value"]=("Case_ID","Criminal_ID")
    combo_search_box.set("Select Option")
    combo_search_box.grid(row=0,column=1,sticky=W,padx=5,pady=5)

    self.var_search=StringVar()
    search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
    search_txt.grid(row=0,column=2,pady=2,sticky="W")

    # search button
    btn_search=Button(search_frame,command=self.search_data,text="Search",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_search.grid(row=0,column=3,padx=3,pady=5)

    # all button
    btn_all=Button(search_frame,command=self.fetch_data,text="Show All",font=("arial",9,"bold"),width=14,bg="blue",fg="white")
    btn_all.grid(row=0,column=4,padx=3,pady=5)

    #table frame
    table_frame=Frame(lower_frame,bd=2,relief=RIDGE)
    table_frame.place(x=5,y=66,width=1312,height=152)

    #scroll bar
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

    self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.criminal_table.xview)
    scroll_y.config(command=self.criminal_table.yview)

    self.criminal_table.heading("1",text="Case ID")
    self.criminal_table.heading("2",text="Criminal Name")
    self.criminal_table.heading("3",text="Criminal ID")
    self.criminal_table.heading("4",text="Date of Birth")
    self.criminal_table.heading("5",text="Age")
    self.criminal_table.heading("6",text="Address")
    self.criminal_table.heading("7",text="Date of Crime")
    self.criminal_table.heading("8",text="Date of Arrest")
    self.criminal_table.heading("9",text="Father's Name")
    self.criminal_table.heading("10",text="Mother's Name")
    self.criminal_table.heading("11",text="Crime Type")
    self.criminal_table.heading("12",text="Occupation")
    self.criminal_table.heading("13",text="Gender")
    self.criminal_table.heading("14",text="Wanted")

    self.criminal_table["show"]="headings"

    self.criminal_table.column("1",width=50)
    self.criminal_table.column("2",width=120)
    self.criminal_table.column("3",width=100)
    self.criminal_table.column("4",width=100)
    self.criminal_table.column("5",width=50)
    self.criminal_table.column("6",width=100)
    self.criminal_table.column("7",width=100)
    self.criminal_table.column("8",width=100)
    self.criminal_table.column("9",width=120)
    self.criminal_table.column("10",width=120)
    self.criminal_table.column("11",width=100)
    self.criminal_table.column("12",width=100)
    self.criminal_table.column("13",width=50)
    self.criminal_table.column("14",width=50)
        
    self.criminal_table.pack(fill=BOTH,expand=1)
    self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

    self.fetch_data()


  # add function
  def add_data(self):
    if self.var_case_id.get()=="" or self.var_criminal_name.get()=="" or self.var_criminal_id.get()=="" or self.var_crime_type.get()=="":
      messagebox.showerror("Error","Case ID, Criminal Name, Criminal ID and Crime Type are required.")
    else:
      try:
        conn=mysql.connector.connect(host="localhost",user="root",password=f"Qmwn@/#)$(1",database="management")
        cur=conn.cursor()
        cur.execute("insert into criminal values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(int(self.var_case_id.get()),self.var_criminal_name.get(),self.var_criminal_id.get(),self.var_dob.get(),int(self.var_age.get()),self.var_address.get(),self.var_doc.get(),self.var_doa.get(),self.var_father.get(),self.var_mother.get(),self.var_crime_type.get(),self.var_occupation.get(),self.var_gender.get(),self.var_wanted.get()))
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()
        messagebox.showinfo("Success","Record has been added.")

      except Exception as e:
        messagebox.showerror("Error",f"Due to: {str(e)}")
            

  #fetch data
  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",user="root",password=f"Qmwn@/#)$(1",database="management")
    cur=conn.cursor()
    cur.execute("select * from criminal")
    data=cur.fetchall()
    if len(data)!=0:
      self.criminal_table.delete(*self.criminal_table.get_children())
      for i in data:
        self.criminal_table.insert("",END,values=i)
      conn.commit()
    conn.close()
    
  #get cursor
  def get_cursor(self,event=""):
    cursor_row=self.criminal_table.focus()
    content=self.criminal_table.item(cursor_row)
    data=content["values"]

    self.var_case_id.set(data[0])
    self.var_criminal_name.set(data[1])
    self.var_criminal_id.set(data[2])
    self.var_dob.set(data[3])
    self.var_age.set(data[4])
    self.var_address.set(data[5])
    self.var_doc.set(data[6])
    self.var_doa.set(data[7])
    self.var_father.set(data[8])
    self.var_mother.set(data[9])
    self.var_crime_type.set(data[10])
    self.var_occupation.set(data[11])
    self.var_gender.set(data[12])
    self.var_wanted.set(data[13])

  #update
  def update_data(self):
    if self.var_case_id.get()=="" or self.var_criminal_name.get()=="" or self.var_criminal_id.get()=="" or self.var_crime_type.get()=="":
      messagebox.showerror("Error","Case ID, Criminal Name, Criminal ID and Crime Type are required.")
    else:
      try:
        update=messagebox.askyesno("Update","Are you sure, you want to update this record?")
        if update>0:    
          conn=mysql.connector.connect(host="localhost",user="root",password=f"Qmwn@/#)$(1",database="management")
          cur=conn.cursor()
          cur.execute("update criminal set Case_ID=%s,Criminal_name=%s,DOB=%s,Age=%s,Address=%s,Date_of_crime=%s,Date_of_arrest=%s,Father_name=%s,Mother_name=%s,Crime_type=%s,Occupation=%s,Gender=%s,Wanted=%s where Criminal_ID=%s",(int(self.var_case_id.get()),self.var_criminal_name.get(),self.var_dob.get(),int(self.var_age.get()),self.var_address.get(),self.var_doc.get(),self.var_doa.get(),self.var_father.get(),self.var_mother.get(),self.var_crime_type.get(),self.var_occupation.get(),self.var_gender.get(),self.var_wanted.get(),self.var_criminal_id.get()))
        else:
          if not update:
            return
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated.")

      except Exception as e:
        messagebox.showerror("Error",f"Due to: {str(e)}")

  #delete
  def delete_data(self):
    if self.var_case_id.get()=="" or self.var_criminal_name.get()=="" or self.var_criminal_id.get()=="" or self.var_crime_type.get()=="":
      messagebox.showerror("Error","Case ID, Criminal Name, Criminal ID and Crime Type are required.")
    else:
      try:
        delete=messagebox.askyesno("Delete","Are you sure, you want to delete this record?")
        if delete>0:
          conn=mysql.connector.connect(host="localhost",user="root",password=f"Qmwn@/#)$(1",database="management")
          cur=conn.cursor()
          sql="delete from criminal where Criminal_ID=%s"
          value=(self.var_criminal_id.get(),)
          cur.execute(sql,value)
        else:
          if not delete:
            return
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()
            
      except Exception as e:
        messagebox.showerror("Error",f"Due to: {str(e)}")

  #clear
  def clear_data(self):
    self.var_case_id.set("")
    self.var_criminal_name.set("")
    self.var_criminal_id.set("")
    self.var_dob.set("")
    self.var_age.set("")
    self.var_address.set("")
    self.var_doc.set("")
    self.var_doa.set("")
    self.var_father.set("")
    self.var_mother.set("")
    self.var_crime_type.set("")
    self.var_occupation.set("")
    self.var_gender.set("")
    self.var_wanted.set("")

  #search
  def search_data(self):
    if self.var_com_search.get()=="":
      messagebox.showerror("Error","Select a parameter.")
    else:
      try:
        conn=mysql.connector.connect(host="localhost",user="root",password=f"Qmwn@/#)$(1",database="management")
        cur=conn.cursor()
        cur.execute("select * from criminal where " +str(self.var_com_search.get())+" like '%"+ str(self.var_search.get()+"%'"))
        rows=cur.fetchall()
        if len(rows)!=0:
          self.criminal_table.delete(*self.criminal_table.get_children())
          for i in rows:
            self.criminal_table.insert("",END,values=i)
          conn.commit()
          conn.close()

      except Exception as e:
        messagebox.showerror("Error",f"Due to: {str(e)}")


if __name__=="__main__":
    main()
