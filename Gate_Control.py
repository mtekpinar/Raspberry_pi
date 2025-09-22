print("yaprak sarma ")

import tkinter as tk

window = tk.Tk()
window.title("BEYKOY HES KAPAK Raspberry Pi GUI")
window.configure(bg="black")
window.geometry("1200x800") # width and height



########### Button Click Functions ############


# *** You can define click GPIO functions here 

def on_button1_click():
    label1.config(text="kapak 1 Indir ON- Kaldir OFF!")
    
def on_button2_click():
    label2.config(text="Button2 Clicked!",bg="black",fg="green",font=("Arial",14,"bold"))

def on_button3_click():
    label3.config(text="Button3 Clicked!")
def on_button4_click():
    label4.config(text="Button4 Clicked!")
    
def on_button5_click():
    label5.config(text="Button5 Clicked!")
def on_button6_click():
    label6.config(text="Button6 Clicked!")
    
def on_button7_click():
    label7.config(text="Button7 Clicked!")    
def on_button8_click():
    label8.config(text="Button8 Clicked!")

#### Second Column ####
    
def on_button21_click():
    label21.config(text="kapak 1 Indir OFF- Kaldir ON!")
    
def on_button22_click():
    label22.config(text="Button22 Clicked")

def on_button23_click():
    label23.config(text="Button23 Clicked!")
def on_button24_click():
    label24.config(text="Button24 Clicked!")
    
def on_button25_click():
    label25.config(text="Button25 Clicked!")
def on_button26_click():
    label26.config(text="Button26 Clicked!")
    
def on_button27_click():
    label27.config(text="Button27 Clicked!")    
def on_button28_click():
    label28.config(text="Button28 Clicked!")
    

#### Third Column ####
    
def on_button31_click():
    label31.config(text="kapak 1 stpped!")
    
def on_button32_click():
    label32.config(text="Button32 Clicked")

def on_button33_click():
    label33.config(text="Button33 Clicked!")
def on_button34_click():
    label34.config(text="Button34 Clicked!")
    
def on_button35_click():
    label35.config(text="Button35 Clicked!")
def on_button36_click():
    label36.config(text="Button36 Clicked!")
    
def on_button37_click():
    label37.config(text="Button37 Clicked!")    
def on_button38_click():
    label38.config(text="Button38 Clicked!")
    
############# BUTTON DEFINE#################   
#button= tk.Button(window,text="Click Me",command =on_button_click)
#button.pack(pady=10)


# Add a button to window

button1= tk.Button(window,text="Kapak1 Indir",command =on_button1_click)

button1.grid(row =2,column=1, padx=10,pady=10)
# add a Label
label1 = tk.Label(window, text="Click Me",font=("Arial",14))
label1.grid(row=2,column=2,padx=10,pady=20)

# Button 2

button2= tk.Button(window,text="kapak 2 Aç",command =on_button2_click)

button2.grid(row =3,column=1, padx=10,pady=10)
# add a Label
label2 = tk.Label(window, text="Click Me",font=("Arial",14))
label2.grid(row=3,column=2,padx=10,pady=20)


#Button3
button3= tk.Button(window,text="Button 3",command =on_button3_click)

button3.grid(row =4,column=1, padx=10,pady=10)
# add a Label
label3 = tk.Label(window, text="Click Me",font=("Arial",14))
label3.grid(row=4,column=2,padx=10,pady=20)

#Button4
button4= tk.Button(window,text="Button 4",command =on_button4_click)

button4.grid(row =5,column=1, padx=10,pady=10)
# add a Label
label4 = tk.Label(window, text="Click Me",font=("Arial",14))
label4.grid(row=5,column=2,padx=10,pady=20)



#Button5
button5= tk.Button(window,text="Button 5",command =on_button5_click)

button5.grid(row =6,column=1, padx=10,pady=10)
# add a Label
label5 = tk.Label(window, text="Click Me",font=("Arial",14))
label5.grid(row=6,column=2,padx=10,pady=20)




#Button6
button6= tk.Button(window,text="Button 6",command =on_button6_click)

button6.grid(row =7,column=1, padx=10,pady=10)
# add a Label
label6 = tk.Label(window, text="Click Me",font=("Arial",14))
label6.grid(row=7,column=2,padx=10,pady=20)


#Button7
button7= tk.Button(window,text="Button 7",command =on_button7_click)

button7.grid(row =8,column=1, padx=10,pady=10)
# add a Label
label7 = tk.Label(window, text="Click Me",font=("Arial",14))
label7.grid(row=8,column=2,padx=10,pady=20)

#Button8
button8= tk.Button(window,text="Button 8",command =on_button8_click)

button8.grid(row =9,column=1, padx=10,pady=10)
# add a Label
label8 = tk.Label(window, text="Click Me",font=("Arial",14))
label8.grid(row=9,column=2,padx=10,pady=20)

