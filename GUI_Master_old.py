import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Crop Prediction And Leaf Disease Using Machine Learning")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
#img=ImageTk.PhotoImage(Image.open("bg2.jpg"))

#img2=ImageTk.PhotoImage(Image.open("bg3.jpg"))

#img3=ImageTk.PhotoImage(Image.open("bg4.png"))
image2 =Image.open('page.png')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
#def move():
#	global x
#	if x == 4:
#		x = 1
#	if x == 1:
#		logo_label.config(image=img)
#	elif x == 2:
#		logo_label.config(image=img2)
#	elif x == 3:
#		logo_label.config(image=img3)
#	x = x+1
#	root.after(2000, move)


#move() 


#lbl = tk.Label(root, text="Crop Prediction And Leaf Disease Using Machine Learning", font=('times', 35,' bold '), height=2, width=60,bg="#8B008B",fg="white")
#lbl.place(x=0, y=0)


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)

#frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=300, bd=5, font=('times', 14, ' bold '),bg="pink")
#frame_alpr.grid(row=0, column=0, sticky='nw')
#frame_alpr.place(x=20, y=150)


    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model
    from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 100
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('C:/Users/ashut/OneDrive/Desktop/UI/soil_model_cnn.h5')
            
        # adam = Adam(lr=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        # model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        brain=np.argmax(prediction)
        print(brain)
        
        def Register():
            from subprocess import call
            call(["python","TheEmporium.py"])
        
        
        if brain == 0:
            Cd="Not a Soil"
            
            
        elif brain ==2:
            Cd="Alluvial Soil"
            _label = tk.Label(root, text="Crop List: \n  Sugarcane, Maize, Cotton, Soybean, Jute", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=300, y=500)
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif brain ==3:
            Cd="Black Soil"
            _label = tk.Label(root, text="Crop List: \n Wheat, onion, Sunflower", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=300, y=500)
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif brain ==4:
            Cd="Red Soil"
            _label = tk.Label(root, text="Crop List: \n Cotton, Oilseeds, Potatoes, Ginger", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=300, y=500)
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif brain ==5:
            Cd="Yellow Soil1"
            _label = tk.Label(root, text="Crop List: \n Rice, Pulses, Ragi", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=300, y=500)
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
       
        A=Cd
        return A

# def clear_img():
    
#     img11 = tk.Label(frame_display, background='lightblue4',width=160,height=120)
#     img11.place(x=0, y=0)







def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=25, height=1, font=('times', 30,' bold '), bg='goldenrod', fg='black')
    result_label.place(x=450, y=380)
# def train_model():
    
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X=Model_frm.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     update_label(msg)

def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Selected Image is {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg='\n'+ X1 + '\n'
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='C:/Users/ashut/OneDrive/Desktop/UI/Soil_data', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


#
#        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
#
#        gs = cv2.resize(gs, (x1, y1))
#
#        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250)
    #result_label1.place(x=300, y=100)
    img.image = imgtk
    img.place(x=300, y=100)
   # out_label.config(text=imgpath)

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button( text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="#17202A",fg="white")
button1.place(x=10, y=300)

button2 = tk.Button(text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="#17202A",fg="white")
button2.place(x=10, y=360)

# button4 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button4.place(x=10, y=240)
#
button3 = tk.Button( text="CNN_Prediction", command=test_model,width=15, height=1,bg="#17202A",fg="white", font=('times', 15, ' bold '))
button3.place(x=10, y=420)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=480)



root.mainloop()