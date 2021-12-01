print("Hello World")
a=10
print(a)
name="Sahas"
print(name)
print(type(a))
print(type(name))
colors=["red","orange","yellow","green","blue","purple","pink","7 colors of the rainbow","Sahas made this var"]
print(colors)
print(type(colors))
from tkinter import*
root=Tk()
root.title("Driver's Liscense")
root.geometry("300x400")
heading=Label(root,text="Driver's Liscense")
heading.pack()

label_name=Label(root)

label_birthday=Label(root)

label_age=Label(root)

label_allowed=Label(root)

def mycarddetails():
    name="Sahas R. Etikyala"
    
    age=11  
    
    label_name["text"]=name
    
    label_birthday["text"]=" Born on 7/9/2010"
    
    label_age["text"]=str(age)+"yrs old"
    
    label_allowed["text"]="4 wheeler, 2wheeler"

button_details=Button(root,text="Show Details",command=mycarddetails)
button_details.pack()
label_name.pack()
label_birthday.pack()
label_age.pack()
label_allowed.pack()
root.mainloop()

