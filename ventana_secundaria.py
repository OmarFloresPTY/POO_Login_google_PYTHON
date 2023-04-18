import tkinter as tk
from random import choice
from datetime import datetime
from iterador_password import IteradorPasswordCreate
import pytz

class VentanaSecundaria():
    def __init__(self,user,parent):
        self.user = user
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("Create your user")
        self.window.iconbitmap("./ico/google.ico")
        self.window.configure(bg="white")
        self.window.geometry("360x410")
        self.label_h1 = tk.Label(self.window, text="Google",bg="white", font=("Arial",12,"bold"),anchor="w")
        self.label_h1.pack(fill="x",padx=10)
        self.label_h2 = tk.Label(self.window, text="Create your Google Account",bg="white", font=("Arial",14),anchor="w")
        self.label_h2.pack(fill="x",padx=10)

        self.frame_texbox_name_last_name = tk.Frame(self.window, bg="white")
        self.frame_texbox_name_last_name.pack(fill="x")
        self.texbox_name = tk.Entry(self.frame_texbox_name_last_name, font="Calibri 12",fg="grey")
        self.texbox_name.insert(0,"First Name")
        self.texbox_name.config(borderwidth=2,relief="solid")
        self.texbox_name.grid(row=0,column=0,padx=10, pady=20)
        self.texbox_last_name = tk.Entry(self.frame_texbox_name_last_name, font="Calibri 12",fg="grey")
        self.texbox_last_name.insert(0,"Last Name")
        self.texbox_last_name.config(borderwidth=2,relief="solid")
        self.texbox_last_name.grid(row=0,column=1,pady=20)

        self.frame_texbox_gmail = tk.Frame(self.window, bg="white")
        self.frame_texbox_gmail.pack(fill="x")
        self.texbox_gmail = tk.Entry(self.frame_texbox_gmail,width=42,font="Calibri 12",fg="grey")
        self.texbox_gmail.insert(0,"Username                                               @gmail.com")
        self.texbox_gmail.config(borderwidth=2,relief="solid")
        self.texbox_gmail.grid(row=0,column=0,padx=10)
        self.label_gmail = tk.Label(self.window,text="You can use letters, number & periods",bg="white",font="Arial 7",anchor="w")
        self.label_gmail.pack(fill="x",padx=10,pady=(0,20)) #Se le asigna la cantidad de espacios arriba y abajo del widget

        self.frame_password=tk.Frame(self.window, bg="white")
        self.frame_password.pack(fill="x")
        self.texbox_password = tk.Entry(self.frame_password,font="Calibri 12",fg="grey")
        self.texbox_password.insert(0, "Password")
        self.texbox_password.config(borderwidth=2,relief="solid")
        self.texbox_password.grid(row=0,column=0,padx=10)
        self.texbox_confirm_password = tk.Entry(self.frame_password,font="Calibri 12",fg="grey")
        self.texbox_confirm_password.insert(0, "Confirm")
        self.texbox_confirm_password.config(borderwidth=2,relief="solid")
        self.texbox_confirm_password.grid(row=0,column=1)

        self.label_password = tk.Label(self.window,text="Use 8 or more characters with a mix of letters, numbers & symbols",bg="white",font="Arial 7",anchor="w")
        self.label_password.pack(fill="x",padx=10)
        
        frame_btn_suggest = tk.Frame(self.window,bg="white")
        frame_btn_suggest.pack(fill="x")
        btn_suggest= tk.Button(frame_btn_suggest, text="Suggest Password",bg="white",fg="red",anchor="w",command=lambda: self.suggestions(frame_btn_suggest))
        btn_suggest.grid(row=0,column=0,padx=10,pady=10)
        self.check_password_var = tk.BooleanVar()
        self.check_password = tk.Checkbutton(self.window, text="Show password",bg="white",anchor="w",variable=self.check_password_var)
        self.check_password.pack(fill="x",padx=10,pady=5)

        self.frame_botton_end = tk.Frame(self.window,bg="white")
        self.frame_botton_end.pack(fill="x",pady=20)
        self.btn_back = tk.Button(self.frame_botton_end, text="Back",bg="white",fg="blue",command=self.on_closin)
        self.btn_create = tk.Button(self.frame_botton_end, text="Login",bg="blue",fg="white",command=self.insert_data)
        self.btn_back.grid(row=0,column=0,padx=10)
        self.btn_create.grid(row=0,column=1,padx=(170,0))
        self.window.protocol("WM_DELETE_WINDOW",self.on_closin)
        self.window.mainloop()

    def on_closin(self):
        self.window.destroy()
        self.parent.deiconify()
    
    
    def suggestions(self,frame):
        sets_password = []
        login_name, login_lastname = self.texbox_name.get(),self.texbox_last_name.get()
        suggestions_for_you = IteradorPasswordCreate(login_name,login_lastname,3)
        for password in suggestions_for_you:
            sets_password.append(password)
        sets_password = set(sets_password)
        label_suggest = tk.Label(frame,text=", ".join(str(x) for x in sets_password),bg="white", font=("Arial",8,"bold"),anchor="w")
        label_suggest.grid(row=1,column=0,padx=5)
            
        
    def insert_data(self):
        panama_timezone = pytz.timezone("America/Panama")
        panama_date = datetime.now(panama_timezone)
        if self.texbox_password.get() == self.texbox_confirm_password.get():
            self.user["Nombre"].append(self.texbox_name.get())
            self.user["Apellido"].append(self.texbox_last_name.get())
            self.user["Correo"].append(self.texbox_gmail.get())
            self.user["Contraseña"].append(self.texbox_password.get())
            self.user["Fecha_Creacion"].append("Panama: "+panama_date.strftime("%d/%m/%Y, %H:%M:%S"))
            print(self.user)
        else:
            print("Las contraseñas no coinciden, vuelva a intentarlo")
        