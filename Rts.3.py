from tkinter import *

root = Tk()

root.title("Restaurant Billing Systems")
root.geometry("940x500")

def check(entry, var):
    if var.get() == 1:
        entry.config(state=NORMAL)
    else:
        entry.delete(0, END)
        entry.config(state=DISABLED)

def click(value):
    output.set(output.get() + str(value))

def evaluate():
    result = eval(output.get())
    output.set(str(result))

def clear():
    output.set("")

def total():
    foodPrices = [110, 99, 120, 80, 130]
    drinkprice = 45
    litems = [i1, i2, i3, i4, i5]
    ritems = [i6, i7, i8, i9, i10]
    ccf = 0
    ccd = 0
    for i, j in zip(litems, foodPrices):
        if i.get():
            ccf += int(i.get()) * j
    for i in ritems:
        if i.get():
            ccd += int(i.get()) * drinkprice
    cf.set(ccf)
    cd.set(ccd)
    sc.set(round((ccf + ccd) * 3 / 100, 2))
    st.set(round(ccf + ccd + sc.get(), 2))
    pt.set(round(st.get() * 18 / 100, 2))
    tc.set(round(st.get() + pt.get(), 2))


def recipt():
    lines = [
        "RA's Restaurant",
        "--------------------------",
        f"Cost of Food     : ₹{cf.get()}",
        f"Cost of Drinks   : ₹{cd.get()}",
        f"Service Charges  : ₹{sc.get()}",
        f"Paid Tax         : ₹{pt.get()}",
        f"Sub Total        : ₹{st.get()}",
        f"Total Amount     : ₹{tc.get()}",
        "--------------------------",
        "Thank you! Have a nice day! 😊"
    ]
    receipt_box.delete(0, END)
    for line in lines:
        receipt_box.insert(END, line)


def reset():
    item1.set(0)
    item2.set(0)
    item3.set(0)
    item4.set(0)
    item5.set(0)
    item6.set(0)
    item7.set(0)
    item8.set(0)
    item9.set(0)
    item10.set(0)
    i1.delete(0, END)
    i2.delete(0, END)
    i3.delete(0, END)
    i4.delete(0, END)
    i5.delete(0, END)
    i6.delete(0, END)
    i7.delete(0, END)
    i8.delete(0, END)
    i9.delete(0, END)
    i10.delete(0, END)
    cf.set(0)
    cd.set(0)
    sc.set(0)
    pt.set(0)
    st.set(0)
    tc.set(0)
    output.set("")
    display.delete(0, END)
    receipt_box.delete(0, END)

item1 = IntVar()
item2 = IntVar()
item3 = IntVar()
item4 = IntVar()
item5 = IntVar()
item6 = IntVar()
item7 = IntVar()
item8 = IntVar()
item9 = IntVar()
item10 = IntVar()
output = StringVar()
display = StringVar()
cf = DoubleVar()
cd = DoubleVar()
sc = DoubleVar()
pt = DoubleVar()
st = DoubleVar()
tc = DoubleVar()

body = Frame(root, bg="aqua")
body.grid()

tf = Frame(body, bd=5, relief=RIDGE)
tf.grid(row=0, column=0,columnspan=2, sticky="ew")
lf = Frame(body, bd=5, relief=RIDGE)
lf.grid(row=1, column=0, padx=5, pady=5, sticky="ns")
rf = Frame(body, bd=5, relief=RIDGE)
rf.grid(row=1, column=1, padx=5, pady=5)

Label(tf, text="RA'S Restaurant",font=("Arial", 24, "bold"), fg="green").grid(row=0, column=0, columnspan=2, padx=(250, 0), pady=5)

lfi = Frame(lf, bd=5, relief=RIDGE)
lfi.grid(row=0, column=0, padx=5, pady=5)
mfi = Frame(lf, bd=5, relief=RIDGE)
mfi.grid(row=0, column=1, padx=5, pady=5)
rfi = Frame(lf, bd=5, relief=RIDGE)
rfi.grid(row=0, column=2, padx=5, pady=5)
bf = Frame(lf, bd=5, relief=RIDGE)
bf.grid(row=1, column=0, columnspan=3, sticky="ews", padx=5, pady=5)

