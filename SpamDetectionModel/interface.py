from tkinter import *
from tkinter import messagebox
from re import fullmatch
from SpamDetectionModel import QueryTransformation,Predict
import pickle

def main():
    root = Tk()
    root.resizable(0, 0)
    app = LoginWindow(root)
    root.mainloop()


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.username = ''
        self.password = ''
        self.master.title('Spam Detection System')
        self.master.geometry('500x320+300+300')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.labelTitle = Label(self.frame, text='Login Form', font=('Bookman Old Style', 20, 'bold'), bd=1)
        self.labelTitle.grid(row=0, column=0, columnspan=1, pady=20)

        self.loginFrame = Frame(self.frame, bd=5, relief='ridge')
        self.loginFrame.grid(row=1, column=0)

        # =============================================================
        self.lablusername = Label(self.loginFrame, width=8, text='Email:',
                                  font=('Bookman Old Style', 12, 'bold'))
        self.lablusername.grid(row=0, column=0, columnspan=1, pady=15, padx=5, sticky=E)
        self.name = self.entusername = Entry(self.loginFrame, width=25,
                                             font=('Bookman Old StyleBookman Old Style', 10))
        self.entusername.grid(row=0, column=1, padx=20)

        self.lablusername = Label(self.loginFrame, width=10, text='Password: ',
                                  font=('Bookman Old StyleBookman Old Style', 12, 'bold'))
        self.lablusername.grid(row=1, column=0, columnspan=1, pady=15, padx=7)
        self.passw = self.entusername = Entry(self.loginFrame, width=25, font=('*', 10))
        self.entusername.grid(row=1, column=1, padx=20)

        self.ckkeepsign = Checkbutton(self.loginFrame, text='keep me signe In')

        self.ckkeepsign.grid(row=2, column=1)
        # =============================================================

        # buttons block
        self.loginFrame2 = Frame(self.frame, relief='ridge')
        self.loginFrame2.grid(row=2, column=0)
        self.lblerrorMsg = Label(self.loginFrame2, state=DISABLED, text='**invalid username or password',
                                 font=('Bookman Old Style', 8, 'bold'), fg='red')
        self.lblerrorMsg.grid(row=0, column=0)

        self.btnLogin = Button(self.loginFrame2, text='register', state=DISABLED,
                               font=('Bookman Old Style', 10, 'bold'), width=10, command=self.registerUser)
        self.btnLogin.grid(row=1, column=0)
        self.btnLogin = Button(self.loginFrame2,
                               text='login', font=('Bookman Old Style', 10, 'bold'), width=10, bg='green',
                               command=self.loginSystem)
        self.btnLogin.grid(row=1, column=1, pady=7)

    def loginSystem(self):
        if str(type(self.name)) == '''<class 'tkinter.Entry'>''':
            self.username = self.name.get()
            self.password = self.passw.get()
            valid = fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", self.username)

            if valid != None and self.password:
                self.master.wm_state('iconic') #it will minimize the login window
                self.openW = Toplevel()
                self.app = EmailWindow(self.openW, self.username)

            else:
                self.lblerrorMsg.config(state=NORMAL)

    def registerUser(self):
        pass


class EmailWindow:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.master.title('Spam Detection System')
        self.master.geometry('700x550+300+300')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.labelTitle = Label(self.frame, text='Sent Mail', font=('Bookman Old Style', 20, 'bold'), bd=1)
        self.labelTitle.grid(row=0, column=0, columnspan=1, pady=20)

        self.mailFrame = Frame(self.frame, bd=5, relief='ridge')
        self.mailFrame.grid(row=1, column=0)

        # =============================================================
        self.lablusername = Label(self.mailFrame, width=8, text='From:',
                                  font=('Bookman Old Style', 12, 'bold'))
        self.lablusername.grid(row=0, column=0, columnspan=1, pady=15, padx=5, sticky=W)
        self.name = self.entusername = Label(self.mailFrame, width=25, text=self.user, state=DISABLED,
                                             font=('Bookman Old StyleBookman Old Style', 10))
        self.entusername.grid(row=0, column=1, padx=20)

        self.lablTo = Label(self.mailFrame, width=10, text='To: ',
                            font=('Bookman Old StyleBookman Old Style', 12, 'bold'))
        self.lablTo.grid(row=1, column=0, columnspan=1, pady=15, padx=7)
        self.EnReciver = self.entusername = Entry(self.mailFrame, width=25,
                                                  font=('Bookman Old StyleBookman Old Style', 10))
        self.EnReciver.grid(row=1, column=1, padx=20)

        self.lblerrorMsg = Label(self.mailFrame, state=DISABLED, text='**please enter valid username',
                                 font=('Bookman Old Style', 8, 'bold'), fg='red')
        self.lblerrorMsg.grid(row=2, column=1)

        self.lablSubject = Label(self.mailFrame, width=10, text='Subject: ',
                                 font=('Bookman Old StyleBookman Old Style', 12, 'bold'))
        self.lablSubject.grid(row=3, column=0, columnspan=1, pady=15, padx=7, sticky=N)

        self.mailbox = Text(self.mailFrame, width=25, height=10)
        self.mailbox.config(wrap='word', relief=FLAT)
        self.mailbox.focus_set()
        self.mailbox.grid(row=3, column=1, pady=7)

        # =============================================================

        # buttons block
        self.mailFrame2 = Frame(self.frame, relief='ridge')
        self.mailFrame2.grid(row=2, column=0)

        self.btnLogin = Button(self.mailFrame2, text='Discard',
                               font=('Bookman Old Style', 10, 'bold'), width=10, command=self.discardMail)
        self.btnLogin.grid(row=1, column=0, padx=10)
        self.btnLogin = Button(self.mailFrame2,
                               text='Sent', font=('Bookman Old Style', 10, 'bold'), width=10, bg='green',
                               command=self.sentMail)
        self.btnLogin.grid(row=1, column=1, pady=7)

    def sentMail(self):
        if str(type(self.EnReciver)) == '''<class 'tkinter.Entry'>''':
            self.reciver = self.EnReciver.get()
            valid = fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", self.reciver)
            if valid == None:
                self.lblerrorMsg.config(state=NORMAL)
            else:
                #============================================================#


                with open('MultinomialNB_model.dat', 'rb') as f:
                    model = pickle.load(f)
                with open('dictonary.dat', 'rb') as f:
                    dictonary = pickle.load(f)
                query = self.mailbox.get(1.0, END)

                t_q = QueryTransformation()
                t_query = t_q.queryTrans(dictonary, query)
                ped = Predict()
                res = ped.prdict(t_query, model)
                if str(res) == '[0]':
                    messagebox.showinfo('Mail continted', 'ham')
                else:
                    messagebox.showinfo('Mail continted', 'spam')

                #============================================================#


    def discardMail(self):
        self.mailbox.delete(1.0, END)


if __name__ == '__main__':
    main()
