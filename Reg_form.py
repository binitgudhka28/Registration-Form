from tkinter import *
import csv
from tkinter import messagebox
root = Tk()
root.title("Registration Form")
root.geometry("500x500")
def click_submit_button():
    country_selected=temp.get()
    gender = var.get()
    if(gender==1):
        gender_select ="Male"
    elif (gender == 2):
        gender_select ="Female"
    else:
        gender_select="Other"
    # 0 -false
    # 1 - True
    if java_checked.get() and python_checked.get():
        language_selected = "Java,Python"
    elif java_checked.get():
        language_selected="Java"
    elif python_checked.get():
        language_selected="Python"
    else:
        language_selected="No language Selected"

    uservalues="\n"+full_name_entry_text.get()+"\n"+Email_entry_text.get() +"\n"+ gender_select +"\n"+ country_selected +"\n"+ language_selected
    f=open("bdivreg.txt",'a')
    f.write(uservalues)
    f.close()
    with open("bdivregdetails.csv","a")as fs:
        w =csv.writer(fs,dialect='excel')
        all=([full_name_entry_text.get(),Email_entry_text.get(),gender_select,country_selected,language_selected])
        w.writerow(all)
        fs.close()
    if full_name_entry_text.get() == " " or Email_entry_text.get()==" ":
        messagebox.showerror("Empty Fields", "Blank fields not allowed")
    else:
        messagebox.showinfo("Form Submission", "Form Submitted Successfully")

#Registration
Registration_formlabel=Label(root,text="Registration Form")
Registration_formlabel.place(x=130,y=40)
Registration_formlabel["font"]=("bold",25)

#full name

full_name_label=Label(root,text="Full Name")
full_name_label.place(x=100,y=120)
full_name_entry_text=Entry(root)
full_name_entry_text.place(x=210,y=120)
#Email

Email_label=Label(root,text="Email")
Email_label.place(x=100,y=165)
Email_entry_text=Entry(root)
Email_entry_text.place(x=210,y=165)

#Geender
var=IntVar()
Gender_label=Label(root,text="Gender")
Gender_label.place(x=98,y=220)
Male_radiobutton=Radiobutton(root,text="Male",padx=1,value=1,variable=var)
Male_radiobutton.place(x=200,y=220)
Female_radiobutton=Radiobutton(root,text="Female",padx=20,value=2,variable=var)
Female_radiobutton.place(x=270,y=220)

#Country
country_label = Label(root, text="Country")
country_label.place(x=98,y=265)
temp = StringVar()
countries=["India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Pakistan","Palestine","PapuaNewGuinea","Paraguay","Peru","Philippines","Poland","portugal"]
country_optionmenu=OptionMenu(root,temp,*countries)
country_optionmenu.place(x=200,y=258)
temp.set("Choose your Country")

#Programming
java_checked=IntVar()
Programming_label=Label(root,text="Programming")
Programming_label.place(x=98,y=310)


java_checkbutton=Checkbutton(root,text="Java",padx=7,onvalue=1,offvalue=0,variable=java_checked)
java_checkbutton.place(x=200,y=310)
python_checked=IntVar()

python_checkbutton=Checkbutton(root,text="Python",padx=7,onvalue=1,offvalue=0,variable=python_checked)
python_checkbutton.place(x=285,y=310)
#Submit
submit_button=Button(root,text="Submit",command=click_submit_button)
submit_button.place(x=165,y=360)
submit_button["width"]=15
submit_button["bg"]="#bd3a0d"
root.mainloop()