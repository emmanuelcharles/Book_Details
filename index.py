from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from tkinter import ttk
from datetime import datetime


conn_1 = MongoClient('localhost', 27017)
db_conn = conn_1.project_db_test
coll_conn = db_conn.Sample02
coll_conn_2 = db_conn.log_test

######################################################################### New user#########################

def new_user():                    
    def new_user_1():
        def new_user_1_clr():
            a = e1.get()
            b = e2.get()
            c = e3.get()
            if len(a)>0 or len(b)>0 or len(c)>0:
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
        def new_user_1_match():
            a = str(e1.get())
            b = str(e2.get())
            c = str(e3.get())

            found1 = 0
            found2 = 0
            found3 = 0
            if(len(a)>0 and len(b)>0 and len(c)>0):
                if(b == c):
                    for i in coll_conn_2.find({},{'_id':0, 'user':1}):
                        if( a == str(i['user'].encode('utf-8').decode('utf-8'))):
                            found2 +=1
                else:
                    found1+=1
            else:
                found3 +=1
                messagebox.showinfo(title="Warning",message = "Please Enter your Username and Password...") 

            if(found1 == 0 and found2 == 0 and found3 == 0):
                coll_conn_2.insert_one({'user': a, 'password': b})
                messagebox.showinfo(message="New User is Successfully Registered...")
            elif(found1 ==1):
                messagebox.showinfo(title="Warning", message="Your password not match with confirm password...")
            else:
                messagebox.showinfo(title="Warning", message="Your username is already exist...")
                
        nu_w2 = Frame(nu_w)
        nu_w2.place(height = 450, width = 500, x =0 ,y=0)
        #nu_w2 = Tk()
        #nu_w2.geometry('500x450+0+0')
        #nu_w2.title("Register New User")
        nu_w2.config(background = "white")
        #nu_w2.resizable(width = 0, height = 0)
        lh1 = Label(nu_w2, text='Add New User', font=('serif',25,'bold'), bg = 'white')
        l1 = Label(nu_w2, text ="Username:", font =('serif', 10 , 'bold'), bg = 'white')
        e1 = Entry(nu_w2, font=('serif', 10 , 'bold'), width = 40, bg ='white')
        l2 = Label(nu_w2, text ="New Password:", font =('serif', 10 , 'bold'), bg = 'white')
        e2 = Entry(nu_w2, font=('serif', 10 , 'bold'), show = '*',width = 40, bg ='white')
        l3 = Label(nu_w2, text ="Confirm Password:", font =('serif', 10 , 'bold'), bg = 'white')
        e3 = Entry(nu_w2, font=('serif', 10 , 'bold'),show = '*', width = 40, bg ='white')
        b1 = Button(nu_w2, text='Submit', font=('serif', 12 ), height = 2, width = 20, command = new_user_1_match)
        b2 = Button(nu_w2, text='Clear', font=('serif', 12 ),height = 2 , width = 20, command = new_user_1_clr)
        lh1.place(x = 130 , y = 20)
        l1.place(x = 25, y = 122)
        e1.place(x = 165 , y = 122)
        l2.place(x = 25, y = 182)
        e2.place(x = 165 , y = 182)
        l3.place(x = 25, y = 242)
        e3.place(x = 165 , y = 242)
        b1.place(x = 55 , y = 300)
        b2.place(x = 259 , y = 300)
        nu_w2.mainloop()

    def new_user_clr():
        a = str(e2.get())
        b = str(e3.get())

        if(len(a)>0 or len(b)>0):
            e2.delete(0, END)
            e3.delete(0, END)

    def new_use_auth():
        a = str(e2.get())
        b = str(e3.get())
        found = 0
        if(len(a)>0 and len(b)>0):
            for i in coll_conn_2.find({},{'_id':0}):
                if(a == str(i['user'].encode('utf-8').decode('utf-8')) and b == str(i['password'].encode('utf-8').decode('utf-8'))):
                    found = 1
        else:
            messagebox.showinfo(title="Warning", message="Please fill the username and password...")

        if(found > 0):
            new_user_1()
        else:
            messagebox.showinfo(title= "Warning", message="Username and password are not matched. Please try again...")      
            
    nu_w = Tk()
    nu_w.geometry('500x450+500+180')
    nu_w.title("Authentication")
    nu_w.config(background ='white')
    nu_w.resizable(width = 0, height = 0)
    l1 = Label(nu_w, text="Authentication", font=('serif',23,'bold'), bg ='white', fg ='dark green')
    l2 = Label(nu_w, text="Username:", font=('serif', 11, 'bold'),bg ='white')
    e2 = Entry(nu_w, width = 50, bg='white')
    l3 = Label(nu_w, text="Password:", font=('serif', 11, 'bold'),bg ='white')
    e3 = Entry(nu_w, width = 50, bg='white', show="*")
    b1 = Button(nu_w, text='Submit', width = 25 , height = 3, command = new_use_auth)
    b2 = Button(nu_w, text='Clear', width = 25, height = 3, command = new_user_clr)
    l1.place(x = 140, y = 20)
    l2.place(x = 30 , y = 120)
    e2.place(x = 135 , y =120)
    l3.place(x = 30 , y = 200)
    e3.place(x = 135 , y = 200)
    b1.place(x = 50 , y = 280)
    b2.place(x = 260 , y = 280)
    nu_w.mainloop()

