# ---------------------------tic tac toe game--------------------------------

from tkinter import *
from tkinter.messagebox import *


class tictac:

    def reset(self):
        self.bt1["text"] = ""
        self.bt2["text"] = ""
        self.bt3["text"] = ""
        self.bt4["text"] = ""
        self.bt5["text"] = ""
        self.bt6["text"] = ""
        self.bt7["text"] = ""
        self.bt8["text"] = ""
        self.bt9["text"] = ""
        self.bt1["state"] = "normal"
        self.bt2["state"] = "normal"
        self.bt3["state"] = "normal"
        self.bt4["state"] = "normal"
        self.bt5["state"] = "normal"
        self.bt6["state"] = "normal"
        self.bt7["state"] = "normal"
        self.bt8["state"] = "normal"
        self.bt9["state"] = "normal"
        self.bt1.config(bg="light green")
        self.bt2.config(bg="pink")
        self.bt3.config(bg="light green")
        self.bt4.config(bg="pink")
        self.bt5.config(bg="light green")
        self.bt6.config(bg="pink")
        self.bt7.config(bg="light green")
        self.bt8.config(bg="pink")
        self.bt9.config(bg="light green")
        self.player = 0

    def chekwin(self):
        if self.bt1["text"] == "X" and self.bt2["text"] == "X" and self.bt3["text"] == "X":
            self.bt1.config(bg="cadet blue")
            self.bt2.config(bg="cadet blue")
            self.bt3.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt4["text"] == "X" and self.bt5["text"] == "X" and self.bt6["text"] == "X":
            self.bt4.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt6.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt7["text"] == "X" and self.bt8["text"] == "X" and self.bt9["text"] == "X":
            self.bt7.config(bg="cadet blue")
            self.bt8.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt1["text"] == "X" and self.bt4["text"] == "X" and self.bt7["text"] == "X":
            self.bt1.config(bg="cadet blue")
            self.bt4.config(bg="cadet blue")
            self.bt7.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt2["text"] == "X" and self.bt5["text"] == "X" and self.bt8["text"] == "X":
            self.bt2.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt8.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt3["text"] == "X" and self.bt6["text"] == "X" and self.bt9["text"] == "X":
            self.bt3.config(bg="cadet blue")
            self.bt6.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt1["text"] == "X" and self.bt5["text"] == "X" and self.bt9["text"] == "X":
            self.bt1.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt3["text"] == "X" and self.bt5["text"] == "X" and self.bt7["text"] == "X":
            self.bt3.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt7.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 1 win")
            self.reset()
        elif self.bt1["text"] == "0" and self.bt2["text"] == "0" and self.bt3["text"] == "0":
            self.bt1.config(bg="cadet blue")
            self.bt2.config(bg="cadet blue")
            self.bt3.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt4["text"] == "0" and self.bt5["text"] == "0" and self.bt6["text"] == "0":
            self.bt4.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt6.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt7["text"] == "0" and self.bt8["text"] == "0" and self.bt9["text"] == "0":
            self.bt7.config(bg="cadet blue")
            self.bt8.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt1["text"] == "0" and self.bt4["text"] == "0" and self.bt7["text"] == "0":
            self.bt1.config(bg="cadet blue")
            self.bt4.config(bg="cadet blue")
            self.bt7.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt2["text"] == "0" and self.bt5["text"] == "0" and self.bt8["text"] == "0":
            self.bt2.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt8.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt3["text"] == "0" and self.bt6["text"] == "0" and self.bt9["text"] == "0":
            self.bt3.config(bg="cadet blue")
            self.bt6.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt1["text"] == "0" and self.bt5["text"] == "0" and self.bt9["text"] == "0":
            self.bt1.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt9.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt3["text"] == "0" and self.bt5["text"] == "0" and self.bt7["text"] == "0":
            self.bt3.config(bg="cadet blue")
            self.bt5.config(bg="cadet blue")
            self.bt7.config(bg="cadet blue")
            showinfo("Winner", "Congratulations!!!\n\nPlayer 2 win")
            self.reset()
        elif self.bt1["state"] == "disabled" and self.bt2["state"] == "disabled" and self.bt3["state"] == "disabled" and \
                self.bt4["state"] == "disabled" and self.bt5["state"] == "disabled" and self.bt6[
            "state"] == "disabled" and self.bt7["state"] == "disabled" and self.bt8["state"] == "disabled" and self.bt9[
            "state"] == "disabled":
            showinfo("Draw", "Oops!! Match Draw\n\nTry Again!!!!")
            self.reset()

    def play1(self):
        if self.player % 2 == 0:
            self.bt1["text"] = "X"
        elif self.player % 2 != 0:
            self.bt1["text"] = "0"
        self.player = self.player + 1
        self.bt1["state"] = "disabled"
        self.chekwin()

    def play2(self):
        if self.player % 2 == 0:
            self.bt2["text"] = "X"
        elif self.player % 2 != 0:
            self.bt2["text"] = "0"
        self.player = self.player + 1
        self.bt2["state"] = "disabled"
        self.chekwin()

    def play3(self):
        if self.player % 2 == 0:
            self.bt3["text"] = "X"
        elif self.player % 2 != 0:
            self.bt3["text"] = "0"
        self.player = self.player + 1
        self.bt3["state"] = "disabled"
        self.chekwin()

    def play4(self):
        if self.player % 2 == 0:
            self.bt4["text"] = "X"
        elif self.player % 2 != 0:
            self.bt4["text"] = "0"
        self.player = self.player + 1
        self.bt4["state"] = "disabled"
        self.chekwin()

    def play5(self):
        if self.player % 2 == 0:
            self.bt5["text"] = "X"
        elif self.player % 2 != 0:
            self.bt5["text"] = "0"
        self.player = self.player + 1
        self.bt5["state"] = "disabled"
        self.chekwin()

    def play6(self):
        if self.player % 2 == 0:
            self.bt6["text"] = "X"
        elif self.player % 2 != 0:
            self.bt6["text"] = "0"
        self.player = self.player + 1
        self.bt6["state"] = "disabled"
        self.chekwin()

    def play7(self):
        if self.player % 2 == 0:
            self.bt7["text"] = "X"
        elif self.player % 2 != 0:
            self.bt7["text"] = "0"
        self.player = self.player + 1
        self.bt7["state"] = "disabled"
        self.chekwin()

    def play8(self):
        if self.player % 2 == 0:
            self.bt8["text"] = "X"
        elif self.player % 2 != 0:
            self.bt8["text"] = "0"
        self.player = self.player + 1
        self.bt8["state"] = "disabled"
        self.chekwin()

    def play9(self):
        if self.player % 2 == 0:
            self.bt9["text"] = "X"
        elif self.player % 2 != 0:
            self.bt9["text"] = "0"
        self.player = self.player + 1
        self.bt9["state"] = "disabled"
        self.chekwin()

    def __init__(self):
        self.root = Tk()
        self.root.title("TIC TAC TOE")
        self.root.config(bg="black")
        self.player = 0
        # file=PhotoImage(file="1.png")  image=file--- ib btn
        self.bt1 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play1)
        self.bt1.config(bg="light green")
        self.bt2 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play2)
        self.bt2.config(bg="pink")
        self.bt3 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, bg="light green",
                          fg="white", command=self.play3)
        # or #self.bt3.config(bg="light green", fg="white")
        self.bt4 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play4)
        self.bt4.config(bg="pink")
        self.bt5 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play5)
        self.bt5.config(bg="light green")
        self.bt6 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play6)
        self.bt6.config(bg="pink")
        self.bt7 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play7)
        self.bt7.config(bg="light green")
        self.bt8 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play8)
        self.bt8.config(bg="pink")
        self.bt9 = Button(self.root, borderwidth=8, text="", font=("bold", 25), width=9, height=4, command=self.play9)
        self.bt9.config(bg="light green")
        self.lb1 = Label(self.root, text="Players : ", font=("arial", 15, "bold"))
        self.lb2 = Label(self.root, text="X is player 1\n0 is player 2", font=("arial", 15))
        self.lb1.config(bg="black", fg="white")
        self.lb2.config(bg="black", fg="white")

        self.bt1.grid(row=0, column=0)
        self.bt2.grid(row=0, column=1)
        self.bt3.grid(row=0, column=2)
        self.bt4.grid(row=1, column=0)
        self.bt5.grid(row=1, column=1)
        self.bt6.grid(row=1, column=2)
        self.bt7.grid(row=2, column=0)
        self.bt8.grid(row=2, column=1)
        self.bt9.grid(row=2, column=2)
        self.lb1.grid(row=3, column=0, padx=10, pady=10)
        self.lb2.grid(row=3, column=1, padx=10, pady=10)

        self.root.mainloop()


# ---------------------------------fxn end here---------------------------------------
obj = tictac()
