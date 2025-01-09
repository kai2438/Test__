#ライブラリのインポート
import tkinter as tk 
from tkinter import messagebox
#import wigget
#---------------------------#

#↓文字を挿入する関数
def clickaction(value):
    text.insert(tk.END, value)

#↓末尾の文字を削除する関数
def delateaction():
    current_text = text.get("1.0", tk.END).strip()
    if current_text:
        text.delete("end-2c", tk.END)

def equalaction():
    global StrValue
    StrValue = text.get("1.0", tk.END).strip()
    calc(StrValue)
    
def calc(StrValue):
    print(StrValue)
#---------------------------#


#tkオブジェクト作成
root = tk.Tk()
root.title("Test")
root.geometry("400x550")

#ウィジェットの配置、イベント処理
Area = tk.Label(root, text="計算機")
Area.pack()

#---------------------------#

text = tk.Text(root, height=2, width=50, font=("Arial", 15))
text.pack()
text.bind("<Key>",lambda e: "break")

button7 = tk.Button(root, text="7",height=2, width=5, command=lambda: clickaction("7"))
button7.place(x=30,y=90)

button4 = tk.Button(root, text="4",height=2, width=5, command=lambda: clickaction("4"))
button4.place(x=30,y=135)

button1 = tk.Button(root, text="1",height=2, width=5, command=lambda: clickaction("1"))
button1.place(x=30,y=180)

buttonequal= tk.Button(root, text="=",height=2, width=5, command=lambda: equalaction())
buttonequal.place(x=210,y=180)

button8 = tk.Button(root, text="8",height=2, width=5, command=lambda: clickaction("8"))
button8.place(x=75,y=90)

button5 = tk.Button(root, text="5",height=2, width=5, command=lambda: clickaction("5"))
button5.place(x=75,y=135)

button2 = tk.Button(root, text="2",height=2, width=5, command=lambda: clickaction("2"))
button2.place(x=75,y=180)

button0 = tk.Button(root, text="0",height=2, width=5, command=lambda: clickaction("0"))
button0.place(x=75,y=225)

button9 = tk.Button(root, text="9",height=2, width=5, command=lambda: clickaction("9"))
button9.place(x=120,y=90)

button6 = tk.Button(root, text="6",height=2, width=5, command=lambda: clickaction("6"))
button6.place(x=120,y=135)

button3 = tk.Button(root, text="3",height=2, width=5, command=lambda: clickaction("3"))
button3.place(x=120,y=180)

buttonten = tk.Button(root, text=".",height=2, width=5, command=lambda: clickaction("."))
buttonten.place(x=120,y=225)

buttonwal = tk.Button(root, text="÷",height=2, width=5, command=lambda: clickaction("+"))
buttonwal.place(x=165,y=90)

buttonkakeru = tk.Button(root, text="x",height=2, width=5, command=lambda: clickaction("x"))
buttonkakeru.place(x=165,y=135)

buttonhiku = tk.Button(root, text="-",height=2, width=5, command=lambda: clickaction("-"))
buttonhiku.place(x=165,y=180)

buttontasu = tk.Button(root, text="+",height=2, width=5, command=lambda: clickaction("+"))
buttontasu.place(x=165,y=225)

buttonkakkol = tk.Button(root, text="(",height=2, width=5, command=lambda: clickaction("("))
buttonkakkol.place(x=210,y=90)

buttonkakkor = tk.Button(root, text=")",height=2, width=5, command=lambda: clickaction(")"))
buttonkakkor.place(x=210,y=135)

delate = tk.Button(root, text="削除",height=2, width=5, command=delateaction)
delate.place(x=255,y=90)

#---------------------------#



#メインループ実行
root.mainloop()