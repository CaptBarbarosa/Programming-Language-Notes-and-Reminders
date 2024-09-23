import tkinter


def create_window():
    window = tkinter.Tk()

    window.title("Hello GUI World")
    window.minsize(width=500, height=300)

    my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold")) # Created the label
    my_label.pack( ) #Shows the label.
    
    # Let's say you want to change the text, or foreground or background you can do:
    #my_label["text"] = "New Text"
    my_label.config(text="New Text")
    
    #button = tkinter.Button(text=)


    window.mainloop() # This will keep the window running.


if __name__ == "__main__":
    create_window()