import os
import sys
import pyodbc
import tkinter as tk
import tkinter.messagebox as mbox
import win32api
import tkinter.font as tkFont
import configparser
from tkinter import messagebox

# Read the connection parameters from the INI file
#config = configparser.ConfigParser()
#config.read('config.ini')

#server_name = config.get('server', 'name')
#database_name = config.get('database', 'database')
#username = config.get('database', 'username')
#password = config.get('database', 'password')#

# Connect to the SQL Server database using ODBC
try:
    cnxn = pyodbc.connect('DSN=DinetaKasa;UID=sa;PWD=opmz96z;Driver={SQL Server};Server=.\SQLEXPRESS;Database=DinetaKasa')
    connection_status = "CONNECTED"
except pyodbc.Error as ex:
    # Handle any errors that occurred while setting up the connection
    print("Error connecting to SQL Server:", ex)
    connection_status = "ERROR"


# Define the function to execute the SQL command
def execute_sql(sql_command):
    cursor = cnxn.cursor()
    cursor.execute(sql_command)
    cnxn.commit()

# Define the function to update the connection status label
def update_connection_status_label():
    if connection_status == "CONNECTED":
        connection_status_label.config(text="CONNECTED", fg="green")
    else:
        connection_status_label.config(text="ERROR", fg="red")

# Define the version number
VERSION = "2.0"


# Create a popup window to get the pin code from the user
#def get_pin():
#    def on_submit():
#        if entry.get() == "110011":
#            popup.destroy() # Close the pin code window
#            root.deiconify()  # Show the main window
#        else:
#            messagebox.showerror("Klaida", "Blogas kodas")
#            sys.exit()  # Close the whole program
#
#    popup = tk.Toplevel()
#    popup.title("Įveskit Pin kodą")
#    popup.geometry("300x150")
#    popup.resizable(False, False)
#    popup.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
#
#    label = tk.Label(popup, text="Įvėskit Pin kodą", font=("Helvetica", 16))
#    label.pack(pady=10)
#
#    entry = tk.Entry(popup, show="*")
#    entry.pack(pady=10)
#
#    button = tk.Button(popup, text="Go", command=on_submit)
#    button.pack(pady=10)


# Create the GUI
root = tk.Tk()
root.title("DinetaPosManager v{}".format(VERSION))
# Set the icon for the window
root.iconbitmap('icon.ico')


# Create a scrollbar for the new frame
button_scrollbar = tk.Scrollbar(button_frame, orient='vertical', command=button_scroll_frame.yview)
button_scrollbar.pack(side='right', fill='y')

# create a scrollbar for the y-axis
y_scrollbar = tk.Scrollbar(frame, orient='vertical')
y_scrollbar.pack(side='right', fill='y')

# create a scrollbar for the x-axis
x_scrollbar = tk.Scrollbar(frame, orient='horizontal')
x_scrollbar.pack(side='bottom', fill='x')

