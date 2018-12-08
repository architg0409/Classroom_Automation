from tkinter import*                 #GUI Module
import mysql.connector               #Database Module
from tkinter import messagebox       #Warning Messages 
import datetime                      #Date And Time Module
import serial                        #Serialization Module



#Switching Relay On
def On():
    Arduino_Serial.write(b'1')
    


#Switching Relay Off
def Off():
    Arduino_Serial.write(b'0')



#Automatic
def Automatic():
    day=datetime.datetime.today().weekday()
    
    currentTime=datetime.datetime.now()
    minute=currentTime.strftime("%M")
    
    for i in range(0,9):
            minute2=list(str(result[i][1]).split(":"))[1]
            if minute2==minute:
                res=result[i][day+2]
                if res==0:
                    print("Light is Switched Off")
                    Off()
                elif res==1:
                    print("Light is Switched On")
                    On()
                    
    AutoButton.after(10000,Automatic)
    
    


#Checking Valid Users    
def Database_Check():
    UserName=UserEntry.get()
    Password=PassEntry.get()
    
    try:
        cursor.execute("select * from users")
        result = cursor.fetchall()
        flag=0
        for users in result:
            if(users[1]==UserName and users[2]==Password):
                flag=1
                Manual()
                break
        if flag==0:
            messagebox.showwarning("Warning","No User with such Credentials")
            
    except:
        pass



#Manual Frame Function
def Manual():
    frame2.pack_forget()
    
    
    Login1Label=Label(frame3,text="Classroom Automation",font=("Roboto",43),fg="steel blue",bg="lemon chiffon")
    Login2Label=Label(frame3,text="Welcome to Manual System",font=("Roboto",35),fg="steel blue",bg="lemon chiffon")
    LoginLabel=Label(frame3,text="Choose to Turn-on or Turn-off:",font=("Roboto",28),fg="steel blue",bg="lemon chiffon")


    TurnOnButton=Button(frame3,text="Turn-ON",fg="white",font=f,bg="green",command=On)
    TurnOffButton=Button(frame3,text="Turn-OFF",fg="white",font=f,bg="green",command=Off)
    

    CheckBox402=Checkbutton(frame3, text="Room No.-402",font=f,bg="lemon chiffon",fg="steel blue")
    CheckBox405=Checkbutton(frame3, text="Room No.-405",font=f,bg="lemon chiffon",state=DISABLED)
    CheckBox420=Checkbutton(frame3, text="Room No.-420",font=f,bg="lemon chiffon",state=DISABLED)
    CheckBox423=Checkbutton(frame3, text="Room No.-423",font=f,bg="lemon chiffon",state=DISABLED)
    CheckBox418=Checkbutton(frame3, text="Room No.-418",font=f,bg="lemon chiffon",state=DISABLED)


    Logout=Button(frame3,text="Logout",fg="black",font=("Roboto",10),bg="firebrick1",command=Home)
    

    frame3.pack()

    
    CheckBox402.place(x=630,y=450)
    CheckBox405.place(x=630,y=500)
    CheckBox420.place(x=630,y=550)
    CheckBox423.place(x=630,y=600)
    CheckBox418.place(x=630,y=650)
    
    
    Login1Label.place(x=423,y=30)
    Login2Label.place(x=430,y=120)
    LoginLabel.place(x=450,y=250)
    

    TurnOnButton.place(x=530,y=350)
    TurnOffButton.place(x=800,y=350)

    
    Logout.place(x=1470,y=10)



#Login Frame Function
def Login():

    global UserEntry,PassEntry

    frame1.pack_forget()

    
    LoginLabela=Label(frame2,text="Classroom Automation",font=("Roboto",40),fg="steel blue",bg="lemon chiffon")
    LoginLabelb=Label(frame2,text="Enter Login Details",font=("Roboto",30),fg="steel blue",bg="lemon chiffon")


    UserLabel=Label(frame2,text="Username",font=f,fg="green",bg="lemon chiffon")
    PassLabel=Label(frame2,text="Password",font=f,fg="green",bg="lemon chiffon")


    SubmitButton=Button(frame2,text="Submit",fg="white",font=f,bg="green",command=Database_Check)
    

    frame2.pack()
    
    
    LoginLabela.place(x=460,y=70)
    LoginLabelb.place(x=550,y=220)


    UserLabel.place(x=520,y=320)
    PassLabel.place(x=520,y=370)
    

    UserEntry.place(x=670,y=320)
    PassEntry.place(x=670,y=370)
    

    SubmitButton.place(x=700,y=450)

    

#Home Frame Function    
def Home():

    frame3.pack_forget()

    global AutoButton
    
    
    Login1Label=Label(frame1,text="Classroom Automation",font=("Roboto",40),fg="steel blue",bg="lemon chiffon")
    LoginLabel=Label(frame1,text="Choose your option:",font=("Roboto",30),fg="steel blue",bg="lemon chiffon")

    AutoLabel=Label(frame1,text="(It will put your system in Automatic Mode)",font=f,fg="medium sea green",bg="lemon chiffon")
    ManLabel=Label(frame1,text="(It will put your system in Manual Mode)",font=f,fg="medium sea green",bg="lemon chiffon")


    ManButton=Button(frame1,text="Manual",fg="white",font=f1,bg="green",command=Login)


    frame1.pack()
    

    Login1Label.place(x=460,y=50)
    LoginLabel.place(x=560,y=150)


    AutoButton.place(x=650,y=280)
    ManButton.place(x=650,y=470)

    
    AutoLabel.place(x=490,y=360)
    ManLabel.place(x=500,y=550)

    
    AutoButton.config( height = 1, width = 10 )
    ManButton.config( height = 1, width = 10 )

    
    Automatic()



window=Tk()                               #Initializing Tkinter Window

window.title("Classroom Automation")      #Setting Title

width_value=window.winfo_screenwidth()
height_value=window.winfo_screenheight()


window.geometry('%dx%d+0+0'%(width_value,height_value))


frame1=Frame(window,height=height_value,width=width_value,bg="lemon chiffon")
frame2=Frame(window,height=height_value,width=width_value,bg="lemon chiffon")
frame3=Frame(window,height=height_value,width=width_value,bg="lemon chiffon")


f=("Roboto",20)
f1=("Roboto",24)


UserEntry=Entry(frame2,bg="azure",font=f,fg="green")
PassEntry=Entry(frame2,show="*",bg="azure",font=f,fg="green")


AutoButton=Button(frame1,text="Automatic",fg="white",font=f1,bg="green",command=Automatic)


Arduino_Serial = serial.Serial(port='COM4',baudrate=9600)    #Setting Arduino Serial Port



#Database Connection
try:
    con = mysql.connector.connect(user='root',password='architgupta97',host='localhost',database='timeslotsdb')
    cursor = con.cursor()
    cursor.execute("select * from time1")
    result=cursor.fetchall()
except:
    pass


    
Home()        #Calling Home Frame Function



window.mainloop()
