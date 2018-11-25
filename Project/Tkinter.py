from tkinter import*
import subprocess,sys

def display():
    p = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Cm.ps1"], stdout=sys.stdout)
    p.communicate()

window=Tk()
window.title("Login")
window.geometry('900x700')
window.configure(background="lemon chiffon")
f=("Courier",14)

LoginLabel=Label(window,text="Enter Login Details",font=("Courier",40),fg="green yellow",bg="lemon chiffon")

UserLabel=Label(window,text="Username :",font=f,fg="green",bg="lemon chiffon")
UserEntry=Entry(window,bg="azure",font=f,fg="green")

PassLabel=Label(window,text="Password :",font=f,fg="green",bg="lemon chiffon")
PassEntry=Entry(window,show="*",bg="azure",font=f,fg="green")

SubmitButton=Button(window,text="Submit",fg="white",font=f,bg="green",command=display)

LoginLabel.place(x=170,y=100)

UserLabel.place(x=250,y=220)
PassLabel.place(x=250,y=270)

UserEntry.place(x=370,y=220)
PassEntry.place(x=370,y=270)

SubmitButton.place(x=350,y=330)

window.mainloop()
