import tkinter as tk

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("first")
from tkinter import ttk
n = tk.StringVar()
onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
onthchoosen['values'] = ('男生', '女生')
onthchoosen.place(relx=0.6,rely=0.3,anchor="n")
def show():
    print(onthchoosen.get())
    text1 = tk.Label(wnd,text=onthchoosen.get())
    text1.pack()
def mes():
    from tkinter import messagebox
    messagebox.showinfo('訊息','哈囉！')
def close():
    wnd.destroy()
add=tk.Button(wnd,text="show",underline=-1,command=show)
add.pack()
show2  =tk.Button(wnd,text="show2",underline=-1,command=mes)
show2.pack()
close2 = tk.Button(wnd,text="close",underline=-1,command=close)
close2.place(relx=0.6,rely=0.8,anchor="n")
wnd.mainloop()