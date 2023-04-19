import tkinter as tk
from ventana_secundaria import VentanaSecundaria
class VentanaPrincial:
    def __init__(self,user):
        self.user = user
        self.window = tk.Tk()
        self.window.title("Welcome to Google")
        self.window.iconbitmap("./ico/google.ico")
        self.window.configure(bg="white")
        self.window.geometry("400x370")
        self.label_h1 = tk.Label(self.window, text="Google", bg="white", font=("Arial",30,"bold"))
        self.label_h1.pack(fill=tk.X)
        self.frame = tk.Frame(self.window,background="white")
        self.label_h2 = tk.Label(self.frame, text="Sign In",bg="white",font=("calibri_font",15))
        self.label_h3 = tk.Label(self.frame, text="Use your Google Account",bg="white",font=("calibri_font",10))
        self.frame.pack(fill=tk.X,side=tk.TOP)
        self.label_h2.pack()
        self.label_h3.pack()
        self.user_frame = tk.Frame(self.window, bg="white")
        self.user_frame.pack(pady=20) 
        self.label_h4 = tk.Label(self.user_frame, text="Forgot User?", bg="white",fg="blue",font="calibri_font 10")
        self.label_h4.grid(row=2,column=1)
        self.texBox_login_user = tk.Entry(self.user_frame, width=35, font="Calibri 13", fg='grey')
        self.texBox_login_user.insert(0,"Email or Phone")
        self.texBox_login_user.config(borderwidth=2,relief="solid")
        self.texBox_login_user.grid(row=1, column=1, pady=15)
        self.label_h5 = tk.Label(self.window, text="Not your computer? Use Guest mode to sign in privately.", bg="white",font=("Arial",10))
        self.label_h5.pack()
        self.label_h6 = tk.Label(self.window, text="Learn more", bg="white",fg="blue",font=("calibri_font",10))
        self.label_h6.pack()
        self.frame_btn = tk.Frame(self.window,background="white")
        self.frame_btn.pack(pady=20)
        self.btn_create_account = tk.Button(self.frame_btn, text="Create account",bg="white",fg="blue",command=self.open_window)
        self.btn_next = tk.Button(self.frame_btn, text="Next",relief="raised",bg="blue",fg="white",command= self.verify_user)
        self.btn_create_account.pack(side=tk.LEFT,padx=20)
        self.btn_next.pack(side=tk.LEFT,padx=40)
        self.window.mainloop()

    def verify_password(self):
        password = self.user["Contraseña"]
        if self.ban == True:
            if self.texBox_password.get() in password:
                print("La Contraseña es correcta! Bienvenido ",self.texBox_login_user.get())
            else:
                print("Olvidaste tú contraseña?")

    def verify_user(self):
        correos = self.user["Correo"]
        if self.texBox_login_user.get() in correos:
            print(self.texBox_login_user.get())
            self.texBox_password = tk.Entry(self.user_frame, width=35, font="Calibri 13", fg='grey')
            self.texBox_password.insert(0,"Password")
            self.texBox_password.config(borderwidth=2,relief="solid")
            self.texBox_password.grid(row=2, column=1, pady=15)
            self.btn_next.destroy()
            self.btn_login = tk.Button(self.frame_btn, text="Login",relief="raised",bg="blue",fg="white",command= self.verify_password)
            self.btn_login.pack(side=tk.LEFT,padx=40)
            self.ban = True
            return self.ban
        else:
            self.ban = False
            print("No se encuentra en la base de datos.")
            return self.ban
    
    def open_window(self):
        self.window.withdraw()
        ventana_secundaria = VentanaSecundaria(self.user,self.window)
    