import tkinter as tk
import tkinter.messagebox

def check():
    global result
    global year
    year = entry_1.get()
    try:
        YEAR = int(year)
        if YEAR%4 == 0:
            if YEAR%100 == 0:
                if YEAR%400 == 0:
                    result.configure(text=f"{YEAR} is a leap year.")
                else:
                    result.configure(text=f"{YEAR} is not a leap year.")
            else:
                result.configure(text=f"{YEAR} is a leap year.")
        else:
            result.configure(text=f"{YEAR} is not leap year.")
    except ValueError:
        tkinter.messagebox.askokcancel(title = "Invalid input", message = "You can only use whole numbers.")


window = tk.Tk()
window.title("Leap year Checker")
window['background'] = "#FFFFFF"
window.resizable(0, 0)

window.geometry("500x350")

label_0 = tk.Label(window, text = "Leap Year Checker", font = ("Verdana", 20, "bold underline"), anchor = "center", bg = "#FF7878")
label_0.pack()

label_1 = tk.Label(window, text = "Enter the year: ", font = ("Times", 20), anchor = "center", bg = "#FFFFFF")
label_1.pack(pady = 20)

entry_1 = tk.Entry(window, text = "YYYY", width = 15, bg = "#CFCFCF")
entry_1.pack()

year = 0

button_1 = tk.Button(window, text = "Check", anchor = "e", command = check)
button_1.place(x = 320, y = 108)


result = tk.Label(window, text = '' , font = ("Times", 30, "bold"), bg = "#FFFFFF")
result.pack(pady = 62)

window.mainloop()
