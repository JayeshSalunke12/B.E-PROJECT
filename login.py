import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('Login.png')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("message", "LogIn sucessfully")
            # ===========================================
            root.destroy()

           
            from subprocess import call
            call(['python','main.py'])
            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


#changes from here

#title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="black",fg="white")
#title.place(x=500,y=190,width=250)
        
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(x=800,y=200)
        
#logolbl=tk.Label(Login_frame, text="Login",bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=0,textvariable=username,font=("",15))
tk.Frame(Login_frame,width=220,height=2,bg='black').place(x=238,y=40)
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=0,textvariable=password,show="*",font=("",15))
tk.Frame(Login_frame,width=220,height=2,bg='black').place(x=238,y=70)
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(text="Login",command=login,width=35,border=0,pady=7,font=("Times new roman", 14, "bold"),bg="#57a1f8",fg="black").place(x=910,y=480)
#btn_log.grid(row=3,column=1,pady=10)

label=tk.Label(width=20,text="Don't have an account?", fg='black',bg='white',font=('Times new roman',14))
label.place(x=965,y=555)        
btn_reg=tk.Button(text="Sign up",command=registration,width=6,border=0,font=("Times new roman", 14, "bold"),bg="white",cursor='hand2',fg="#57a1f8").place(x=1200,y=550)
#btn_reg.grid(row=3,column=0,pady=10)
        
       

root.mainloop()