# left items
Checkbutton(lfi, text="Pizza Qty.", variable=item1, command=lambda: check(i1, item1)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
i1 = Entry(lfi, state=DISABLED)
i1.grid(row=0, column=1)
Checkbutton(lfi, text="Burger Qty.", variable=item2, command=lambda: check(i2, item2)).grid(row=1, column=0, sticky='w', padx=5, pady=5)
i2 = Entry(lfi, state=DISABLED)
i2.grid(row=1, column=1)
Checkbutton(lfi, text="Fries Qty.", variable=item3, command=lambda: check(i3, item3)).grid(row=2, column=0, sticky='w', padx=5, pady=5)
i3 = Entry(lfi, state=DISABLED)
i3.grid(row=2, column=1)
Checkbutton(lfi, text="Pasta Qty.", variable=item4, command=lambda: check(i4, item4)).grid(row=3, column=0, sticky='w', padx=5, pady=5)
i4 = Entry(lfi, state=DISABLED)
i4.grid(row=3, column=1)
Checkbutton(lfi, text="Tacos Qty.", variable=item5, command=lambda: check(i5, item5)).grid(row=4, column=0, sticky='w', padx=5, pady=5)
i5 = Entry(lfi, state=DISABLED)
i5.grid(row=4, column=1)

# right items
Checkbutton(rfi, text="Thumbs up Qty.", variable=item6, command=lambda: check(i6, item6)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
i6 = Entry(rfi, state=DISABLED)
i6.grid(row=0, column=1)
Checkbutton(rfi, text="coke Qty.", variable=item7, command=lambda: check(i7, item7)).grid(row=1, column=0, sticky='w', padx=5, pady=5)
i7 = Entry(rfi, state=DISABLED)
i7.grid(row=1, column=1)
Checkbutton(rfi, text="pepsi Qty.", variable=item8, command=lambda: check(i8, item8)).grid(row=2, column=0, sticky='w', padx=5, pady=5)
i8 = Entry(rfi, state=DISABLED)
i8.grid(row=2, column=1)
Checkbutton(rfi, text="7up Qty.", variable=item9, command=lambda: check(i9, item9)).grid(row=3, column=0, sticky='w', padx=5, pady=5)
i9 = Entry(rfi, state=DISABLED)
i9.grid(row=3, column=1)
Checkbutton(rfi, text="Mountain Dew Qty.", variable=item10, command=lambda: check(i10, item10)).grid(row=4, column=0, sticky='w', padx=5, pady=5)
i10 = Entry(rfi, state=DISABLED)
i10.grid(row=4, column=1)

# bottom
Label(bf, text="Cost of food").grid(row=0, column=0, sticky='w', padx=5, pady=5)
Label(bf, textvariable=cf).grid(row=0, column=1, sticky='w', padx=5, pady=5)
Label(bf, text="Cost of drinks").grid(row=1, column=0, sticky='w', padx=5, pady=5)
Label(bf, textvariable=cd).grid(row=1, column=1, sticky='w', padx=5, pady=5)
Label(bf, text="Service charge").grid(row=2, column=0, sticky='w', padx=5, pady=5)
Label(bf, textvariable=sc).grid(row=2, column=1, sticky='w', padx=5, pady=5)

Label(bf, text="Paid tax").grid(row=0, column=2, sticky='w', padx=5, pady=5)
Label(bf, textvariable=pt).grid(row=0, column=4, padx=5, pady=5)
Label(bf, text="sub tax").grid(row=1, column=2, sticky='w', padx=5, pady=5)
Label(bf, textvariable=st).grid(row=1, column=4, padx=5, pady=5)
Label(bf, text="total").grid(row=2, column=2, sticky='w', padx=5, pady=5)
Label(bf, textvariable=tc).grid(row=2, column=4, padx=5, pady=5)

# calculator
display = Entry(rf, textvariable=output)
display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

Button(rf, text="7", command=lambda: click(7)).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
Button(rf, text="8", command=lambda: click(8)).grid(row=1, column=1, sticky="ew", padx=5, pady=5)
Button(rf, text="9", command=lambda: click(9)).grid(row=1, column=2, sticky="ew", padx=5, pady=5)
Button(rf, text="+", command=lambda: click('+')).grid(row=1, column=3, sticky="ew", padx=5, pady=5)

Button(rf, text="4", command=lambda: click(4)).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
Button(rf, text="5", command=lambda: click(5)).grid(row=2, column=1, sticky="ew", padx=5, pady=5)
Button(rf, text="6", command=lambda: click(6)).grid(row=2, column=2, sticky="ew", padx=5, pady=5)
Button(rf, text="-", command=lambda: click('-')).grid(row=2, column=3, sticky="ew", padx=5, pady=5)

Button(rf, text="1", command=lambda: click(1)).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
Button(rf, text="2", command=lambda: click(2)).grid(row=3, column=1, sticky="ew", padx=5, pady=5)
Button(rf, text="3", command=lambda: click(3)).grid(row=3, column=2, sticky="ew", padx=5, pady=5)
Button(rf, text="*", command=lambda: click('*')).grid(row=3, column=3, sticky="ew", padx=5, pady=5)

Button(rf, text="C", command=clear).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
Button(rf, text="0", command=lambda: click(0)).grid(row=4, column=1, sticky="ew", padx=5, pady=5)
Button(rf, text="=", command=evaluate).grid(row=4, column=2, sticky="ew", padx=5, pady=5)
Button(rf, text="/", command=lambda: click('/')).grid(row=4, column=3, sticky="ew", padx=5, pady=5)

receipt_box = Listbox(rf, font=("Arial", 12))
receipt_box.grid(row=5, column=0, columnspan=4, sticky="ew")


Button(rf, text="Total", width=10, command=total).grid(row=6, column=0, padx=5, pady=5)
Button(rf, text="Receipt", width=10, command=recipt).grid(row=6, column=1, padx=5, pady=5)
Button(rf, text="Reset", width=10, command=reset).grid(row=6, column=2, padx=5, pady=5)
Button(rf, text="Exit", width=10, command=root.quit).grid(row=6, column=3, padx=5, pady=5)

root.mainloop()
