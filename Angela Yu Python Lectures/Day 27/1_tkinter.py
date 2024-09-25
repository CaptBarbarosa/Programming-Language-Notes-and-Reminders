import tkinter


def create_window():
    window = tkinter.Tk()

    window.title("Hello GUI World")
    window.minsize(width=500, height=300)

    my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold")) # Created the label
    my_label.pack() #Shows the label.
    
    # Let's say you want to change the text, or foreground or background you can do:
    #my_label["text"] = "New Text"
    #my_label.place(x=100, y=0)
    my_label.config(text="New Text")
    
    
    input = tkinter.Entry(width=15)
    input.pack()
    
    #IMPORTANT
    #Lambda allows you to create an anonymous function that will defer execution of button_clicked until the button is clicked.
    #Without lambda it will automatically execute the function.
    button = tkinter.Button(text="Click Here", command=lambda: button_clicked(my_label, input))
    button.pack()


    window.mainloop() # This will keep the window running.


def button_clicked(my_label, input):
    #This will change the text of the window when button clicked.
    """
    my_label.config(text="You clicked the button")
    print("Button is clicked")
    """
    #This will change the label to what the user enters as an entry.
    my_label.config(text=input.get())


if __name__ == "__main__":
    create_window()