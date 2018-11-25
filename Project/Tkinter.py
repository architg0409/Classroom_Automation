from tkinter import*
import subprocess,sys

def display():
    p = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Cm.ps1"],stdout=sys.stdout)
    p.communicate()

window=Tk()
window.title("Login")
window.geometry('900x700')
window.configure(background="lemon chiffon")
f=("Courier",14)

Login1Label=Label(window,text="Classroom Automation",font=("Courier",40),fg="green yellow",bg="lemon chiffon")

LoginLabel=Label(window,text="Enter Login Details:",font=("Courier",30),fg="green yellow",bg="lemon chiffon")

UserLabel=Label(window,text="Username :",font=f,fg="green",bg="lemon chiffon")
UserEntry=Entry(window,bg="azure",font=f,fg="green")

PassLabel=Label(window,text="Password :",font=f,fg="green",bg="lemon chiffon")
PassEntry=Entry(window,show="*",bg="azure",font=f,fg="green")

SubmitButton=Button(window,text="Submit",fg="white",font=f,bg="green",command=display)

Login1Label.place(x=160,y=50)

LoginLabel.place(x=210,y=150)

UserLabel.place(x=270,y=250)
PassLabel.place(x=270,y=300)

UserEntry.place(x=370,y=250)
PassEntry.place(x=370,y=300)

SubmitButton.place(x=400,y=380)

window.mainloop()
