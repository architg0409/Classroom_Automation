from tkinter import*
import subprocess,sys

window=Tk()
window.title("Classroom Automation")
window.geometry('900x700')
frame1=Frame(window,height=700,width=900,bg="lemon chiffon")
frame2=Frame(window,height=700,width=900,bg="lemon chiffon")
frame3=Frame(window,height=700,width=900,bg="lemon chiffon")
f=("Artifika",20)
f1=("Artifika",24)


def Automatic():
    print("Hello")

def On():
    p = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Documents\\GitHub\\Classroom_Automation\\Project\\Cm.ps1"], stdout=sys.stdout)
    p.communicate()

def Off():
    q = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Documents\\GitHub\\Classroom_Automation\\Project\\Cm.ps1"], stdout=sys.stdout)
    q.communicate()

def Manual():
    frame2.destroy()
    Login1Label=Label(frame3,text="Classroom Automation",font=("Artifika",43),fg="steel blue",bg="lemon chiffon")

    Login2Label=Label(frame3,text="Welcome to Manual System",font=("Artifika",35),fg="steel blue",bg="lemon chiffon")


    LoginLabel=Label(frame3,text="Choose to Turn-on OR Turn-off:",font=("Artifika",28),fg="steel blue",bg="lemon chiffon")

    TurnOnButton=Button(frame3,text="Turn-ON",fg="white",font=f,bg="green",command=On)

    TurnOffButton=Button(frame3,text="Turn-OFF",fg="white",font=f,bg="green",command=Off)


    frame3.pack()
    
    Login1Label.place(x=123,y=30)

    Login2Label.place(x=130,y=120)

    LoginLabel.place(x=150,y=250)
    

    TurnOnButton.place(x=230,y=350)

    TurnOffButton.place(x=500,y=350)
    

def Login():
    frame1.destroy()
    LoginLabela=Label(frame2,text="Classroom Automation",font=("Artifika",40),fg="steel blue",bg="lemon chiffon")

    LoginLabelb=Label(frame2,text="Enter Login Details",font=("Artifika",30),fg="steel blue",bg="lemon chiffon")

    UserLabel=Label(frame2,text="Username",font=f,fg="green",bg="lemon chiffon")
    UserEntry=Entry(frame2,bg="azure",font=f,fg="green")

    PassLabel=Label(frame2,text="Password",font=f,fg="green",bg="lemon chiffon")
    PassEntry=Entry(frame2,show="*",bg="azure",font=f,fg="green")

    SubmitButton=Button(frame2,text="Submit",fg="white",font=f,bg="green",command=Manual)

    frame2.pack() 
    
    LoginLabela.place(x=160,y=50)

    LoginLabelb.place(x=250,y=150)

    UserLabel.place(x=220,y=250)
    PassLabel.place(x=220,y=300)

    UserEntry.place(x=370,y=250)
    PassEntry.place(x=370,y=300)

    SubmitButton.place(x=400,y=380)
def Home():
    
    Login1Label=Label(frame1,text="Classroom Automation",font=("Artifika",40),fg="steel blue",bg="lemon chiffon")
    LoginLabel=Label(frame1,text="Choose your option:",font=("Artifika",30),fg="steel blue",bg="lemon chiffon")

    AutoLabel=Label(frame1,text="(It will put your system in Automatic Mode)",font=f,fg="medium sea green",bg="lemon chiffon")
    AutoButton=Button(frame1,text="Automatic",fg="white",font=f1,bg="green",command=Automatic)


    ManLabel=Label(frame1,text="(It will put your system in Manual Mode)",font=f,fg="medium sea green",bg="lemon chiffon")
    ManButton=Button(frame1,text="Manual",fg="white",font=f1,bg="green",command=Login)

    frame1.pack()
    
    Login1Label.place(x=160,y=50)

    LoginLabel.place(x=260,y=150)



    AutoButton.place(x=350,y=280)
    AutoLabel.place(x=190,y=360)
    ManButton.place(x=350,y=470)
    ManLabel.place(x=200,y=550)
    AutoButton.config( height = 1, width = 10 )
    ManButton.config( height = 1, width = 10 )

    
Home()

window.mainloop()