###########

button21= tk.Button(window,text="Kapak1 Kaldir",command =on_button21_click)

button21.grid(row =2,column=3, padx=10,pady=10)
# add a Label
label21 = tk.Label(window, text="Click Me",font=("Arial",14))
label21.grid(row=2,column=4,padx=10,pady=20)

# Button 22

button22= tk.Button(window,text="kapak 2 kapat",command =on_button22_click)

button22.grid(row =3,column=3, padx=10,pady=10)
# add a Label
label22 = tk.Label(window, text="Click Me",font=("Arial",14))
label22.grid(row=3,column=4,padx=10,pady=20)

#Button23
button23= tk.Button(window,text="Button 23",command =on_button23_click)

button23.grid(row =4,column=3, padx=10,pady=10)
# add a Label
label23 = tk.Label(window, text="Click Me",font=("Arial",14))
label23.grid(row=4,column=4,padx=10,pady=20)

#Button24
button24= tk.Button(window,text="Button 24",command =on_button24_click)

button24.grid(row =5,column=3, padx=10,pady=10)
# add a Label
label24 = tk.Label(window, text="Click Me",font=("Arial",14))
label24.grid(row=5,column=4,padx=10,pady=20)

#Button25
button25= tk.Button(window,text="Button 25",command =on_button25_click)

button25.grid(row =6,column=3, padx=10,pady=10)
# add a Label
label25 = tk.Label(window, text="Click Me",font=("Arial",14))
label25.grid(row=6,column=4,padx=10,pady=20)

#Button26
button26= tk.Button(window,text="Button 26",command =on_button26_click)

button26.grid(row =7,column=3, padx=10,pady=10)
# add a Label
label26 = tk.Label(window, text="Click Me",font=("Arial",14))
label26.grid(row=7,column=4,padx=10,pady=20)

#Button27
button27= tk.Button(window,text="Button 27",command =on_button27_click)

button27.grid(row =8,column=3, padx=10,pady=10)
# add a Label
label27 = tk.Label(window, text="Click Me",font=("Arial",14))
label27.grid(row=8,column=4,padx=10,pady=20)

#Button28
button28= tk.Button(window,text="Button 28",command =on_button28_click)

button28.grid(row =9,column=3, padx=10,pady=10)
# add a Label
label28 = tk.Label(window, text="Click Me",font=("Arial",14))
label28.grid(row=9,column=4,padx=10,pady=20)

########### Stop

###########

button31= tk.Button(window,text="Kapak1 stop",command =on_button31_click)

button31.grid(row =2,column=5, padx=10,pady=10)
# add a Label
label31 = tk.Label(window, text="Click Me",font=("Arial",14))
label31.grid(row=2,column=6,padx=10,pady=20)

# Button 32
button32= tk.Button(window,text="kapak 2 stop",command =on_button32_click)

button32.grid(row =3,column=5, padx=10,pady=10)
# add a Label
label32 = tk.Label(window, text="Click Me",font=("Arial",14))
label32.grid(row=3,column=6,padx=10,pady=20)

#Button33
button33= tk.Button(window,text="Button 33",command =on_button33_click)

button33.grid(row =4,column=5, padx=10,pady=10)
# add a Label
label33 = tk.Label(window, text="Click Me",font=("Arial",14))
label33.grid(row=4,column=6,padx=10,pady=20)

#Button34
button34= tk.Button(window,text="Button 34",command =on_button34_click)

button34.grid(row =5,column=5, padx=10,pady=10)
# add a Label
label34 = tk.Label(window, text="Click Me",font=("Arial",14))
label34.grid(row=5,column=6,padx=10,pady=20)

#Button35
button35= tk.Button(window,text="Button 35",command =on_button35_click)

button35.grid(row =6,column=5, padx=10,pady=10)
# add a Label
label35 = tk.Label(window, text="Click Me",font=("Arial",14))
label35.grid(row=6,column=6,padx=10,pady=20)

#Button36
button36= tk.Button(window,text="Button 36",command =on_button36_click)

button36.grid(row =7,column=5, padx=10,pady=10)
# add a Label
label36 = tk.Label(window, text="Click Me",font=("Arial",14))
label36.grid(row=7,column=6,padx=10,pady=20)

#Button37
button37= tk.Button(window,text="Button 37",command =on_button37_click)

button37.grid(row =8,column=5, padx=10,pady=10)
# add a Label
label37 = tk.Label(window, text="Click Me",font=("Arial",14))
label37.grid(row=8,column=6,padx=10,pady=20)

#Button38
button38= tk.Button(window,text="Button 38",command =on_button38_click)

button38.grid(row =9,column=5, padx=10,pady=10)
# add a Label
label38 = tk.Label(window, text="Click Me",font=("Arial",14))
label38.grid(row=9,column=6,padx=10,pady=20)





#Run application
window.mainloop()

