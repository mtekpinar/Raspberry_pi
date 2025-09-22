print("yaprak sarma seviyorum :) ")

import tkinter as tk

from gpiozero import LED
from time import sleep




window = tk.Tk()
window.title("Raspberry Pi GUI")
window.geometry("800x600") # width and height

#16.09.2025 saat 15:42 led on off yapıldı.

led = LED(18) # Buradaki bmc numarası = gpio numarasıdır



# Add a button
def on_button1_click():
    
    led.on()
    #sleep(1)
    label1.config(text="LED ON!")
    label2.config(text="Click Me!")
    
    
   
    
def on_button2_click():
       
    label2.config(text="LED OFF!")
    led.off()
    label1.config(text="Click Me!")
    

def on_button3_click():
    label3.config(text="Button Clicked!")
def on_button4_click():
    label4.config(text="Button Clicked!")
    
def on_button5_click():
    label5.config(text="Button Clicked!")
def on_button6_click():
    label6.config(text="Button Clicked!")
    
def on_button7_click():
    label7.config(text="Button Clicked!")    
def on_button8_click():
    label8.config(text="Button Clicked!")
#button= tk.Button(window,text="Click Me",command =on_button_click)
#button.pack(pady=10)

button1= tk.Button(window,text="LED ON",command =on_button1_click)

button1.grid(row =2,column=1, padx=10,pady=10)
# add a Label
label1 = tk.Label(window, text="Click Me",font=("Arial",14))
label1.grid(row=2,column=2,padx=10,pady=20)

# Button 2

button2= tk.Button(window,text="LED OFF",command =on_button2_click)

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

#Run application
window.mainloop()

