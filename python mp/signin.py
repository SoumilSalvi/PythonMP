from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#FUNCTIONALITY PART


def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Somu@sql',database='userdata')
            mycursor = con.cursor()
            query ='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s' 
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))   
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset ,please login with new password',parent=window)
                window.destroy()
            
    window=Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window,image=bgPic)
    bglabel.grid()

    heading_label = Label(window,text='RESET PASSWORD',font=('arial','18','bold')
                                           ,bg ='white',fg ='blue')
    heading_label.place(x=480,y=60)

    userLabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='blue')
    userLabel.place(x=470,y=130)

    user_entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='skyblue')
    user_entry.place(x=470,y=160)

    Frame(window,width=250,height=2,bg='skyblue').place(x=470,y=180)

    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='blue')
    passwordLabel.place(x=470,y=210)

    newpass_entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='skyblue')
    newpass_entry.place(x=470,y=240)

    Frame(window,width=250,height=2,bg='skyblue').place(x=470,y=260)

    confirmpassLabel=Label(window,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='blue')
    confirmpassLabel.place(x=470,y=290)

    confirmpass_entry=Entry(window,width=25,font=('arial',11,'bold'),bd=0,fg='skyblue')
    confirmpass_entry.place(x=470,y=320)

    Frame(window,width=250,height=2,bg='skyblue').place(x=470,y=340)

    submitButton=Button(window,text='Submit',font=('Open Sans',16,'bold'),
                   fg='white',bg='skyblue',activeforeground='white'
                   ,activebackground='skyblue',cursor='hand2',bd=0,width=19
                   ,command=change_password)
    submitButton.place(x=470,y=390)

   


    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
         con=pymysql.connect(host='localhost',user='root',password='Somu@sql')
         mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection not established try again')
            return
        
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is successful')    

        


def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)        

#GUI PART

login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')
                                           ,bg ='white',fg ='firebrick1')
heading.place(x=605,y=120)


usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg ='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)


passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg ='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)


frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),
                 fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715,y=295)


loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white'
                   ,activebackground='firebrick1',cursor='hand2',bd=0,width=19
                   ,command=login_user)
loginButton.place(x=578,y=350)


orLabel=Label(login_window,text='---------------OR---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,  image= google_logo ,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new account',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='white'
                   ,activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)


login_window.mainloop()