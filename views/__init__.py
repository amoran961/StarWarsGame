from tkinter import *
import game.startgame
import services.Service
import game.constants as c
bgclr = "#282828"
fgclr = "#cecece"
clr = '#004a95'


def login(user_Entry, password_Entry, w, warn):
    log = services.Service.ServiceLogin().login(user_Entry.get(), password_Entry.get())
    users = [("dilip", "python")]
    if (log == True):
        c.USER = user_Entry.get()
        w.destroy()
        game.startgame.start_game()
    else:
        warn.config(text="Usuario y/o contraseña incorrecta", fg="red")

def register(user_Entry, password_Entry, w, warn):
    log = services.Service.ServiceLogin().register(user_Entry.get(), password_Entry.get())
    users = [("dilip", "python")]
    if (log == True):
      loginWindow()
    else:
        warn.config(text="Ocurrió un problema, intente luego", fg="red")


def loginWindow():
    button = Button(w,
                    text="Login",
                    bg=clr,
                    fg="white",
                    relief=GROOVE,
                    highlightcolor=clr,
                    highlightthickness=4,
                    width=40,
                    font=10,
                    command=lambda: login(user_Entry, password_Entry, w, warn))
    button.place(x=20, y=240)
    buttonR = Button(w,
                     text="Registrar",
                     bg="#228B22	",
                     fg="white",
                     relief=GROOVE,
                     highlightcolor=clr,
                     highlightthickness=0,
                     width=10,
                     font=10,
                     command=lambda:registerWindow())
    buttonR.place(x=20, y=300)

def registerWindow():
    button = Button(w,
                    text="Registrar",
                    bg=clr,
                    fg="white",
                    relief=GROOVE,
                    highlightcolor=clr,
                    highlightthickness=4,
                    width=40,
                    font=10,
                    command=lambda: register(user_Entry, password_Entry, w, warn))
    button.place(x=20, y=240)

    buttonR = Button(w,
                     text="Login",
                     bg="#228B22",
                     fg="white",
                     relief=GROOVE,
                     highlightcolor=clr,
                     highlightthickness=0,
                     width=10,
                     font=10,
                     command=lambda: loginWindow())
    buttonR.place(x=20, y=300)



w = Tk()

ws = w.winfo_screenwidth()  # width of the screen
hs = w.winfo_screenheight()  # height of the screen
wi = 450  # width for the Tk root0
hi = 350  # height for the Tk root

x = (ws / 2) - (wi / 2)
y = (hs / 2) - (hi / 2)

w.title("Star Wars")
w.geometry('%dx%d+%d+%d' % (wi, hi, x, y))

w.config(bg=bgclr)
w.resizable()

user = Label(w,
             text="User",
             font=("blod", 15),
             bg=bgclr,
             fg=fgclr)
user.place(x=20, y=40)

user_Entry = Entry(w, bg=bgclr,
                   fg="white",
                   relief=GROOVE,
                   highlightcolor="white",
                   highlightthickness=2,
                   highlightbackground=clr,
                   width=40,
                   font=10,
                   bd=5)
user_Entry.place(x=20, y=80)

password = Label(w,
                 text="Password",
                 font=("blod", 15),
                 bg=bgclr,
                 fg=fgclr)
password.place(x=20, y=120)

password_Entry = Entry(w, bg=bgclr,
                       fg="white",
                       relief=GROOVE,
                       highlightcolor="white",
                       highlightthickness=2,
                       highlightbackground=clr,
                       width=40,
                       font=10,
                       show="*",
                       bd=5)
password_Entry.place(x=20, y=160)

warn = Label(w,
             font=("blod", 10),
             bg=bgclr)

warn.place(x=80, y=200)
loginWindow()
w.mainloop()



