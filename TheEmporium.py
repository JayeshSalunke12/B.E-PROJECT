from tkinter import *
from tkinter import messagebox
import tkinter as tk
import PIL as p
from PIL import Image
import PIL.ImageTk as ptk
import os
from datetime import datetime
root=Tk()
root.title("theemporium.in")
root.geometry("3200x2200")
bg = Image.open("main1.png")
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=p.Image.open("Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open("UI.jpg"))

grocery1_image=ptk.PhotoImage(p.Image.open("img1.jpeg"))
grocery2_image=ptk.PhotoImage(p.Image.open("img2.jpeg"))
grocery3_image=ptk.PhotoImage(p.Image.open("img3.jpeg"))
grocery4_image=ptk.PhotoImage(p.Image.open("img4.jpeg"))
grocery5_image=ptk.PhotoImage(p.Image.open("img5.jpeg"))
grocery6_image=ptk.PhotoImage(p.Image.open("img6.jpeg"))
grocery7_image=ptk.PhotoImage(p.Image.open("img7.jpeg"))
grocery8_image=ptk.PhotoImage(p.Image.open("img8.jpeg"))
grocery9_image=ptk.PhotoImage(p.Image.open("img9.jpeg"))
grocery10_image=ptk.PhotoImage(p.Image.open("img10.jpeg"))



#Grocery Variables
clicked_grocery1=StringVar()
clicked_grocery1.set("1kg - Rs.200")
clicked_grocery2=StringVar()
clicked_grocery2.set("1.5kg – Rs.300")
clicked_grocery3=StringVar()
clicked_grocery3.set("750g – Rs.250")
clicked_grocery4=StringVar()
clicked_grocery4.set("1kg – Rs.195")
clicked_grocery5=StringVar()
clicked_grocery5.set("25kg – Rs.500")
clicked_grocery6=StringVar()
clicked_grocery6.set("5kg – Rs.300")
clicked_grocery7=StringVar()
clicked_grocery7.set("10kg – Rs.350")
clicked_grocery8=StringVar()
clicked_grocery8.set("2kg – Rs.200")
clicked_grocery9=StringVar()
clicked_grocery9.set("25kg – Rs.400")
clicked_grocery10=StringVar()
clicked_grocery10.set("5kg – Rs.325")
grocery_list=[]

#pesticides
pest1=ptk.PhotoImage(p.Image.open("p1.jpg"))
pest2=ptk.PhotoImage(p.Image.open("p2.jpg"))
pest3=ptk.PhotoImage(p.Image.open("p3.jpg"))
pest4=ptk.PhotoImage(p.Image.open("p4.jpg"))
pest5=ptk.PhotoImage(p.Image.open("p5.jpeg"))
pest6=ptk.PhotoImage(p.Image.open("p6.png"))
pest7=ptk.PhotoImage(p.Image.open("p7.jpeg"))
pest8=ptk.PhotoImage(p.Image.open("p8.jpeg"))
pest9=ptk.PhotoImage(p.Image.open("p9.jpeg"))
pest10=ptk.PhotoImage(p.Image.open("p10.jpeg"))




clicked_pest1=StringVar()
clicked_pest1.set("500ml - Rs.200")
clicked_pest2=StringVar()
clicked_pest2.set("500ml – Rs.300")
clicked_pest3=StringVar()
clicked_pest3.set("750g – Rs.250")
clicked_pest4=StringVar()
clicked_pest4.set("500ml – Rs.195")
clicked_pest5=StringVar()
clicked_pest5.set("500ml – Rs.200")
clicked_pest6=StringVar()
clicked_pest6.set("5kg – Rs.300")
clicked_pest7=StringVar()
clicked_pest7.set("10kg – Rs.350")
clicked_pest8=StringVar()
clicked_pest8.set("2kg – Rs.200")
clicked_pest9=StringVar()
clicked_pest9.set("25kg – Rs.400")
clicked_pest10=StringVar()
clicked_pest10.set("5kg – Rs.325")
pest_list=[]

#name=Label(Heading,text="",font="arial 20 bold italic",bg="light pink",fg="blue").grid(row=0,column=1)
tagline=Label(Heading,text="Shopping made easier!",font="magneto 16 italic",fg="gold",bg="black").grid(row=0,column=4,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1050,height=800)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=250,y=100)
#label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)

