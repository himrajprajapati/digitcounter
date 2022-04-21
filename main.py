from tkinter import*

counter = 0

def digcount(mylabel) :
    counter = 0
    def digit() :
        global counter
        counter += 1
        mylabel.config(text=str(counter))
        mylabel.after(10,digit)
    digit()

root = Tk()
root.title('Digit Counter')
mylabel = Label(fg='red',font=100)
mylabel.pack()
digcount(mylabel)
btn = Button(text='Terminate',width = 50, command=root.destroy)
btn.pack()

root.mainloop()
