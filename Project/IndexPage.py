from tkinter import*
import subprocess,sys

def display1():
    p = subprocess.Popen(["PATH OF FILE-AUTOMATIC MODE"],stdout=sys.stdout)
    p.communicate()
def display2():
    p = subprocess.Popen(["PATH OF FILE-MANUAL MODE"],stdout=sys.stdout)
    p.communicate()

window=Tk()
window.title("Login")
window.geometry('900x700')
window.configure(background="lemon chiffon")
f=("Artifika",14)
f1=("Courier",24)

Login1Label=Label(window,text="Classroom Automation",font=("Artifika",40),fg="steel blue",bg="lemon chiffon")

LoginLabel=Label(window,text="Choose your option:",font=("Artifika",30),fg="steel blue",bg="lemon chiffon")

AutoLabel=Label(window,text="(It will put your system in Automatic Mode)",font=f,fg="medium sea green",bg="lemon chiffon")
AutoButton=Button(window,text="Automatic",fg="white",font=f1,bg="green yellow",command=display1)


ManLabel=Label(window,text="(It will put your system in Manual Mode)",font=f,fg="medium sea green",bg="lemon chiffon")
ManButton=Button(window,text="Manual",fg="white",font=f1,bg="green yellow",command=display2)

Login1Label.place(x=140,y=50)

LoginLabel.place(x=230,y=150)



AutoButton.place(x=350,y=280)
AutoLabel.place(x=230,y=360)
ManButton.place(x=350,y=470)
ManLabel.place(x=245,y=550)
AutoButton.config( height = 1, width = 10 )
ManButton.config( height = 1, width = 10 )
window.mainloop()
