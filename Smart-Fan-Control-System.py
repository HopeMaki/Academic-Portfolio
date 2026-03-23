#ส่วนนำเข้าไลบารี่
import serial
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk,StringVar
from PIL import Image,ImageTk
import threading

#กำหนดการเชื่อมต่อ
arduino = serial.Serial(port='COM3',baudrate=9600,timeout=1)

#ส่วนการสร้างหน้าต่างแสดงผล
window = Tk()
window.title("ระบบเปิด-ปิดพัดลมอัตโนมัติด้วยอุณภูมิ")
window.geometry("700x500")

#ฟังก์ชันสำหรับเรียกใช้งาน 
def read_temperature():
    data = arduino.readline().deode('utf-8').strip()
    return float(data)
    
def control_fan():
    global themp
    if themp > 27 :
        print("Fan ON - Temperature is above 27°C")
        lb_val.config(text=themp)
        lb_swtch.config(image=on_image)
    else:
        print("Fan ON - Temperature is below 27°C")
        lb_val.config(text=themp)

#นำเข้ารูปภาพ
off_image = ImageTk.PhotoImage(Image.open("switch_off.png"))
on_image = ImageTk.PhotoImage(Image.open("switch_on.png"))
back_image = ImageTk.PhotoImage(Image.open("GUI.png"))


#ส่วนภาพพื้นหลัง
lb_back = ttk.Label(window,image=back_image)
lb_back.place(x=0,y=0)


#ส่วนแสดงอุณภูมิ
lb_1 = Label(window,text="อุณหภูมิ",font=("Helvetica 30 bold"),anchor=tk.CENTER,foreground="#0E435C",background="#CEECE3")
lb_1.place(x=250,y=50,width=400)

lb_val = Label(window,text="",font=("Helvetica 180 bold"),anchor=tk.CENTER,foreground="#0E435C",background="#CEECE3")
lb_val.place(x=250,y=100,width=400)

lb_1 = Label(window,text="องศาเซลเซียส",font=("Helvetica 30 bold"),anchor=tk.CENTER,foreground="#0E435C",background="#CEECE3")
lb_1.place(x=250,y=380,width=400)


#ส่วนสร้างพื้นที่สำหรับ
lb_swtch = ttk.Label(window,image= off_image)
lb_swtch.place(x=55,y=354)


#เรียกใช้งานฟังก์ชั่น
while True:
    temp=read_temperature()
    if temp is not None:
        print(f"Temperature: {temp} °C") 
        control_fan()


#PeriodicThread(0.5,ser_read).start() <<ไม่มั่นใจว่าต้องมีไหมนะ

#ส่วนที่ต้องมี อะนะ-
    window.mainloop()