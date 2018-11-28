from tkinter import*
import subprocess,sys

def On():
    p = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Documents\\GitHub\\Classroom_Automation\\Project\\LightOn.ps1"], stdout=sys.stdout)
    p.communicate()

def Off():
    q = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Documents\\GitHub\\Classroom_Automation\\Project\\LightOff.ps1"], stdout=sys.stdout)
    q.communicate()

window=Tk()
window.title("Login")
window.geometry('900x700')
window.configure(background="lemon chiffon")
f=("Artifika",20)

Login1Label=Label(window,text="Classroom Automation",font=("Artifika",43),fg="steel blue",bg="lemon chiffon")

Login2Label=Label(window,text="Welcome to Manual System",font=("Artifika",35),fg="steel blue",bg="lemon chiffon")


LoginLabel=Label(window,text="Choose to Turn-on OR Turn-off:",font=("Artifika",28),fg="steel blue",bg="lemon chiffon")

TurnOnButton=Button(window,text="Turn-ON",fg="white",font=f,bg="green",command=On)

TurnOffButton=Button(window,text="Turn-OFF",fg="white",font=f,bg="green",command=Off)


Login1Label.place(x=123,y=30)

Login2Label.place(x=130,y=120)

LoginLabel.place(x=150,y=250)




TurnOnButton.place(x=230,y=350)

TurnOffButton.place(x=500,y=350)



window.mainloop()
