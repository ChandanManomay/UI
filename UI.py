from tkinter import *


# Main Window
window = Tk()
window.geometry("1080x600")
window.configure(bg="#FFFFFF")

# Frames
main_frame = Frame(window, highlightthickness=2, highlightbackground="black")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_1 = Frame(main_frame, highlightthickness=2, highlightbackground="black")
frame_1.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

frame_2 = Frame(main_frame, highlightthickness=2, highlightbackground="black")
frame_2.place(relx=0, rely=0, relheight=.6, relwidth=0.7)

frame_3 = Frame(main_frame, highlightthickness=2, highlightbackground="black")
frame_3.place(relx=0, rely=0.6, relheight=.4, relwidth=0.7)


# Canvas
canvas_frame_2 = Canvas(frame_2)
canvas_frame_2.place(relx=0, rely=0, relheight=1, relwidth=1)

canvas_frame_3 = Canvas(frame_3)
canvas_frame_3.place(relx=0, rely=0, relheight=1, relwidth=1)

# Frame 3 Scrollbar
vertical_scrollbar = Scrollbar(canvas_frame_3, orient="vertical")
vertical_scrollbar.pack(side=RIGHT, fill=Y)

horizontal_scrollbar = Scrollbar(
    canvas_frame_3, orient="horizontal")
horizontal_scrollbar.pack(side=BOTTOM, fill=X)


# Dummy text
text = '''Technology is all around you – in your gaming gadgets like the Wii, Playstation, Xbox, etc. and in your mobile phones, iPads, computers, etc. Most 
of the things we have in our kitchen, like the microwave, toaster, fridge, etc. are all different types of technology.
 Technology is when we take something from the world of science and then create it into something that 
 humans use.

We must keep our food cold so that it is not spoilt by being out in the warm weather. 
This concept of science helped scientists develop technology to keep our food cold when we are not eating it 
by using the fridge. However, all of us like to eat hot food. So, to instantly make food hot, scientists 
created a microwave. In this way, scientists used technology to help all of us with our daily lives. Technology is 
very useful in our daily lives.'''
t = Text(canvas_frame_3, wrap=NONE, xscrollcommand=horizontal_scrollbar.set,
         yscrollcommand=vertical_scrollbar.set, font=('Helvetica 19'))
t.insert(INSERT, text)
t.pack(side=TOP, fill=X)
horizontal_scrollbar.config(command=t.xview)
vertical_scrollbar.config(command=t.yview)


# + button in frame 1


def add_button_func():
    temp_frame = Frame(frame_1, height=50)
    temp_frame.place(relwidth=.9, y=(len(frame_1.winfo_children())-3)*50)
    Entry(temp_frame, bd=1).place(
        relx=0.005, rely=0.1, relwidth=.3, relheight=.7)
    Entry(temp_frame, bd=1).place(
        relx=0.33, rely=0.1, relwidth=.3, relheight=.7)
    Entry(temp_frame, bd=1).place(
        relx=0.66, rely=0.1, relwidth=.3, relheight=.7)


def remove_button_func():
    if len(frame_1.winfo_children()) > 2:
        frame_1.winfo_children()[2:][-1].destroy()


add_button = Button(frame_1, text='+', height=1,
                    width=1, command=add_button_func)
add_button.place(relx=.89, rely=.01, relheight=.05, relwidth=.1)


remove_button = Button(frame_1, text='-', height=1,
                       width=1, command=remove_button_func)
remove_button.place(relx=.89, rely=.08, relheight=.05, relwidth=.1)


window.mainloop()