# create a listbox widget to test the scrollbars
listbox = tk.Listbox(frame, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
for i in range(100):
    listbox.insert(tk.END, 'Item %d' % i)
listbox.pack(side='left', fill='both', expand=True)

# associate the scrollbars with the listbox widget
y_scrollbar.config(command=listbox.yview)
x_scrollbar.config(command=listbox.xview)






# Hide the main window until the correct pin code is entered
#root.withdraw()

# Set the background image of the GUI
bg_image = tk.PhotoImage(file=r"background.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#get_pin()








# Create the frame to hold the buttons - Banko kortelės -  Svarstyklės - Sanitex - Perlas - Amžiaus cenzo priminimas - Kliento displėjus
button_frame = tk.Frame(root, bg="#00A2E8")
button_frame.grid(row=1, column=0, padx=10, pady=10)

# Create a new frame for the extra buttons - Lentų trynimas
button_frame2 = tk.Frame(root, bg="#00A2E8")
button_frame2.grid(row=3, column=0, padx=10, pady=10)


# Create a new frame for the SQL Update Statements
button_frame3 = tk.Frame(root, bg="#00A2E8")
button_frame3.grid(row=6, column=0, padx=10, pady=10)

    

# Create the frame to hold the buttons - Fiskalinis režimas
button_frame4 = tk.Frame(root, bg="#00A2E8")
button_frame4.grid(row=0, column=0, padx=10, pady=10)

# Create the frame to hold the buttons
button_frame5 = tk.Frame(root, bg="#00A2E8")
button_frame5.grid(row=1, column=0, padx=10, pady=10)



# Set the background image of the frame
frame_bg_image = tk.PhotoImage(file=r"background.png")
frame_bg_label = tk.Label(button_frame, image=frame_bg_image)
frame_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

  
# Set the background image of the frame
frame_bg_image2 = tk.PhotoImage(file=r"background.png")
frame_bg_label2 = tk.Label(button_frame2, image=frame_bg_image2)
frame_bg_label2.place(x=0, y=0, relwidth=1, relheight=1)


# Set the background image of the frame SQL
frame_bg_image3 = tk.PhotoImage(file=r"background.png")
frame_bg_label3 = tk.Label(button_frame3, image=frame_bg_image3)
frame_bg_label3.place(x=0, y=0, relwidth=1, relheight=1)

# Set the background image of the frame SQL
frame_bg_image4 = tk.PhotoImage(file=r"background.png")
frame_bg_label4 = tk.Label(button_frame4, image=frame_bg_image4)
frame_bg_label4.place(x=0, y=0, relwidth=1, relheight=1)

# Set the background image of the frame SQL
frame_bg_image5 = tk.PhotoImage(file=r"background.png")
frame_bg_label5 = tk.Label(button_frame5, image=frame_bg_image4)
frame_bg_label5.place(x=0, y=0, relwidth=1, relheight=1)


bold_font = tkFont.Font(weight="bold")
    
# Text font
    
text_bg_image = tk.PhotoImage(file=r"Text.png")
text_style = {"width": text_bg_image.width(), "height": text_bg_image.height(), "image": text_bg_image, "compound": "center", "font": bold_font, "fg": "white"}

text_bg_image = tk.PhotoImage(file=r"Text.png")
text_style2 = {"width": text_bg_image.width(), "height": text_bg_image.height(), "image": text_bg_image, "compound": "center", "font": bold_font, "fg": "#FFCCCB"}

text_bg_image = tk.PhotoImage(file=r"Text.png")
text_style3 = {"width": text_bg_image.width(), "height": text_bg_image.height(), "image": text_bg_image, "compound": "center", "font": bold_font, "fg": "#FFFFFF"}

#text

text = "Fiskalinis režimas"
button1 = tk.Label(button_frame4, text=text, **text_style)
button1.grid(row=0, column=0, padx=2, pady=2)

text = "Banko kortelės"
button2 = tk.Label(button_frame, text=text, **text_style)
button2.grid(row=0, column=0, padx=2, pady=2)


text = "Svarstyklės"
button3 = tk.Label(button_frame, text=text, **text_style)
button3.grid(row=1, column=0, padx=2, pady=2)


text = "Sanitex"
button4 = tk.Label(button_frame, text=text, **text_style)
button4.grid(row=2, column=0, padx=2, pady=2)

text = "Perlas"
button8 = tk.Label(button_frame, text=text, **text_style)
button8.grid(row=3, column=0, padx=2, pady=2)

text = "Amžiaus cenzas"
button5 = tk.Label(button_frame, text=text, **text_style)
button5.grid(row=4, column=0, padx=2, pady=2)


text = "Kliento displėjus"
button7 = tk.Label(button_frame, text=text, **text_style)
button7.grid(row=5, column=0, padx=2, pady=2)

text = "Kainos keitimas"
button20 = tk.Label(button_frame, text=text, **text_style)
button20.grid(row=6, column=0, padx=2, pady=2)


text = "DK pardavimas"
button21 = tk.Label(button_frame, text=text, **text_style)
button21.grid(row=7, column=0, padx=2, pady=2)


text = "Lentų trynimas"
button6 = tk.Label(button_frame2, text=text, **text_style2)
button6.grid(row=0, column=0, padx=2, pady=2)


text_style3 = {"width": 30, "height": 2, "compound": "center", "font": bold_font, "fg": "White","bg": "#00A2E8"}


# Create a new frame for the extra buttons - Padalinys
button_frame6 = tk.Frame(root, bg="#00A2E8")
button_frame6.grid(row=7, column=0, padx=1, pady=1)


# Create a new frame for the extra buttons - Padalinys
button_frame7 = tk.Frame(root, bg="#00A2E8")
button_frame7.grid(row=8, column=0, padx=1, pady=1)


# Define the SQL script

sql_script = "SELECT T_STORE.F_NAME FROM T_STORE JOIN T_DEVICE ON T_DEVICE.F_STOREID = T_STORE.ID"

# Define the function to execute the SQL script and update the button text
def execute_sql_script():
    try:
        cursor = cnxn.cursor()
        cursor.execute(sql_script)
        rows = cursor.fetchall()
        result_text = ""
        for row in rows:
            result_text += str(row[0]) + "\n"
        button19.config(text=result_text)
    except pyodbc.Error as ex:
        # Handle any errors that occurred while executing the SQL script
        print("Error executing SQL script:", ex)

# Create the button widget with the initial SQL script as its label
button19 = tk.Label(button_frame6, text="", **text_style3, anchor="center")

button19.grid(row=0, column=0, padx=1, pady=1)


# Call the function to execute the SQL script when the program starts
execute_sql_script()



sql_script = "SELECT T_PARTNER.F_NAME FROM T_PARTNER JOIN T_DEVICE ON T_DEVICE.F_DEBTORID = T_PARTNER.ID"


# Define the function to execute the SQL script and update the button text
def execute_sql_script():
    try:
        cursor = cnxn.cursor()
        cursor.execute(sql_script)
        rows = cursor.fetchall()
        result_text = ""
        for row in rows:
            result_text += str(row[0]) + "\n"
        button20.config(text=result_text)
    except pyodbc.Error as ex:
        # Handle any errors that occurred while executing the SQL script
        print("Error executing SQL script:", ex)

# Create the button widget with the initial SQL script as its label
button20 = tk.Label(button_frame7, text="", **text_style3, anchor="center")

button20.grid(row=1, column=0, padx=1, pady=1)


# Call the function to execute the SQL script when the program starts
execute_sql_script()



text = "Dovanų kuponais"
button9 = tk.Label(button_frame, text=text, **text_style)
button9.grid(row=0, column=7, padx=2, pady=2)

text = "Kreditas nr.3"
button10 = tk.Label(button_frame, text=text, **text_style)
button10.grid(row=1, column=7, padx=2, pady=2)

text = "Kreditas nr.4"
button11 = tk.Label(button_frame, text=text, **text_style)
button11.grid(row=2, column=7, padx=2, pady=2)

text = "Kreditas nr.5"
button12 = tk.Label(button_frame, text=text, **text_style)
button12.grid(row=3, column=7, padx=2, pady=2)

text = "Sandelio numeris"
button13 = tk.Label(button_frame, text=text, **text_style)
button13.grid(row=5, column=7, padx=2, pady=2)

text = "Kasos numeris"
button14 = tk.Label(button_frame, text=text, **text_style)
button14.grid(row=6, column=7, padx=2, pady=2)

text = "Pasword"
button15 = tk.Label(button_frame, text=text, **text_style)
button15.grid(row=7, column=7, padx=2, pady=2)

text = "Dineta Web URL"
button16 = tk.Label(button_frame, text=text, **text_style)
button16.grid(row=4, column=7, padx=2, pady=2)

text = "COM PORT"
button17 = tk.Label(button_frame4, text=text, **text_style)
button17.grid(row=1, column=0, padx=2, pady=2)


text = "COM OPEN"
button18 = tk.Label(button_frame4, text=text, **text_style)
button18.grid(row=2, column=0, padx=2, pady=2)


text = "Max nuolaida"
button19 = tk.Label(button_frame, text=text, **text_style)
button19.grid(row=8, column=7, padx=2, pady=2)





# Create the buttons


# Button font

button_bg_image = tk.PhotoImage(file=r"Button.png")
button_style = {"width": button_bg_image.width(), "height": button_bg_image.height(), "image": button_bg_image, "compound": "center", "font": bold_font, "fg": "white"}


button_bg_image = tk.PhotoImage(file=r"Button2.png")
button_style2 = {"width": button_bg_image.width(), "height": button_bg_image.height(), "image": button_bg_image, "compound": "center", "font": bold_font, "fg": "#FFCCCB"}

button_bg_image = tk.PhotoImage(file=r"Button2.png")
button_style3 = {"fg": "#FFFFFF"}

button_bg_image = tk.PhotoImage(file=r"Button.png")
button_style = {"width": button_bg_image.width(), "height": button_bg_image.height(), "image": button_bg_image, "compound": "center", "font": bold_font, "fg": "white"}






# Buttons 

button1_1 = tk.Button(button_frame4, text="Išjungti", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='2'"), **button_style)
button1_1.grid(row=0, column=1, padx=2, pady=2)

button1_2 = tk.Button(button_frame4, text="SPS", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='9'"), **button_style)
button1_2.grid(row=0, column=2, padx=2, pady=2)

button1_3 = tk.Button(button_frame4, text="Empirija", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='0'"),  **button_style)
button1_3.grid(row=0, column=3, padx=2, pady=2)

button1_4 = tk.Button(button_frame4, text="RASO", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='5'"),  **button_style)
button1_4.grid(row=0, column=4, padx=2, pady=2)

button1_5 = tk.Button(button_frame4, text="ASPA", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='4'"), **button_style)
button1_5.grid(row=0, column=5, padx=2, pady=2)
button1_6 = tk.Button(button_frame4, text="Strauja", command=lambda: execute_sql("update T_DEVICE set F_DEVICETYPE='12'"),  **button_style)
button1_6.grid(row=0, column=6, padx=2, pady=2)

button2_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='-' where F_NAME ='INTEGRATEDCARD'"), **button_style)
button2_1.grid(row=0, column=1, padx=2, pady=2)

button2_2 = tk.Button(button_frame, text="Wordline", command=lambda: execute_sql("update T_PARAM set F_VALUE='FDL' where F_NAME ='INTEGRATEDCARD'"), **button_style)
button2_2.grid(row=0, column=2, padx=2, pady=2)

button2_3 = tk.Button(button_frame, text="Verifone", command=lambda: execute_sql("update T_PARAM set F_VALUE='Verifone' where F_NAME ='INTEGRATEDCARD'"), **button_style)
button2_3.grid(row=0, column=3, padx=2, pady=2)

button2_4 = tk.Button(button_frame, text="Ashburn", command=lambda:execute_sql("update T_PARAM set F_VALUE='ASHBURN_XCON' where F_NAME ='INTEGRATEDCARD'"), **button_style)
button2_4.grid(row=0, column=4, padx=2, pady=2)


button3_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='SCALE_ENABLE'"), **button_style)
button3_1.grid(row=1, column=1, padx=2, pady=2)

button3_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='SCALE_ENABLE'"), **button_style)
button3_2.grid(row=1, column=2, padx=2, pady=2)

button4_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='PREPAID'"),**button_style)
button4_1.grid(row=2, column=1, padx=2, pady=2)

button4_2 = tk.Button(button_frame, text="Įjungti",  command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='PREPAID'"),**button_style)
button4_2.grid(row=2, column=2, padx=2, pady=2)

button5_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='SHOW_N18_LABEL'"), **button_style)
button5_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='SHOW_N18_LABEL'"), **button_style)
button5_1.grid(row=3, column=1, padx=2, pady=2)
        
button5_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='SHOW_N18_LABEL'"),**button_style)
button5_2.grid(row=3, column=2, padx=2, pady=2)

button8_1 = tk.Button(button_frame, text="Išjungti",  command=lambda: execute_sql("update T_PARAM set F_VALUE='-' where F_NAME ='PERLAS_PORT'"),**button_style)
button8_1.grid(row=4, column=1, padx=2, pady=2)

button8_2 = tk.Button(button_frame, text="Įjungti",  command=lambda: execute_sql("update T_PARAM set F_VALUE='11000' where F_NAME ='PERLAS_PORT'"),**button_style)
button8_2.grid(row=4, column=2, padx=2, pady=2)


button7_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='CLIENT_DISPLAY_TYPE'"), **button_style)
button7_1.grid(row=5, column=1, padx=2, pady=2)

button7_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='4' where F_NAME ='CLIENT_DISPLAY_TYPE'"), **button_style)
button7_2.grid(row=5, column=2, padx=2, pady=2)

button9_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='DISCOUNTCOUPON'"), **button_style)
button9_1.grid(row=0, column=8, padx=2, pady=2)

button9_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='DISCOUNTCOUPON'"), **button_style)
button9_2.grid(row=0, column=9, padx=2, pady=2)



button10_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='CREDIT3_LEASING'"), **button_style)
button10_1.grid(row=1, column=8, padx=2, pady=2)

button10_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='2' where F_NAME ='CREDIT3_LEASING'"), **button_style)
button10_2.grid(row=1, column=9, padx=2, pady=2)

button11_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='CREDIT4_ENABLED'"), **button_style)
button11_1.grid(row=2, column=8, padx=2, pady=2)

button11_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='CREDIT4_ENABLED'"), **button_style)
button11_2.grid(row=2, column=9, padx=2, pady=2)

button12_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='CREDIT5_ENABLED'"), **button_style)
button12_1.grid(row=3, column=8, padx=2, pady=2)

button12_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='CREDIT5_ENABLED'"), **button_style)
button12_2.grid(row=3, column=9, padx=2, pady=2)

button13_1 = tk.Entry(button_frame, width=8, font=('Arial', 10))
button13_1.grid(row=5, column=8, padx=2, pady=2)
button13_2 = tk.Button(button_frame, text="Keisti", command=lambda:
 execute_sql(f"update T_DEVICE set F_STORENO='{button13_1.get()}';"
    f"update T_PARAM set F_VALUE='{button13_1.get()}' where F_NAME ='DINETAWEB_LOCATION_LOYALTY';"
    f"update T_PARAM set F_VALUE='{button13_1.get()}' where F_NAME ='DINETAWEB_LOCATION'")
 , **button_style)
button13_2.grid(row=5, column=9, padx=2, pady=2)

button14_1 = tk.Entry(button_frame, width=8, font=('Arial', 10))
button14_1.grid(row=6, column=8, padx=2, pady=2)
button14_2 = tk.Button(button_frame, text="Keisti", command=lambda: 
    execute_sql(f"update T_DEVICE set F_POSNO='{button14_1.get()}';"
    f"update T_PARAM set F_VALUE='{button14_1.get()}' where F_NAME ='DINETAWEB_POS_LOYALTY';"
    f"update T_PARAM set F_VALUE='{button14_1.get()}' where F_NAME ='DINETAWEB_POS'")
    , **button_style)
    
button14_2.grid(row=6, column=9, padx=2, pady=2)

button15_1 = tk.Entry(button_frame, width=8, font=('Arial', 10))
button15_1.grid(row=7, column=8, padx=2, pady=2)

button15_2 = tk.Button(button_frame, text="Keisti", command=lambda: 
    execute_sql(f"update T_PARAM set F_VALUE='{button15_1.get()}' where F_NAME ='DINETAWEB_WS_PASSWORD';"
    f"update T_PARAM set F_VALUE='{button15_1.get()}' where F_NAME ='DINETAWEB_WS_PASSWORD_LOYALTY'")
    , **button_style)

button15_2.grid(row=7, column=9, padx=2, pady=2)

button16_1 = tk.Entry(button_frame, width=8, font=('Arial', 10))
button16_1.grid(row=4, column=8, padx=2, pady=2)

button16_2 = tk.Button(button_frame, text="Keisti", command=lambda: 
    execute_sql(f"update T_PARAM set F_VALUE='{button16_1.get()}/ws/dineta_pos/' where F_NAME ='DINETAWEB_WEBSERVICE_URL';"
    f"update T_PARAM set F_VALUE='{button16_1.get()}/ws/dineta_pos/' where F_NAME ='DINETAWEB_WEBSERVICE_URL_LOYALTY'")
    , **button_style)

button16_2.grid(row=4, column=9, padx=2, pady=2)



button17_1 = tk.Entry(button_frame4, width=8, font=('Arial', 10))
button17_1.grid(row=1, column=1, padx=2, pady=2)
button17_2 = tk.Button(button_frame4, text="Keisti", command=lambda:
 execute_sql(f"update T_PARAM set F_VALUE='{button17_1.get()}' where F_NAME ='COM_PORT'")
 , **button_style)
button17_2.grid(row=1, column=2, padx=2, pady=2)


button18_1 = tk.Entry(button_frame4, width=8, font=('Arial', 10))
button18_1.grid(row=2, column=1, padx=2, pady=2)
button18_2 = tk.Button(button_frame4, text="Keisti", command=lambda:
 execute_sql(f"update T_PARAM set F_VALUE='{button18_1.get()}' where F_NAME ='COM_OPEN'")
 , **button_style)
button18_2.grid(row=2, column=2, padx=2, pady=2)


button19_1 = tk.Entry(button_frame, width=8, font=('Arial', 10))
button19_1.grid(row=8, column=8, padx=2, pady=2)

button19_2 = tk.Button(button_frame, text="Keisti", command=lambda:
    execute_sql(f"update T_STORE set F_MAXDISCOUNT='{button19_1.get()}' where ID = (SELECT T_DEVICE.F_STOREID FROM T_DEVICE WHERE T_DEVICE.ID = '1');"),
    **button_style)
button19_2.grid(row=8, column=9, padx=2, pady=2)



button20_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='ALLOW_CHANGE_PRICE'"), **button_style)
button20_1.grid(row=6, column=1, padx=2, pady=2)

button20_2 = tk.Button(button_frame, text="Didinti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='ALLOW_CHANGE_PRICE'"), **button_style)
button20_2.grid(row=6, column=2, padx=2, pady=2)

button20_3 = tk.Button(button_frame, text="Mažint", command=lambda: execute_sql("update T_PARAM set F_VALUE='2' where F_NAME ='ALLOW_CHANGE_PRICE'"),  **button_style)
button20_3.grid(row=6, column=3, padx=2, pady=2)

button20_3 = tk.Button(button_frame, text="Antra", command=lambda: execute_sql("update T_PARAM set F_VALUE='3' where F_NAME ='ALLOW_CHANGE_PRICE'"),  **button_style)
button20_3.grid(row=6, column=4, padx=2, pady=2)


button21_1 = tk.Button(button_frame, text="Išjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='0' where F_NAME ='DISCOUNTCOUPON_ONLINE'"), **button_style)
button21_1.grid(row=7, column=1, padx=2, pady=2)

button21_2 = tk.Button(button_frame, text="Įjungti", command=lambda: execute_sql("update T_PARAM set F_VALUE='1' where F_NAME ='DISCOUNTCOUPON_ONLINE'"), **button_style)
button21_2.grid(row=7, column=2, padx=2, pady=2)


def clear_operations():
    answer = messagebox.askyesno("Patvirtinkite", "DĖMESIO! Bus ištrintos visos operacijos negrįžtamai!")
    if answer:
        execute_sql("delete from T_POSD; delete from T_POSD2; delete from T_POSDDISCOUNT; delete from T_POSHINFO; delete from T_POSHINFO2; delete from T_POSLOG; delete from T_POSZ; delete from T_POSH2; delete from T_POSH; delete from T_COUPONSH; delete from T_COUPONSD; delete from T_COUPONAUTHOR; delete from T_INVOICEINFO; delete from T_VPO;")
        
button6_1 = tk.Button(button_frame2, text="Valyti operacijas sinchronizacijai", command=clear_operations, **button_style2)
button6_1.grid(row=0, column=1, padx=2, pady=2)

def execute_sql_and_prompt(sql):
    if messagebox.askyesno("Patvirtinkite", "DĖMESIO! Bus ištrintos visos operacijos negrįžtamai!"):
        execute_sql(sql)

button6_2 = tk.Button(button_frame2, text="Valyti viską sinchronizacijai", command=lambda: execute_sql_and_prompt("delete from T_POSD delete from T_POSD2 delete from T_POSDDISCOUNT delete from T_POSHINFO delete from T_POSHINFO2 delete from T_POSLOG delete from T_POSZ delete from T_POSH2 delete from T_POSH delete from T_COUPONSH delete from T_COUPONSD delete from T_COUPONAUTHOR delete from T_INVOICEINFO delete from T_VPO delete from T_PRODUCER delete from T_POSADDSTOCK delete from T_PRICE delete from T_BARCODE delete from T_DISCOUNTSTOCKBUY delete from T_DISCOUNTSTOCKNOTBUY delete from T_DISCOUNTSTOCKWIN delete from T_DISCOUNTSTOCKNOTWIN delete from T_STOCK delete from T_STORE delete from T_PARTNER truncate table dbo.T_DISCOUNTCATEGORYBUY truncate table dbo.T_DISCOUNTCATEGORYNOTBUY truncate table dbo.T_DISCOUNTCATEGORYNOTWIN truncate table dbo.T_DISCOUNTCATEGORYWIN truncate table dbo.T_DISCOUNTGROUPNOTBUY truncate table dbo.T_DISCOUNTGROUPBUY truncate table dbo.T_DISCOUNTGROUPNOTWIN truncate table dbo.T_DISCOUNTGROUPWIN truncate table dbo.T_DISCOUNTLOYALTYGROUPNOTWIN truncate table dbo.T_DISCOUNTLOYALTYGROUPWIN truncate table dbo.T_DISCOUNTSTOCKNOTBUY truncate table dbo.T_DISCOUNTSTOCKBUY truncate table dbo.T_DISCOUNTSTOCKNOTWIN truncate table dbo.T_DISCOUNTSTOCKWIN delete from T_GROUP delete from T_UNIT delete from T_SYSTEM delete from T_POST delete from T_USER"), **button_style2)
button6_2.grid(row=0, column=2, padx=2, pady=2)


# Set the background color of the frame as a fallback
button_frame.configure(background="#00A2E8")



# Create the connection status label
connection_status_label = tk.Label(root, text="", font=("Arial", 16))
connection_status_label.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
update_connection_status_label()



# Start the GUI event loop
button_frame.mainloop()