######################################################################### Operation 04_2####################################

def ser_all():
        
        ser_all_w = Tk()
        ser_all_w.geometry('1300x600+20+40')
        ser_all_w.title("All Details...")
        y1 = 50
        for i in coll_conn.find({},{'_id':0}):
                        L1 = Label(ser_all_w, text = i, font = ('serif', 11))
                        L1.place(x = 10 , y = y1)
                        y1+=35
        x_scroll = Scrollbar(ser_all_w)
        y_scroll = Scrollbar(ser_all_w, orient = HORIZONTAL)

        x_scroll.pack(side = RIGHT, fill = Y)
        y_scroll.pack(side = BOTTOM, fill = X)

#########################################################################Operation 04_1#######################################
def ser_sin():

        def clr():
                a = str(ser_sin_e.get())
                if len(a)>0:
                        ser_sin_e.delete(0, END)
        def find():
                found = 0
                a = str(ser_sin_e.get())
                for i in coll_conn.find({},{'_id': 0, 'Bookid': 1}):
                        if a == str(i['Bookid'].encode('utf-8').decode('utf-8')):
                                found+=1
                                for j in coll_conn.find({},{'_id':0}):
                                        result_l1 = Label(ser_sin_f, text = 'Book ID:', font =('serif', 11, 'bold' ), bg ='white')
                                        result_l1.place(x = 110, y = 230)
                                        result_l2 = Label(ser_sin_f, text = j['Bookid'], font =('serif', 11 ), bg ='white')
                                        result_l2.place(x = 250, y = 230)
                                        result_l1 = Label(ser_sin_f, text = 'Book Name:', font =('serif', 11, 'bold' ), bg ='white')
                                        result_l1.place(x = 110, y = 260)
                                        result_l3 = Label(ser_sin_f, text = j['BookName'], font =('serif', 11), bg ='white')
                                        result_l3.place(x = 250, y = 260)
                                        result_l4 = Label(ser_sin_f, text = "Author:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l4.place(x = 110, y = 290)
                                        result_l5 = Label(ser_sin_f, text = j['Author'], font =('serif', 11), bg ='white')
                                        result_l5.place(x = 250, y = 290)
                                        result_l6 = Label(ser_sin_f, text = "Price:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l6.place(x = 110, y = 320)
                                        result_l7 = Label(ser_sin_f, text = j['Price'], font =('serif', 11), bg ='white')
                                        result_l7.place(x = 250, y = 320)
                                        result_l8 = Label(ser_sin_f, text = "Page:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l8.place(x = 110, y = 350)
                                        result_l5 = Label(ser_sin_f, text = j['Page'], font =('serif', 11), bg ='white')
                                        result_l5.place(x = 250, y = 350)
                                        result_l10 = Label(ser_sin_f, text = "Language:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l10.place(x = 110, y = 380)
                                        result_l5 = Label(ser_sin_f, text = j['Language'], font =('serif', 11), bg ='white')
                                        result_l5.place(x = 250, y = 380)
                                        result_l12 = Label(ser_sin_f, text = "Category:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l12.place(x = 110, y = 410)
                                        result_l5 = Label(ser_sin_f, text = j['Category'], font =('serif', 11), bg ='white')
                                        result_l5.place(x = 250, y = 410)
                                        result_l14 = Label(ser_sin_f, text = "Description:", font =('serif', 11, 'bold'), bg ='white')
                                        result_l14.place(x = 110, y = 440)
                                        result_l5 = Label(ser_sin_f, text = j['Book_Description'], font =('serif', 11), bg ='white')
                                        result_l5.place(x = 250, y = 440)
                if found == 0:
                        result_f = Label(text = "Sorry! Search not found...", font =('serif', 13), bg ='white')
                        result_f.place(x = 300, y = 260)
                
                        
                        
        ser_sin_f = Tk()
        ser_sin_f.geometry("800x550+340+90")
        ser_sin_f.title("Search Operation")
        ser_sin_f.resizable(width='false', height='false')
        ser_sin_f.config(background="white")
        ser_sin_l1 = Label(ser_sin_f, text = 'Search your Details', font=('serif', 20 , 'bold'),bg = 'white')
        ser_sin_el = Label(ser_sin_f, text="Book ID", font=('serif', 10 , 'bold'),bg = 'white')
        ser_sin_e = Entry(ser_sin_f, width = 100, bg='white')
        ser_sin_sub = Button(ser_sin_f, text='Submit', width = 25 , height = 3, command = find)
        ser_sin_clr = Button(ser_sin_f, text='Clear', width = 25 , height = 3, command = clr)
        ser_sin_l1.pack()
        ser_sin_el.place(x = 80 , y = 90)
        ser_sin_e.place(x = 160 , y = 90)
        ser_sin_sub.place(x = 200 , y = 130)
        ser_sin_clr.place(x = 440, y = 130)
        ser_sin_f.mainloop()
        
###########################################################################Operation 04 ########################################
def ser_win():       
    ser_win_f = Tk()
    ser_win_f.geometry("440x390+490+90")
    ser_win_f.title("Search Operation")
    ser_win_f.config(background="white")
    ser_win_f.resizable(height = "false", width = "false")

    ser_one_b = Button(ser_win_f, text = "Search", width = 40 , height = 3, command = ser_sin)
    view_all_b = Button(ser_win_f, text = "View All", width = 40 , height = 3, command = ser_all)

    ser_l = Label(ser_win_f, text="Search Operation", font=('Serif', 35 , 'bold'), bg='white')

    ser_l.place(x = 23 , y = 55)
    ser_one_b.place(x = 75 , y = 170)
    view_all_b.place(x= 75, y = 240)
    ser_win_f.mainloop()


##################################################################################### Operation 02 #################################
def up_win():

    def up_win_clr():
        a = str(up_win_e1.get())
        b = str(up_win_e2.get())
        c = str(up_win_e3.get())

        if len(a)>0 or len(b) >0 or len(c)>0:
            up_win_e1.delete(0, END)
            up_win_e2.delete(0, END)
            up_win_e3.delete(0, END)
            
    def up_win_up():
        a = str(up_win_e1.get())
        b = str(up_win_e2.get())
        c = str(up_win_e3.get())
        found = 0
        
        if len(a)>0 and len(b)>0 and len(c)>0:
            for i in coll_conn.find({}):
                if a == str(i['Bookid'].encode('utf-8').decode('utf-8')):
                    found +=1
            if found == 1:
                coll_conn.update_one({'Bookid':a},{'$set':{b:c}})
                messagebox.showinfo(message="Your details are updated successfully...", title = "Message")
            else:
                messagebox.showinfo(message ="Failed to update your details...", title = "Error")
        else:
            messagebox.showinfo(message="Please fill the details...", title="Message")
                
    up_win_s = Tk()
    up_win_s.geometry('450x550+530+90')
    up_win_s.title('Delete Operation')
    up_win_s.config(background ="white")

    up_win_ml = Label(up_win_s, text="Update Section", bg='white', fg='black', font=('serif', 25,'bold'))
    up_win_l1 = Label(up_win_s, text="Enter your ID:", bg ='white', fg='black', font=('serif',10, 'bold'))
    up_win_l2 = Label(up_win_s, text="Enter field to update:", bg ='white', fg='black', font=('serif',10, 'bold'))
    up_win_l3 = Label(up_win_s, text="Update the details:", bg ='white', fg='black', font=('serif',10, 'bold'))
    up_win_l4 = Label(up_win_s, text="Bookid and Book_Description fields cannot be updated..." , bg ='white', fg='red', font=('serif', 9 , 'bold'))

    up_win_e1 = Entry(up_win_s, font=('serif', 10 , 'bold'), width = 36, bg='white')
    up_win_e2 = ttk.Combobox(up_win_s, font=('serif', 10 , 'bold'), width = 33, values =['BookName','Author','Price','Page','Language','Category'])
    up_win_e3 = Entry(up_win_s, font=('serif', 10 , 'bold'), width = 36, bg='white')
    
    up_win_b1 = Button(up_win_s, text="Update", width = 50 , height = 3, font=('serif', 10 , 'bold'), command = up_win_up)
    up_win_b2 = Button(up_win_s, text="Clear", width = 50 , height = 3, font=('serif', 10 , 'bold'), command = up_win_clr)

    up_win_e1.place(x = 160 , y = 130)
    up_win_e2.place(x = 160 , y = 190)
    up_win_e3.place(x = 160 , y = 250)
    
    up_win_b1.place(x = 20 , y = 330)
    up_win_b2.place(x = 20 , y = 410)
    
    up_win_l1.place(x = 19 , y = 130)
    up_win_l2.place(x = 19 , y = 190)
    up_win_l3.place(x = 19 , y = 250)
    up_win_l4.place(x = 60 , y = 510)
    
    up_win_ml.place(x = 110 , y = 25)
    up_win_s.mainloop()

############################################################################################ Operation 03 ###########################

def del_win():

    def del_win_clr():
        a = str(del_win_e1.get())
        b = str(del_win_e2.get())
        c = str(del_win_e3.get())

        if len(a)>0 or len(b) >0 or len(c)>0:
            del_win_e1.delete(0, END)
            del_win_e2.delete(0, END)
            del_win_e3.delete(0, END)

    def del_win_Delete():
        Namefound = 0
        a = str(del_win_e1.get())
        b = str(del_win_e2.get())
        c = str(del_win_e3.get())
        
        if len(a)>0 and len(b)>0 and len(c)>0:
            for i in coll_conn.find({}):
                if b == str(i['BookName'].encode('utf-8').decode('utf-8')) and a == str(i['Bookid'].encode('utf-8').decode('utf-8')) and c == str(i['Author'].encode('utf-8').decode('utf-8')):
                    Namefound +=1
                    
            if Namefound == 1:
                coll_conn.delete_one({'Bookid':a})
                messagebox.showinfo(message="Your details are deleted successfully", title="Message")
            else:
                messagebox.showinfo(message="You details are not found. Please try again", title="Error")
                
        elif len(a)==0 and len(b)>0 and len(c)>0:
            for i in coll_conn.find({}):
                if b == str(i['BookName'].encode('utf-8').decode('utf-8')) and c == str(i['Author'].encode('utf-8').decode('utf-8')):
                    Namefound +=1
                    
            if Namefound == 1:
                coll_conn.delete_one({'BookName':b, 'Author':c})
                messagebox.showinfo(message="Your details are deleted successfully...", title="Message")
            else:
                messagebox.showinfo(message="Please try to identify by id...", title="Error")
        else:
            messagebox.showinfo(message="Please fill the details to delete...", title="Error")
                
    

    del_win_s = Tk()
    del_win_s.geometry('450x550+530+90')
    del_win_s.title('Delete Operation')
    del_win_s.config(background ="white")

    del_win_ml = Label(del_win_s, text="Delete Section", bg='white', fg='black', font=('serif', 25,'bold'))
    del_win_l1 = Label(del_win_s, text="Enter your ID :", bg ='white', fg='black', font=('serif',10, 'bold'))
    del_win_l2 = Label(del_win_s, text="Enter Book Name :", bg ='white', fg='black', font=('serif',10, 'bold'))
    del_win_l3 = Label(del_win_s, text="Enter Author Name :", bg ='white', fg='black', font=('serif',10, 'bold'))

    del_win_e1 = Entry(del_win_s, font=('serif', 10 , 'bold'), width = 36, bg='white')
    del_win_e2 = Entry(del_win_s, font=('serif', 10 , 'bold'), width = 36, bg='white')
    del_win_e3 = Entry(del_win_s, font=('serif', 10 , 'bold'), width = 36, bg='white')
    
    del_win_b1 = Button(del_win_s, text="Submit", width = 50 , height = 3, font=('serif', 10 , 'bold'), command = del_win_Delete)
    del_win_b2 = Button(del_win_s, text="Clear", width = 50 , height = 3, font=('serif', 10 , 'bold'), command = del_win_clr)

    del_win_e1.place(x = 160 , y = 130)
    del_win_e2.place(x = 160 , y = 190)
    del_win_e3.place(x = 160 , y = 250)
    
    del_win_b1.place(x = 20 , y = 330)
    del_win_b2.place(x = 20 , y = 410)
    
    del_win_l1.place(x = 19 , y = 130)
    del_win_l2.place(x = 19 , y = 190)
    del_win_l3.place(x = 19 , y = 250)
    
    del_win_ml.place(x = 110 , y = 25)
    del_win_s.mainloop()

############################################################################################# Operation 01 #############################################

def add_win():
    global add_win_e1, add_win_e2, add_win_e3, add_win_e4, add_win_e5, add_win_e6, add_win_e7

    def add_win_clr():
        a = str(add_win_e1.get())
        b = str(add_win_e2.get())
        c = str(add_win_e3.get())
        d = str(add_win_e4.get())
        e = str(add_win_e5.get())
        f = str(add_win_e6.get())
        g = str(add_win_e7.get(0.1, END))

        if(len(a)>0 or len(b)>0 or len(c)>0 or len(d)>0 or len(e)>0 or len(f)>0 or len(g)>0):
            add_win_e1.delete(0 , END)
            add_win_e2.delete(0 , END)
            add_win_e3.delete(0 , END)
            add_win_e4.delete(0 , END)
            add_win_e5.delete(0 , END)
            add_win_e6.delete(0 , END)
            add_win_e7.delete(0.1 , END)

    def add_win_db():
        d1 = datetime.now()
        a = str(add_win_e1.get())
        b = str(add_win_e2.get())
        c = str(add_win_e3.get())
        d = str(add_win_e4.get())
        e = str(add_win_e5.get())
        f = str(add_win_e6.get())
        g = str(add_win_e7.get(0.1, END))
        dy = str(d1.year)
        dm = str(d1.month)
        dd = str(d1.day)
        dh = str(d1.hour)
        dm = str(d1.minute)
        ds = str(d1.second)
        Book_id = dm+""+dy+""+dd+""+dm+""+dh+""+ds
        found = 0

        if(len(a)<=0 or len(b)<=0 or len(c)<=0 or len(d)<=0 or len(e)<=0 or len(f)<=0 or len(g)<=0):
            messagebox.showinfo(title='Error', message="You have not entered some details. Please fill the details... ")
        else:
            for i in coll_conn.find({},{'_id': 0}):
                if a == str(i['BookName'].encode('utf-8').decode('utf-8')) and b == str(i['Author'].encode('utf-8').decode('utf-8')) and d == str(i['Page'].encode('utf-8').decode('utf-8')): 
                    found+=1
                    
        if found > 0:
            messagebox.showinfo(message="your details are matched with some other id. Please try again")
        else:
            coll_conn.insert_one({'Bookid': Book_id,'BookName': a, 'Author': b, 'Price' : c , 'Page' : d, 'Language' : e, 'Category': f, 'Book_Description':g})
            messagebox.showinfo(message ="Your details are registered successfully...", title="Message")
    
    add_win_1 = Tk()
    add_win_1.title("Add your Details")
    add_win_1.geometry('500x730+500+20')
    add_win_1.config(background="white")
    add_win_1.resizable(width ="False", height = 'False')

    add_win_l1 = Label(add_win_1, text="Add Details", font=('serif', 29, 'bold'), bg='white')

    add_win_l2 = Label(add_win_1, text="Enter the Book Name", font=('serif', 11), bg='white')
    add_win_e1 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l3 = Label(add_win_1, text="Enter the Author Name", font=('serif', 11), bg='white')
    add_win_e2 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l4 = Label(add_win_1, text="Enter the book price", font=('serif', 11), bg='white')
    add_win_e3 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l5 = Label(add_win_1, text="Enter the total page", font=('serif', 11), bg='white')
    add_win_e4 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l6 = Label(add_win_1, text="Enter the Language", font=('serif', 11), bg='white')
    add_win_e5 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l7 = Label(add_win_1, text="Enter the category", font=('serif', 11), bg='white')
    add_win_e6 = Entry(add_win_1, font=('serif', 10), width = 40)

    add_win_l8 = Label(add_win_1, text="Enter About this book", font=('serif', 11), bg='white')
    add_win_e7 = Text(add_win_1, font=('serif', 10), width = 40, height = 4)

    add_win_b1 = Button(add_win_1, text ="Submit" ,font=('serif', 11, 'bold'), width =20 ,height =2 ,bg='black', fg='white', command = add_win_db)
    add_win_b2 = Button(add_win_1, text ="Clear" ,font=('serif', 11, 'bold'), width =20 ,height =2, bg='black', fg='white', command = add_win_clr)
    
    add_win_l1.place(x = 145 , y = 29)
    add_win_l2.place(x = 15 , y = 130)
    add_win_l3.place(x = 15 , y = 190)
    add_win_l4.place(x = 15 , y = 250)
    add_win_l5.place(x = 15 , y = 310)
    add_win_l6.place(x = 15 , y = 370)
    add_win_l7.place(x = 15 , y = 430)
    add_win_l8.place(x = 15 , y = 500)
    
    add_win_e1.place(x = 175 , y = 130)
    add_win_e2.place(x = 175 , y = 190)
    add_win_e3.place(x = 175 , y = 250)
    add_win_e4.place(x = 175 , y = 310)
    add_win_e5.place(x = 175 , y = 370)
    add_win_e6.place(x = 175 , y = 430)
    add_win_e7.place(x = 175 , y = 500)

    add_win_b1.place(x =50 , y = 610)
    add_win_b2.place(x =260 , y = 610)
    add_win_1.mainloop()

#####################################################################################Guest ########################
def log_1_view():
    log_1_view_w1 = Tk()
    log_1_view_w1.geometry('1350x500+50+130')
    log_1_view_w1.title("View Board")
    log_1_view_w1.resizable(height='false', width = 'false')
    log_1_view_w1.config(background = "white")
    log_1_view_l1 = Label(log_1_view_w1, text ="View Board", font =('serif', 25, 'bold'), bg ='white')
    x_scroll = Scrollbar(log_1_view_w1)
    y_scroll = Scrollbar(log_1_view_w1, orient= HORIZONTAL)
    y1 = 65
    for i in coll_conn.find({},{'_id' :0, 'Price':0, 'Page':0}):
        log_1_view_l2 = Label(log_1_view_w1, text = i, font =('serif', 10), bg ='white')
        log_1_view_l2.place(x = 0 , y = y1)
        y1 += 30
    log_1_view_l1.place(x = 600 , y =0)
    x_scroll.pack(side = RIGHT, fill = Y)
    y_scroll.pack(side = BOTTOM, fill = X)
#####################################################################################Admin#####################################

def admin_home():
    admin_home_f = Frame()
    admin_home_f.place(x = 0 , y = 0 , width = 720 , height = 400)
    admin_home_f.config(background="white")
    admin_home_f_b1 = Button(text="Add", font=('san', 15 ,'bold'), bg='#87366d', fg='white', width = 14 , height = 2, command = add_win)
    admin_home_f_b2 = Button(text="Update", font=('san', 15 ,'bold'), bg='#87366d', fg='white', width = 14 , height = 2, command = up_win)
    admin_home_f_b3 = Button(text="Delete", font=('san', 15 ,'bold'), bg='#87366d', fg='white', width = 14 , height = 2, command = del_win)
    admin_home_f_b4 = Button(text="Search", font=('san', 15 ,'bold'), bg='#87366d', fg='white', width = 14 , height = 2, command = ser_win)

    admin_home_f_l4 = Label(text="To add a new user hit the 'NEW USER' button", font=('serif' , 10, 'bold'),fg ='black', bg ='white')
    admin_home_f_b5 = Button(text="NEW USER", font=('serif',10, 'bold'), bg='black', fg='white', width = 20, command = new_user)
    admin_home_f_dl1 = Label(text= "Total Books:", font=('serif', 29), bg='white')

    j=0
    for i in coll_conn.find({},{'_id':1}):
        j+=1

    admin_home_f_dl2 = Label(text= j, font=('serif', 33,'bold'), bg='white')
    admin_home_f_dl2.place(x =320, y=178)    
    admin_home_f_dl1.place(x = 80, y = 180)
    admin_home_f_b1.place(x = 1 , y = 10)
    admin_home_f_b2.place(x = 180 , y = 10)
    admin_home_f_b3.place(x = 360 , y = 10)
    admin_home_f_b4.place(x = 540 , y = 10)
    admin_home_f_l4.place(x = 150 , y = 350)
    admin_home_f_b5.place(x = 450 , y = 348)

    

def log_1_check():
    a = str(log_1_f_e1.get())
    b = str(log_1_f_e2.get())
    found = 0
    if len(a)==0 or len(b)==0:
        messagebox.showinfo(title="Error", message ="fill the details...")
        
    for i in coll_conn_2.find({}):
        if a == str(i['user'].encode('utf-8').decode('utf-8')) and b == str(i['password'].encode('utf-8').decode('utf-8')):
                found +=1
        if found >0:
            admin_home()
        else:
            messagebox.showinfo(title="Error" , message ="you given data is not match...")
        
def log_1_clear():
    a = str(log_1_f_e1.get())
    b = str(log_1_f_e2.get())

    if(len(a)>0 or len(b)>0):
        log_1_f_e1.delete(0, END)
        log_1_f_e2.delete(0, END)

def log_1():
    global log_1_f_e1, log_1_f_e2
    log_1_f = Frame()
    log_1_f.place(x= 0 , y = 0 , width = 720 , height = 400)
    
    log_1_f.config(background = '#87366d')
    log_1_f_l1 = Label(log_1_f, text="Login" , font=('ink free',35 , 'bold'), bg = '#87366d', fg ='white')
    log_1_f_l2 = Label(log_1_f, text="Username" , font=('ink free',15, 'bold'), bg = '#87366d', fg ='white')
    log_1_f_e1 = Entry(log_1_f, font=('ink free', 12, 'bold'), bg = 'violet' , fg= 'black', width =25)
    log_1_f_l3 = Label(log_1_f, text="Password" , font=('ink free',15, 'bold'), bg = '#87366d', fg ='white')
    log_1_f_e2 = Entry(log_1_f, show="*", font=('ink free', 12, 'bold'), bg = 'violet' , fg= 'black', width =25)
    log_1_f_b1 = Button(log_1_f, text='Submit', font=('ink free', 10 , 'bold'), bg='black', fg='violet', width = 18 ,height = 2, command = log_1_check)
    log_1_f_b2 = Button(log_1_f, text='Clear', font=('ink free', 10 , 'bold'), bg='black', fg='violet', width = 18 ,height = 2, command = log_1_clear)

    log_1_f_lg = Label(log_1_f, text = "If you are a guest",
                       font=('ink free', 15 , 'bold'), bg ='#87366d' , fg ='white')

    log_1_f_lg2 = Label(log_1_f, text = "Hit the below button" ,
                       font=('ink free', 15 , 'bold'), bg ='#87366d' , fg ='white')

    log_1_f_gb = Button(log_1_f, text='Guest' ,width = 15, height = 2 , bg = 'black', fg='white', font=('ink free', 10, 'bold'), command = log_1_view)

    log_1_f_l1.place(x = 390, y = 30)
    log_1_f_l2.place(x = 300, y = 130)
    log_1_f_e1.place(x = 410 , y = 135)
    log_1_f_l3.place(x = 300, y = 195)
    log_1_f_e2.place(x = 410 , y = 200)
    log_1_f_b1.place(x = 320 , y = 280)
    log_1_f_b2.place(x = 500 , y = 280)

    log_1_f_gb.place(x = 90 , y = 240)

    log_1_f_lg.place(x = 55, y = 120)
    log_1_f_lg2.place(x = 50, y = 180)
    
    log_1_f.mainloop()

main_win = Tk()
main_win.title("My Book details...")
main_win.geometry('720x400+350+160')
main_win.config(background ='#87366d')
main_win.resizable(height ='false', width ='false')
main_win_l1 = Label(main_win, text="My Book Details", font=('ink free',50, 'bold'), bg='#87366d', fg ='white')
main_win_l2 = Label(main_win, text="This application provide a short details about my books", font=('ink free',13,'bold'), bg='#87366d', fg ='violet')
main_win_b1 = Button(main_win, text="Click here to start" , width = 25, height = 2 , font = ('ink free', 10 , 'bold'), bg = 'black' , fg = 'white', command = log_1)

main_win_l1.place(x = 120 , y =90)
main_win_l2.place(x = 130 , y = 180)
main_win_b1.place(x = 250 , y = 230)
main_win.mainloop()
