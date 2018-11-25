import subprocess, sys
i=int(input("Enter"))
if i>0:
    p = subprocess.Popen(["powershell.exe","C:\\Users\\lenovo\\Cm.ps1"], stdout=sys.stdout)
    p.communicate()
else:
    print("You entered less than Zero")