def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s

def GroceryCall():
    HideAllFrames()
    Grocery_Label=Label(Products_frame,text="Fertilizer",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_grocery1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery1.place(x=5,y=35,width=180,height=280)
    lf_grocery2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery2.place(x=210,y=35,width=180,height=280)
    lf_grocery3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery3.place(x=415,y=35,width=180,height=280)
    lf_grocery4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery4.place(x=620,y=35,width=180,height=280)
    lf_grocery5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery5.place(x=825,y=35,width=180,height=280)
    lf_grocery6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery6.place(x=5,y=310,width=180,height=280)
    lf_grocery7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery7.place(x=210,y=310,width=180,height=280)
    lf_grocery8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery8.place(x=415,y=310,width=180,height=280)
    lf_grocery9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery9.place(x=620,y=310,width=180,height=280)
    lf_grocery10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery10.place(x=825,y=310,width=180,height=280)
    label_grocery_1=Label(lf_grocery1,image=grocery1_image,bd=2).grid(row=0,column=0)
    label_grocery_2=Label(lf_grocery2,image=grocery2_image,bd=2).grid(row=0,column=0)
    label_grocery_3=Label(lf_grocery3,image=grocery3_image,bd=2).grid(row=0,column=0,padx=13)
    label_grocery_4=Label(lf_grocery4,image=grocery4_image,bd=2).grid(row=0,column=0)
    label_grocery_5=Label(lf_grocery5,image=grocery5_image,bd=2).grid(row=0,column=0)
    label_grocery_6=Label(lf_grocery6,image=grocery6_image,bd=2).grid(row=0,column=0)
    label_grocery_7=Label(lf_grocery7,image=grocery7_image,bd=2).grid(row=0,column=0)
    label_grocery_8=Label(lf_grocery8,image=grocery8_image,bd=2).grid(row=0,column=0)
    label_grocery_9=Label(lf_grocery9,image=grocery9_image,bd=2).grid(row=0,column=0)
    label_grocery_10=Label(lf_grocery10,image=grocery10_image,bd=2).grid(row=0,column=0)
    name_grocery1=Label(lf_grocery1,text="Fertilizer",font="arial 9").grid(row=1,column=0)
    name_grocery2=Label(lf_grocery2,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery3=Label(lf_grocery3,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery4=Label(lf_grocery4,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery5=Label(lf_grocery5,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery6=Label(lf_grocery6,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery7=Label(lf_grocery7,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery8=Label(lf_grocery8,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_grocery9=Label(lf_grocery9,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_grocery10=Label(lf_grocery10,text="Fertilizer",font="arial 9",justify="center").grid(row=1,column=0)
    label_qty_grocery1=Label(lf_grocery1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery2=Label(lf_grocery2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery3=Label(lf_grocery3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery4=Label(lf_grocery4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery5=Label(lf_grocery5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery6=Label(lf_grocery6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery7=Label(lf_grocery7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery8=Label(lf_grocery8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery9=Label(lf_grocery9,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery10=Label(lf_grocery10,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_grocery1=["1kg – Rs.200","5kg – Rs.800"]
    options_grocery2=["1.5kg – Rs.300","10kg – Rs.1000"]
    options_grocery3=["750g – Rs.250"]
    options_grocery4=["1kg – Rs.195"]
    options_grocery5=["25kg – Rs.500","50kg – Rs.1000"]
    options_grocery6=["5kg – Rs.300","10kg – Rs.1500"]
    options_grocery7=["10kg – Rs.350","20kg – Rs.600"]
    options_grocery8=["2kg – Rs.200","5kg – Rs.500","10kg – Rs.950"]
    options_grocery9=["25kg – Rs.400","50kg – Rs.2800"]
    options_grocery10=["5kg – Rs.325","10kg – Rs.600"]
    global clicked_grocery1,clicked_grocery2,clicked_grocery3,clicked_grocery4,clicked_grocery5,grocery_list
    global clicked_grocery6,clicked_grocery7,clicked_grocery8,clicked_grocery9,clicked_grocery10
    drop_grocery1=OptionMenu(lf_grocery1,clicked_grocery1,*options_grocery1).place(x=30,y=212)
    drop_grocery2=OptionMenu(lf_grocery2,clicked_grocery2,*options_grocery2).place(x=30,y=212)
    drop_grocery3=OptionMenu(lf_grocery3,clicked_grocery3,*options_grocery3).place(x=30,y=212)
    drop_grocery4=OptionMenu(lf_grocery4,clicked_grocery4,*options_grocery4).place(x=30,y=212)
    drop_grocery5=OptionMenu(lf_grocery5,clicked_grocery5,*options_grocery5).place(x=30,y=212)
    drop_grocery6=OptionMenu(lf_grocery6,clicked_grocery6,*options_grocery6).place(x=30,y=212)
    drop_grocery7=OptionMenu(lf_grocery7,clicked_grocery7,*options_grocery7).place(x=30,y=212)
    drop_grocery8=OptionMenu(lf_grocery8,clicked_grocery8,*options_grocery8).place(x=30,y=212)
    drop_grocery9=OptionMenu(lf_grocery9,clicked_grocery9,*options_grocery9).place(x=30,y=212)
    drop_grocery10=OptionMenu(lf_grocery10,clicked_grocery10,*options_grocery10).place(x=30,y=212)
    def GroceryPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def GroceryQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery1.get()),GroceryQty(clicked_grocery1.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery1.get()+") is not added to the cart.")
    def AddG2():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery2.get()),GroceryQty(clicked_grocery2.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery2.get()+") is not added to the cart.")
    def AddG3():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery3.get()),GroceryQty(clicked_grocery3.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery3.get()+") is not added to the cart.")
    def AddG4():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery4.get()),GroceryQty(clicked_grocery4.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery4.get()+") is not added to the cart.")
    def AddG5():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery5.get()),GroceryQty(clicked_grocery5.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery5.get()+") is not added to the cart.")
    def AddG6():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery6.get()),GroceryQty(clicked_grocery6.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery6.get()+") is not added to the cart.")
    def AddG7():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery7.get()),GroceryQty(clicked_grocery7.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery7.get()+") is not added to the cart.")
    def AddG8():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery8.get()),GroceryQty(clicked_grocery8.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery8.get()+") is not added to the cart.")
    def AddG9():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery9.get()),GroceryQty(clicked_grocery9.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery9.get()+") is not added to the cart.")
    def AddG10():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Fertilizere",GroceryPrice(clicked_grocery10.get()),GroceryQty(clicked_grocery10.get()),Spaces(40-len("Fertilizere"))])
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fertilizere ("+clicked_grocery10.get()+") is not added to the cart.")
    add_grocery1=Button(lf_grocery1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=60,y=245)
    add_grocery2=Button(lf_grocery2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=60,y=245)
    add_grocery3=Button(lf_grocery3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=60,y=245)
    add_grocery4=Button(lf_grocery4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=60,y=245)
    add_grocery5=Button(lf_grocery5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=60,y=245)
    add_grocery6=Button(lf_grocery6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=60,y=245)
    add_grocery7=Button(lf_grocery7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=60,y=245)
    add_grocery8=Button(lf_grocery8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=60,y=245)
    add_grocery9=Button(lf_grocery9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=60,y=245)
    add_grocery10=Button(lf_grocery10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=60,y=245)

def PesticidesCall():
    HideAllFrames()
    Grocery_Label=Label(Products_frame,text="Pesticides",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_grocery1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery1.place(x=5,y=35,width=180,height=280)
    lf_grocery2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery2.place(x=210,y=35,width=180,height=280)
    lf_grocery3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery3.place(x=415,y=35,width=180,height=280)
    lf_grocery4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery4.place(x=620,y=35,width=180,height=280)
    lf_grocery5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery5.place(x=825,y=35,width=180,height=280)
    lf_grocery6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery6.place(x=5,y=310,width=180,height=280)
    lf_grocery7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery7.place(x=210,y=310,width=180,height=280)
    lf_grocery8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery8.place(x=415,y=310,width=180,height=280)
    lf_grocery9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery9.place(x=620,y=310,width=180,height=280)
    lf_grocery10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_grocery10.place(x=825,y=310,width=180,height=280)
    label_grocery_1=Label(lf_grocery1,image=pest1,bd=2).grid(row=0,column=0)
    label_grocery_2=Label(lf_grocery2,image=pest2,bd=2).grid(row=0,column=0)
    label_grocery_3=Label(lf_grocery3,image=pest3,bd=2).grid(row=0,column=0,padx=13)
    label_grocery_4=Label(lf_grocery4,image=pest4,bd=2).grid(row=0,column=0)
    label_grocery_5=Label(lf_grocery5,image=pest5,bd=2).grid(row=0,column=0)
    label_grocery_6=Label(lf_grocery6,image=pest6,bd=2).grid(row=0,column=0)
    label_grocery_7=Label(lf_grocery7,image=pest7,bd=2).grid(row=0,column=0)
    label_grocery_8=Label(lf_grocery8,image=pest8,bd=2).grid(row=0,column=0)
    label_grocery_9=Label(lf_grocery9,image=pest9,bd=2).grid(row=0,column=0)
    label_grocery_10=Label(lf_grocery10,image=pest10,bd=2).grid(row=0,column=0)
    name_grocery1=Label(lf_grocery1,text="",font="arial 9").grid(row=1,column=0)
    name_grocery2=Label(lf_grocery2,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery3=Label(lf_grocery3,text="",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery4=Label(lf_grocery4,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery5=Label(lf_grocery5,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery6=Label(lf_grocery6,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery7=Label(lf_grocery7,text="",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery8=Label(lf_grocery8,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_grocery9=Label(lf_grocery9,text="",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_grocery10=Label(lf_grocery10,text="",font="arial 9",justify="center").grid(row=1,column=0)
    label_qty_grocery1=Label(lf_grocery1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery2=Label(lf_grocery2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery3=Label(lf_grocery3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery4=Label(lf_grocery4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery5=Label(lf_grocery5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery6=Label(lf_grocery6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery7=Label(lf_grocery7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery8=Label(lf_grocery8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery9=Label(lf_grocery9,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery10=Label(lf_grocery10,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_grocery1=["500ml – Rs.200","1.5l – Rs.800"]
    options_grocery2=["500ml – Rs.300","1l – Rs.1000"]
    options_grocery3=["750g – Rs.250"]
    options_grocery4=["500ml – Rs.195"]
    options_grocery5=["500ml – Rs.200","1l – Rs.350"]
    options_grocery6=["250g – Rs.300","500g – Rs.400"]
    options_grocery7=["250g – Rs.350","500g – Rs.600"]
    options_grocery8=["150g – Rs.200","250g – Rs.350","500g – Rs.500"]
    options_grocery9=["150g – Rs.100","250g – Rs.200"]
    options_grocery10=["250g – Rs.200","500gg – Rs.350"]
    global clicked_pest1,clicked_pest2,clicked_pest3,clicked_pest4,clicked_pest5,pest_list
    global clicked_pest6,clicked_pest7,clicked_pest8,clicked_pest9,clicked_pest10
    drop_grocery1=OptionMenu(lf_grocery1,clicked_pest1,*options_grocery1).place(x=30,y=212)
    drop_grocery2=OptionMenu(lf_grocery2,clicked_pest2,*options_grocery2).place(x=30,y=212)
    drop_grocery3=OptionMenu(lf_grocery3,clicked_pest3,*options_grocery3).place(x=30,y=212)
    drop_grocery4=OptionMenu(lf_grocery4,clicked_pest4,*options_grocery4).place(x=30,y=212)
    drop_grocery5=OptionMenu(lf_grocery5,clicked_pest5,*options_grocery5).place(x=30,y=212)
    drop_grocery6=OptionMenu(lf_grocery6,clicked_pest6,*options_grocery6).place(x=30,y=212)
    drop_grocery7=OptionMenu(lf_grocery7,clicked_pest7,*options_grocery7).place(x=30,y=212)
    drop_grocery8=OptionMenu(lf_grocery8,clicked_pest8,*options_grocery8).place(x=30,y=212)
    drop_grocery9=OptionMenu(lf_grocery9,clicked_pest9,*options_grocery9).place(x=30,y=212)
    drop_grocery10=OptionMenu(lf_grocery10,clicked_pest10,*options_grocery10).place(x=30,y=212)
    def GroceryPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def GroceryQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest1.get()),GroceryQty(clicked_pest1.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest1.get()+") is not added to the cart.")
    def AddG2():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest2.get()),GroceryQty(clicked_pest2.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest2.get()+") is not added to the cart.")
    def AddG3():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest3.get()),GroceryQty(clicked_pest3.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest3.get()+") is not added to the cart.")
    def AddG4():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest4.get()),GroceryQty(clicked_pest4.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest4.get()+") is not added to the cart.")
    def AddG5():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest5.get()),GroceryQty(clicked_pest5.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest5.get()+") is not added to the cart.")
    def AddG6():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest6.get()),GroceryQty(clicked_pest6.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest6.get()+") is not added to the cart.")
    def AddG7():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest7.get()),GroceryQty(clicked_pest7.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest7.get()+") is not added to the cart.")
    def AddG8():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest8.get()),GroceryQty(clicked_pest8.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest8.get()+") is not added to the cart.")
    def AddG9():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest9.get()),GroceryQty(clicked_pest9.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide("+clicked_pest9.get()+") is not added to the cart.")
    def AddG10():
        global pest_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            pest_list.append(["Pesticide",GroceryPrice(clicked_pest10.get()),GroceryQty(clicked_pest10.get()),Spaces(40-len("Pesticide"))])
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pesticide ("+clicked_pest10.get()+") is not added to the cart.")
    add_grocery1=Button(lf_grocery1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=60,y=245)
    add_grocery2=Button(lf_grocery2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=60,y=245)
    add_grocery3=Button(lf_grocery3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=60,y=245)
    add_grocery4=Button(lf_grocery4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=60,y=245)
    add_grocery5=Button(lf_grocery5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=60,y=245)
    add_grocery6=Button(lf_grocery6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=60,y=245)
    add_grocery7=Button(lf_grocery7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=60,y=245)
    add_grocery8=Button(lf_grocery8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=60,y=245)
    add_grocery9=Button(lf_grocery9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=60,y=245)
    add_grocery10=Button(lf_grocery10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=60,y=245)

#Grocery_button=Button(Button_frame,text="Grocery",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=GroceryCall)
#Grocery_button.grid(row=0,column=0,padx=5,pady=5)
def window():
  root.destroy()



Grocery_button=Button(Button_frame,text="Fertilizers",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=GroceryCall)
Grocery_button.grid(row=0,column=0,padx=5,pady=5)

Grocery_button=Button(Button_frame,text="Pesticides",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=PesticidesCall)
Grocery_button.grid(row=1,column=0,padx=5,pady=5)
Grocery_button=Button(Button_frame,text="Back",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=window)
Grocery_button.grid(row=2,column=0,padx=5,pady=5)
#Electronics_button=Button(Button_frame,text="Electronics",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=ElectronicsCall)
#Electronics_button.grid(row=1,column=0,padx=5,pady=5)
#Sports_Gym_button=Button(Button_frame,text="Sports and Gym",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=SportsGymCall)
#Sports_Gym_button.grid(row=2,column=0,padx=5,pady=5)
#Furniture_button=Button(Button_frame,text="Furniture",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=FurnitureCall)
#Furniture_button.grid(row=3,column=0,padx=5,pady=5)
#Appliances_button=Button(Button_frame,text="Appliances",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=AppliancesCall)
#Appliances_button.grid(row=4,column=0,padx=5,pady=5)
Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="green",font="arial 16 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)


       
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.750)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        grocery_price=0
        electronics_price=0
        sportsgym_price=0
        furniture_price=0
        appliances_price=0
        for i in range(len(grocery_list)):
            grocery_price+=grocery_list[i][1]
        for i in range(len(pest_list)):
            appliances_price+=pest_list[i][1]
       
        total_price=grocery_price+electronics_price+appliances_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=900,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"The Emporium\n"+Spaces(90,'*')+"\n")
            if len(grocery_list)>0:
                bill_txt_area.insert(END,"Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in grocery_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Price : Rs."+str(grocery_price)+"\n"+Spaces(90,'*')+"\n")
            
            
            if len(pest_list)>0:
                bill_txt_area.insert(END,"Pesticide (s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in pest_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Pesticides Price : Rs."+str(appliances_price)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=700)
            
            save_button=Button(root,text="Exit",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=window)
            save_button.place(x=300,y=700)
    #  Appliances Price      
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.grid(row=0,column=20)

root.mainloop()
