import tkinter as tk 
from gpiozero import LED
from time import sleep

red_led = LED(18)
yel_led = LED(15)
gre_led = LED(14)

def redon():
    yel_led.off()
    gre_led.off()
    red_led.on()
    print("赤色点灯！")

def yelon():
    red_led.off()
    gre_led.off()
    yel_led.on()
    print("黄色点灯！")

def greon():
    red_led.off()
    yel_led.off()
    gre_led.on()
    print("緑色点灯！")

root = tk.Tk()
root.title("TestLED")
root.geometry("300x300")

button1 = tk.Button(root, text="RED",height=2, width=5, command=redon)
button1.place(x=50,y=50)

button2 = tk.Button(root, text="YELLOW",height=2, width=5, command=yelon)
button2.place(x=120,y=50)

button3 = tk.Button(root, text="GREEN",height=2, width=5, command=greon)
button3.place(x=190,y=50)

root.mainloop()