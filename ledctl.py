import tkinter as tk 
#from gpiozero import LED
#from time import sleep

#red_led = LED(18)
#yel_led = LED(15)
#gre_led = LED(14)

root = tk.Tk()
root.title("TestLED")
root.geometry("300x300")

button1 = tk.Button(root, text="RED",height=2, width=5)
button1.place(x=50,y=50)

button2 = tk.Button(root, text="YELLOW",height=2, width=5)
button2.place(x=120,y=50)

button3 = tk.Button(root, text="GREEN",height=2, width=5)
button3.place(x=190,y=50)

root.mainloop()