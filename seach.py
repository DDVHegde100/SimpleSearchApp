from tkinter import *
import wikipedia

#setting up basic gui settings for application
root = Tk()
root.title("Wiki")
root.geometry("600x450")
root.configure(bg='#4db8ff')

#establishing and setting the search bar
#update to make placeholder disappear
frame = Frame(root)
input = Entry(frame, width = 50)
input.insert(0, "Type Inquiry Here...")
input.pack()
result = ''
text = Text(root, font = ('ariel',20))

#searching wikipedia for summary and inserting results
def search():
     global result
     result = input.get()
     summary = wikipedia.summary(result, sentences=3)
     text.insert('1.0',summary)

#Setting search bar, background, and additional gui settings
root.configure(bg="#4db8ff")
button = Button(frame, text = 'Search', command = search)                                                 
button.pack(side = RIGHT)
frame.pack(side = TOP)
text.pack()
root.mainloop()
