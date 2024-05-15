from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("Conversion_App")


def jpg_to_png():
    global im1

    # import the image from the folder
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".jpg"):

        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im1.save(export_filename)

        # displaying the Messaging box with the Success
        messagebox.showinfo("success ", "your Image converted to Png")
    else:

        label_2 = Label(root, text="", width=20,
                        fg="red", font=("bold", 15))
        label_2.place(x=80, y=280)
        messagebox.showerror("Fail!!", "Invalid Image Format...")


def png_to_jpg():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith(".png"):
        im1 = Image.open(import_filename)
        im2 = im1.convert('RGB')
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")

        im2.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to jpg ")
    else:
        label_2 = Label(root, text=" ", width=20,
                        fg="red", font=("bold", 15))
        label_2.place(x=80, y=280)

        messagebox.showerror("Fail!!", "Invalid Image Format.....")


def image_to_tiff():
    global im1
    import_filename = fd.askopenfilename()
    im1 = Image.open(import_filename)
    export_filename = fd.asksaveasfilename(defaultextension=".tiff")
    im1.save(export_filename)
    messagebox.showinfo("success ", "your Image converted to TIFF")



def pdf_to_word():
    pass


button1 = Button(root, text="JPG_to_PNG", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png)

button1.place(x=120, y=20)

button2 = Button(root, text="PNG_to_JPEG", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=png_to_jpg)

button2.place(x=120, y=120)


button3 = Button(root, text="Image_to_TIFF", width=20, height=2, bg="green",
                 fg="white", font=("helvetica", 12, "bold"), command=image_to_tiff)

button3.place(x=120, y=220)


root.geometry("500x400+400+200")
root.mainloop()
