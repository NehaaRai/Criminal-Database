from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

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
    window=Tk()
    obj=Criminal(window)
    window.mainloop()