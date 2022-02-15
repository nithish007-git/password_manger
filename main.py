from tkinter import *
from tkinter import messagebox
import pyperclip
import json
window=Tk()
#hackerfeast

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    a=  random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    entry_pass.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    newdata={
        entry1.get():{
          "email": entry_email.get(),
          "passw":entry_pass.get()


        }
    }

    if len(entry1.get())==0 or len(entry_pass.get())==0 :
        messagebox.showerror(title="OOPS",message="please dont leave the fileds empty")
    else:
        try:

            with open("data.json", "r") as file:
                data12= json.load(file)

        except(FileNotFoundError,json.JSONDecodeError):
            with open("data.json","w") as data_file:
                json.dump(newdata, data_file, indent=4)
        else:
                data12.update(newdata)
                with open("data.json", "w") as data_file:
                     json.dump(data12, data_file, indent=4)

        finally:
              clear()


def clear():
    entry1.delete(0,"end")
    entry_pass.delete(0,"end")
def find_pass():

     website=entry1.get()
     try:
          with open("data.json") as file:
              data=json.load(file)
              pass
     except (FileNotFoundError,json.decoder.JSONDecodeError):
         messagebox.showerror(title="Error",message="no data file found")
     else:
         if website in data:
             data2 = data[website]["email"]
             data_pass1 = data[website]["passw"]
             messagebox.showinfo(title=website, message=f"email : {data2} \n password:{data_pass1}")
             pyperclip.copy(data_pass1)









# ---------------------------- UI SETUP ------------------------------- #
window.title("password manager")
window.config(width=600,height=500)
window.config(bg="black")
#canvas
canvas=Canvas(width=300,height=400,bg="black",highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100,190,image=img)
canvas.grid(column=2,row=2,padx=10,pady=10)

#website label
label_web=Label(text="Website:",font=("arial",20,),highlightthickness=0,fg="white",bg="black")
label_web.grid(column=1,row=3,pady=4,padx=4)

#entry-web
entry1=Entry(width=35,highlightthickness=0,fg="black")
entry1.grid(column=2,row=3,columnspan=2)
entry1.focus()
#emails

label_email=Label(text="Email:",font=("arial",20,),highlightthickness=0,fg="white",bg="black")
label_email.grid(column=1,row=4,pady=4,padx=4)
#entrylabel(email)
entry_email=Entry(width=35,highlightthickness=0,fg="black")
entry_email.grid(column=2,row=4,columnspan=2)
entry_email.insert(0,"nithish3604@gmail.com")
#password
label_pass=Label(text="Password:",font=("arial",20),highlightthickness=0,fg="white",bg="black")
label_pass.grid(column=1,row=5,pady=10,padx=10)

#entry
entry_pass=Entry(width=35,highlightthickness=0)
entry_pass.grid(column=2,row=5,columnspan=2)

#button
button=Button(text="Genertate",width=10,highlightthickness=0,fg="black",command=password)
button.grid(column=3,row=5,sticky=EW,pady=10,padx=7)
#add button
button1=Button(text="Add",width=10,highlightthickness=0,fg="black",command=save_pass)
button1.grid(column=2,row=6,padx=20,pady=20,columnspan=2,sticky=EW)
#search button
button2=Button(text="search",width=10,fg="black",command=find_pass)
button2.grid(column=3,row=3)
window.mainloop()