import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModelp
import webbrowser
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
root.title("Plant Leaf Disease Detection System")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('page.png')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
#lbl = tk.Label(root, text="Plant Leaf Disease Detection System", font=('times', 35,' bold '), height=1, width=32,bg="maroon1",fg="white")
#lbl.place(x=300, y=10)


#frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="white")
#frame_alpr.grid(row=0, column=0, sticky='nw')
#frame_alpr.place(x=10, y=250)

    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModelp.main()
    
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
    #from keras.optimizers import Adam

#    global fn
    #change 64=256
    IMAGE_SIZE = 256
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('cnnmodelp1.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
     #sequential
        def Register():
            from subprocess import call
            call(["python","TheEmporium.py"])
        
        if plant == 0:
            Cd="Apple Scab  \n Pesticides=Antracol, \n Bonide Captan,\n wettable sulfur,\n summer lime sulfur, \n  "
            #my_link=tk.Label(root,text="link",fg="blue",cursor='hand2',font=('times',20,'underline'))
            #my_link.bind('<Button-1>',lambda x:webbrowser.open_new("https://agrostar.in/product/bayer-antracol-propineb-70-wp-500-g/AGS-CP-699?language=mr&state=maharashtra&gclid=Cj0KCQiAi8KfBhCuARIsADp-A541OleASCSPDFhBy12OsiY_1rDayVugJzdQXHihZeweKABbGZRfFXQaAsB5EALw_wcB"))
            #my_link.place(x=660,y=700)  
            
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
            
        elif plant == 8:
            Cd="Grape Black Rot \n Pesticides = Mancozeb, and Ziram are \n all highly effective \n against black rot., \n"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700) 
        elif plant == 9:
            Cd="Grape Leaf Blight (Isariopsis Leaf Spot) \n Pesticides = Fungicides with the active \n  ingredient Myclobutanil are most \n effective in preventing rust"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 10:            
            Cd="Grape Healthy Leaf"
        elif plant == 11:
            Cd="Potato Early blight \n Pesticides = Mancozeb and chlorothalonil  \n are most \n effective in preventing rust"
           
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 12:
            Cd="Potato Late Blight \n Pesticides = Dithane (mancozeb) MZ or Tattoo C or Acrobat MZ "
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 13:
            Cd="Potato Healthy Leaf "
        elif plant == 14:
            Cd="Strawberry Leaf Scorch  \n Pesticides =  chlorothalonil, myclobutanil, or triflumizole"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700) 
        elif plant == 15:
            Cd="Strawberry Healthy Leaf "
            
        
        elif plant == 1:
            Cd="Apple Black Rot \n Pesticides = BACF Azon Azoxystrobin 11% + Tebuconazole"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 2:
            Cd="Apple Healthy Leaf"
        elif plant == 3:
            Cd=" Data Not Found"   
        elif plant == 4:
            Cd="Cherry Powdery Mildew \n Pesticides = Pristine (pyraclostrobin + boscalid), \n and Unicorn (tebuconazole + sulfur), \n Luna Sensation (fluopyram + trifloxystrobin)"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 5:
            Cd="Cherry Healthy Leaf"
        elif plant == 6:
            Cd="Corn Northern Leaf Blight \n Pesticides=Chlorothalonil (M5) "
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 7:
            Cd="Corn Healthy Leaf"
            
        elif plant == 16:
            Cd="Tomato Bacterial_spot, \n Pesticides = Orcon Bacterial & Viral Disease (Organic IMO Certified), \n Eugenol 01.00% min. and \n Potassium Salt of fatty acids 99.00% "
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 17:
            
            Cd="Tomato Late Blight, \n Pesticides = MYCICON - Fungicide \n For Controlling Fungal Infection Like Powdery, \n Downy Mildew And Blight"
            d3=tk.Button(root,text="Buy",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
            d3.place(x=600,y=700)
        elif plant == 18:
            Cd="Tomato Healthy Leaf"
            
            
       
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=60, font=("bold", 20), bg='bisque2', fg='black')          
    result_label.place(x=250, y=380)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        x2=format(X)+""
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='C:/Users/ashut/Project/dataset', title='Select image for Aanalysis ',
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



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

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

button2 = tk.Button( text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="#17202A",fg="white")
button2.place(x=10, y=360)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=160)
#
button4 = tk.Button( text="CNN_Prediction", command=test_model,width=15, height=1,bg="#17202A",fg="white", font=('times', 15, ' bold '))
button4.place(x=10, y=420)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=480)



root.mainloop()