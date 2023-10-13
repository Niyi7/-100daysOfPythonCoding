import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(
    text="I am a Label",
    fg="blue",
    activebackground="blue",
    activeforeground="red",
    bg="red",
    font=("Arial", 24, "bold"),
)
my_label.pack(expand=1)

my_label["text"] = "New Text"

window.mainloop()


# def add(*args):
#     sum_of_num = 0
#     for n in args:
#         sum_of_num += n
#     return sum_of_num


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def calculate(*args, **kwargs):
#     print(kwargs)

#     for n in args:
#         n += kwargs["add"]
#         n *= kwargs["multiply"]
#         print(n)


# calculate(2, 3, 4, 5, add=3, multiply=5)
