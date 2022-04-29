
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font


payment_form = tk.Tk()
payment_form.title("finsYs")
payment_form.geometry("1000x1000")
payment_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(payment_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    scrollregion=mycanvas.bbox('all')))

full_frame = Frame(mycanvas, width=1500, height=1600, bg='#2f516a')
mycanvas.create_window((0, 0), window=full_frame, anchor="nw")


heading_frame = Frame(mycanvas)
mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
headingfont = font.Font(family='Times New Roman', size=25,)
credit_heading = Label(heading_frame, text="PAYMENT", fg='#fff',
                       bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=75)
credit_heading.pack(padx=0, pady=0)

# form fields
sub_headingfont = font.Font(family='Times New Roman', size=20,)
form_frame = Frame(mycanvas, width=1500, height=500, bg='#243e55')
mycanvas.create_window((0, 150), window=form_frame, anchor="nw")


title_lab = tk.Label(form_frame, text="Choose Ref No", bg='#243e55', fg='#fff')
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("REF1 REF2 REF3 REF4")

title_lab.place(x=20, y=100, height=15, width=100)
drop2.place(x=30, y=130, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)

payee = Label(form_frame, text="Payee", bg='#243e55', fg='#fff')
payee.place(x=30, y=200,)
payee_input = Entry(form_frame, width=55, bg='#243e55', fg='#fff')
payee_input.place(x=30, y=230, height=40)


payment_account_lab = tk.Label(
    form_frame, text="Payment account", bg='#243e55', fg='#fff')
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("Acc1 Acc2 Acc3 Acc4")

payment_account_lab.place(x=530, y=200, height=15, width=100)
drop2.place(x=530, y=230, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)

payment_date = Label(form_frame, text="Payment Date", bg='#243e55', fg='#fff')
payment_date.place(x=30, y=300,)
payment_input = Entry(form_frame, width=55, bg='#243e55', fg='#fff')
payment_input.place(x=30, y=330, height=40)


payment_method_lab = tk.Label(
    form_frame, text="Payment Method", bg='#243e55', fg='#fff')
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("Cash Cheque Debit_Card Credit_Card")

payment_method_lab.place(x=530, y=300, height=15, width=100)
drop2.place(x=530, y=330, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)

amount = Label(form_frame, text="AMOUNT", bg='#243e55', fg='#fff')
amount.place(x=1130, y=270,)


digit = font.Font(family='Times New Roman', size=35,)
digit = Label(form_frame, text="0.00", bg='#243e55', font=digit, fg='#fff')
digit.place(x=1130, y=320,)


# CATEGORY DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form2_frame = Frame(mycanvas, width=1500, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 650), window=form2_frame, anchor="nw")

bill_heading = tk.Label(form2_frame, text="Catgory Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form2_frame, text="CATEGORY\t\tDESCRIPTION\t\tNOT APPLICABLE\t\tPRICE\t\tTOTAL\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=120, y=60)

# row1
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form2_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=120, height=15, width=150)
pro_drop.place(x=50, y=150, height=40, width=200)
# 2
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form2_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=210, height=15, width=150)
pro_drop.place(x=50, y=240, height=40, width=200)
# 3
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form2_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=280, height=15, width=150)
pro_drop.place(x=50, y=310, height=40, width=200)


# row 1
discription_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=380, y=150, height=40, width=200)
# row2
discription_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=380, y=240, height=40, width=200)
# row3
discription_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=380, y=310, height=40, width=200)

# row 1
quantity_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=150, height=40, width=200)
# row2
quantity_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=240, height=40, width=200)
# row3
quantity_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=310, height=40, width=200)


# row 1
price_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=150, height=40, width=150)
# row2
price_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=240, height=40, width=150)
# row3
price_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=310, height=40, width=150)

# row 1
total_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=150, height=40, width=100)
# row2
total_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=240, height=40, width=100)
# row3
total_input = Entry(form2_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=310, height=40, width=100)


##################

# ITEM DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form4_frame = Frame(mycanvas, width=1500, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1100), window=form4_frame, anchor="nw")

bill_heading = tk.Label(form4_frame, text="Item Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form4_frame, text="PRODUCT/SERVICE\tHSN\tDESCRIPTION\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\tTAX\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=60, y=60)

# row1
pro = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=120, height=15, width=150)
pro_drop.place(x=50, y=150, height=40, width=175)
# 2
pro = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=210, height=15, width=150)
pro_drop.place(x=50, y=240, height=40, width=175)
# 3
pro = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=50, y=280, height=15, width=150)
pro_drop.place(x=50, y=310, height=40, width=175)


# row 1
discription_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=410, y=150, height=40, width=200)
# row2
discription_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=410, y=240, height=40, width=200)
# row3
discription_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
discription_input.place(x=410, y=310, height=40, width=200)

# row 1
hsn_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input.place(x=280, y=150, height=40, width=100)
# row2
hsn_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input.place(x=280, y=240, height=40, width=100)
# row3
hsn_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
hsn_input.place(x=280, y=310, height=40, width=100)

# row 1
quantity_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=150, height=40, width=200)
# row2
quantity_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=240, height=40, width=200)
# row3
quantity_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
quantity_input.place(x=650, y=310, height=40, width=200)


# row 1
price_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=150, height=40, width=150)
# row2
price_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=240, height=40, width=150)
# row3
price_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
price_input.place(x=880, y=310, height=40, width=150)

# row 1
total_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=150, height=40, width=100)
# row2
total_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=240, height=40, width=100)
# row3
total_input = Entry(form4_frame, width=40, bg='#243e55', fg='#fff')
total_input.place(x=1080, y=310, height=40, width=100)
# row1
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=1250, y=150, height=15, width=150)
pro_drop.place(x=1250, y=150, height=40, width=200)
# row2
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=1250, y=240, height=15, width=150)
pro_drop.place(x=1250, y=240, height=40, width=200)
# row3
pro_drop = ttk.Combobox(form4_frame)
pro_drop['values'] = ("", "", "", "")
pro.place(x=1250, y=310, height=15, width=150)
pro_drop.place(x=1250, y=310, height=40, width=200)

##################


sub_headingfont = font.Font(family='Times New Roman', size=18,)
form3_frame = Frame(mycanvas, width=1600, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1500), window=form3_frame, anchor="nw")

sub_total = Label(form3_frame, text="SUB TOTAL", bg='#243e55', fg='#fff')
sub_total.place(x=900, y=110)
sub_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
sub_input.place(x=1000, y=100, height=40, width=200)

tax_amount = Label(form3_frame, text="TAX AMOUNT", bg='#243e55', fg='#fff')
tax_amount.place(x=900, y=160)
tax_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
tax_input.place(x=1000, y=150, height=40, width=200)

grand_total = Label(form3_frame, text="GRAND TOTAL", bg='#243e55', fg='#fff')
grand_total.place(x=900, y=210)
grand_input = Entry(form3_frame, width=40, bg='#243e55', fg='#fff')
grand_input.place(x=1000, y=200, height=40, width=200)

button = tk.Button(form3_frame, text="Submit Form",)
button.place(x=1050, y=280, width=100)

payment_form.mainloop()
