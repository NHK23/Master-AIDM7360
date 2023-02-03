import tkinter as tk
from tkinter import * 
import os
import matplotlib
matplotlib.use("TkAgg")
import sys
import os
sys.path.append(os.getcwd())
print(sys.platform)
# if sys.platform == 'win32'


class UI:
    def __init__(self, UI_list, House_info, Host_info, House_Location, Platform, Fee, User):
        # Report UI variable
        self.House_info = House_info
        self.Host_info = Host_info
        self.House_Location = House_Location
        self.Platform = Platform
        self.Fee = Fee
        self.User = User
        self.on_hit = -5
        self.UI_list = UI_list
        self.window = tk.Tk()
        self.var = tk.StringVar()
        self.button_var = tk.StringVar()
        self.photo = None
        self.img = None
        self.dispaly = None
        # Get file name variable
        self.text = None
        self.csv_name = None
        self.db_name = None
        self.main_contorl = 0
        self.dispaly = None
        self.Receive = None
        self.txt = None
        # 2 symbols to control shut down or run again
        self.ctn = False
        self.exit = False
        # 4 symbols(binary type) to control operation
        self.update = None      
        self.delete = None
        self.insert = None
        self.report = None



    def hit_display(self):
        if self.on_hit == -5:
            self.var.set('House info table')
            self.window.geometry('820x340')
            self.txt = Text(self.window, height = 15, width = 103)
            self.txt.insert(END, self.House_info)
            self.txt.place(x = 47, y = 67)
            self.on_hit += 1
        elif self.on_hit == -4:
            self.var.set('Host info table')
            self.txt.destroy()
            self.window.geometry('730x340')
            self.txt = Text(self.window, height = 14, width = 93)
            self.txt.insert(END, self.Host_info)
            self.txt.place(x = 42, y = 70)
            self.on_hit += 1
        elif self.on_hit == -3:
            self.var.set('House location table')
            self.window.geometry('840x340')
            self.txt.destroy()
            self.txt = Text(self.window, height = 15, width = 107)
            self.txt.insert(END, self.House_Location)
            self.txt.place(x = 43, y = 70)
            self.on_hit += 1
        elif self.on_hit == -2:
            self.var.set('Platform table')
            self.window.geometry('1080x340')
            self.txt.destroy()
            self.txt = Text(self.window, height = 15, width = 142)
            self.txt.insert(END, self.Platform)
            self.txt.place(x = 40, y = 70)
            self.on_hit += 1
        elif self.on_hit == -1:
            self.var.set('Fee table')
            self.window.geometry('345x340')
            self.txt.destroy()
            self.txt = Text(self.window, height = 15, width = 38)
            self.txt.insert(END, self.Fee)
            self.txt.place(x = 40, y = 70)
            self.on_hit += 1
        elif self.on_hit == 0:
            self.var.set('User table')
            self.window.geometry('705x335')
            self.txt.destroy()
            self.txt = Text(self.window, height = 15, width = 88)
            self.txt.insert(END, self.User)
            self.txt.place(x = 41, y = 70)
            self.on_hit += 1
        elif self.on_hit == 1:
            self.txt.destroy()
            path = os.getcwd() + '/' + 'Data' + '/images/' + 'Neighbourhood_group.png'     
            self.photo = tk.PhotoImage(file = path)
            self.window.geometry('1000x800')
            self.img = tk.Label(image = self.photo)
            self.img.pack(side = 'top')
            self.on_hit += 1
            self.var.set(self.UI_list[0])
        elif self.on_hit == 4:
            self.img.destroy()
            self.window.geometry('1000x200')
            self.on_hit += 1
            self.var.set(self.UI_list[1])
        elif self.on_hit == 3:
            self.img.destroy()
            path = os.getcwd() + '/' + 'Data' + '/images/' + 'cancellation_policy.png'     
            self.photo = tk.PhotoImage(file = path)
            self.window.geometry('1000x800')
            self.img = tk.Label(image = self.photo)
            self.img.pack(side = 'top')
            self.on_hit += 1
            self.var.set(self.UI_list[2])
        elif self.on_hit == 2:
            self.img.destroy()
            path = os.getcwd() + '/' + 'Data' + '/images/' + 'availability_365.png'     
            self.photo = tk.PhotoImage(file = path)
            self.window.geometry('1000x800')
            self.img = tk.Label(image = self.photo)
            self.img.pack(side = 'top')
            self.on_hit += 1
            self.var.set(self.UI_list[3])
        elif self.on_hit == 5:
            self.img.destroy()
            self.window.geometry('1000x200')
            self.on_hit += 1
            self.var.set(self.UI_list[4])
        elif self.on_hit == 6:
            self.on_hit += 1
            self.var.set(self.UI_list[5])
        elif self.on_hit == 7:
            self.on_hit += 1
            self.var.set(self.UI_list[6])
        elif self.on_hit == 8:
            self.on_hit += 1
            self.var.set('The report has been output by a word file and you can click on Exit to re-input a dataset.')
            self.button_var.set('Exit')
        else:
            self.window.update()
            self.window.destroy()

    def UI_report(self):
        self.window.title('Automated content management system')
        self.window.geometry('900x200')

        self.var.set('Please click on button to get report.')
        self.display = tk.Message(self.window, textvariable = self.var, font = ('Arial', 16), width = 900, pady = 20)
        self.display.pack()

        self.button_var.set('Next')
        button = tk.Button(self.window, textvariable = self.button_var, width = 10, height = 2, command = self.hit_display)
        button.pack(side = 'bottom')

        self.window.mainloop()


    # get user inut by text module, and pass variable to main.py to get data
    def get_Text_Input(self):
        if self.main_contorl == 0:
            self.csv_name = self.text.get('1.0', 'end')
            self.text.destroy()
            self.main_contorl += 1
            self.display.destroy()
            self.Receive = tk.Message(self.window, text = 'Recieve it.', font = ('Arial', 16), width = 900, pady = 20)
            self.Receive.pack()
            self.button_var.set('Next')
        elif self.main_contorl == 1:
            self.Receive.destroy()
            self.text = tk.Text(self.window, height = 3)
            self.text.pack()
            self.button_var.set('Input')
            self.main_contorl += 1
            self.Receive = tk.Message(self.window, text = 'Please input you want to create database name. Like airbnb, BOSTON', font = ('Arial', 16), width = 900, pady = 20)
            self.Receive.pack()
        elif self.main_contorl == 2:
            self.db_name = self.text.get('1.0', 'end')
            self.button_var.set('Next')
            self.Receive.destroy()
            self.main_contorl += 1
            self.text.destroy()
            self.Receive = tk.Message(self.window, text = 'Recieve it.', font = ('Arial', 16), width = 900, pady = 20)
            self.Receive.pack()
            self.button_var.set('Exit')
        elif self.main_contorl == 3:
            self.window.update()
            self.window.destroy()

    def file(self):
        self.window.title('Automated content management system')
        self.window.geometry('900x200')

        self.text = tk.Text(self.window, height = 3)
        self.text.pack()

        self.var.set('Please input your dataset file name. Like BOSTON, Airbnb_Open_Data')
        self.display = tk.Message(self.window, textvariable = self.var, font = ('Arial', 16), width = 900, pady = 20)
        self.display.pack()

        self.button_var.set('Input')
        btnRead = tk.Button(self.window, textvariable = self.button_var, height = 2, width = 10, command = self.get_Text_Input)
        btnRead.pack(side = 'bottom')

        self.window.mainloop()
        
        return self.csv_name, self.db_name


    # click on Again button, it will call this function
    def button_continue(self):
        self.ctn = True
        self.window.update()
        self.window.destroy()
    
    # click on Exit button, it will call this function
    def button_exit(self):
        self.exit = True
        self.window.update()
        self.window.destroy()
    
    # control whole programme shut down or run again
    def Exit_or_continue(self):
        self.window.title('Automated content management system')
        self.window.geometry('900x200')

        self.display = tk.Message(self.window, text = '''If you want to shut down the programme, click on Exit.
If you want to input another dataset and get report, click on Again.'''
        , font = ('Arial', 16), width = 800, pady = 30)
        self.display.place(x = 190)

        button = tk.Button(self.window, text = 'Again', width = 13, height = 2, command = self.button_continue)
        button.place(x = 260, y = 130)
        button = tk.Button(self.window, text = 'Exit', width = 13, height = 2, command = self.button_exit)
        button.place(x = 550, y = 130)

        self.window.mainloop()

        if self.exit == True:
            return 1


    # get operation(insert, update, delete, get report) sign    
    def update_button(self):
        self.update = 0b00     
        self.window.update()
        self.window.destroy()
    def delete_button(self):
        self.delete = 0b01
        self.window.update()
        self.window.destroy()
    def insert_button(self):
        self.insert = 0b10
        self.window.update()
        self.window.destroy()
    def report_button(self):
        self.report = 0b11
        self.window.update()
        self.window.destroy()


    def operation_sign(self):
        self.window.title('Automated content management system')
        self.window.geometry('950x200')

        self.display = tk.Message(self.window, text = 'Select operation you want to do.', font = ('Arial', 16), width = 900, pady = 40)
        self.display.pack()

        upd_button = tk.Button(self.window, text = 'Update', width = 12, height = 2, command = self.update_button)     
        upd_button.place(x = 60, y = 130)
        del_button = tk.Button(self.window, text = 'Delete', width = 12, height = 2, command = self.delete_button)
        del_button.place(x = 290, y = 130)
        ins_button = tk.Button(self.window, text = 'Insert', width = 12, height = 2, command = self.insert_button)
        ins_button.place(x = 510, y = 130)
        rep_button = tk.Button(self.window, text = 'Get\nreport', width = 12, height = 2, command = self.report_button)
        rep_button.place(x = 740, y = 130)

        self.window.mainloop()

        # 0b00 is update operation, 0b11 is delete, 0b10 is insert, 0b11 is get report
        if self.update == 0b00:
            return 0b00
        elif self.delete == 0b01:
            return 0b01
        elif self.insert == 0b10:
            return 0b10
        elif self.report == 0b11:
            return 0b11