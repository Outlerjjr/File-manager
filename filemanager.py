import customtkinter as ctk
import string
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from customtkinter import filedialog
import os
import keyboard
import pyperclip  
import screen_brightness_control as pct
import shutil
import zipfile
window =ctk.CTk()
#window.iconbitmap('C:\\Users\\User\\Downloads\\Capture6.ico')
window.title('File-Manager')
window.geometry('276x280')
import pyttsx3
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
title_label = ctk.CTkLabel(window,text = 'File-Manager',font = ('Roboto',24))
Control_panel_button =ctk.CTkButton(window,text = 'Control panel')
Backup_button =ctk.CTkButton(window,text = ' Backup')
feedback_button = ctk.CTkButton(window,text = 'Feedback')
def distributor1_window():
    root = tk.Tk()
    root.title("App distributor")
    
    def select_directory():
        directory = filedialog.askdirectory()
        if directory:
            organize_apps(directory)
        messagebox.showinfo('File Distributor','Files distributed successfully!')
    
    def organize_apps(directory):
     extensions = {}
     for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = os.path.splitext(filename)[1][1:].lower()
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

     for extension, filenames in extensions.items():
        extension_directory = os.path.join(directory, extension)
        os.makedirs(extension_directory, exist_ok=True)
        for filename in filenames:
            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(extension_directory, filename)
            os.rename(source_path, destination_path)
        
        
    label = tk.Label(root, text="Select a directory:")
    label.pack()
    
    select_button = tk.Button(root, text="Select", command=select_directory)
    select_button.pack()

    root.mainloop()
def generate_strong_password(key_entry):
    password_length = 12
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    key_entry.delete(0, END)
    key_entry.insert(0, password)

def copy_password(key_entry):
    password = key_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copy Password", "Password copied to clipboard!")

def encrypt_file(file_path, key):
    encrypted_text = ""
    key_length = len(key)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        for i, char in enumerate(text):
            key_char = key[i % key_length]
            encrypted_char = chr((ord(char) + ord(key_char)) % 1114112)  
            encrypted_text += encrypted_char

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

def encrypt_files(file_paths, key):
    txt_files_found = False  
    for file_path in file_paths:
        if file_path.endswith(".txt"):
            txt_files_found = True
            encrypt_file(file_path, key)
    if txt_files_found:
        messagebox.showinfo("Encryption", "Files encrypted successfully!")
    else:
        messagebox.showerror("Error", "No .txt files selected.")

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Text Files", "*.txt")])
    if file_paths:
        ask_key(file_paths)

def ask_key(file_paths):
    key_window = Tk()
    key_window.title("Enter Encryption Key")
    key_label = Label(key_window, text="Enter the encryption key:")
    key_label.pack()
    key_entry = Entry(key_window, show="*")
    key_entry.pack()
    generate_button = Button(key_window, text="Generate a Strong Password", command=lambda: generate_strong_password(key_entry))
    generate_button.pack()
    copy_button = Button(key_window, text="Copy Password", command=lambda: copy_password(key_entry))
    copy_button.pack()
    encrypt_button = Button(key_window, text="Encrypt", command=lambda: encrypt_files(file_paths, key_entry.get()))
    encrypt_button.pack()

def run_encryptor_application():
    encryptor_root = Tk()
    encryptor_root.title("File Encryption")
    label = Label(encryptor_root, text="Select text files:")
    label.pack()
    select_button = Button(encryptor_root, text="Select", command=select_files)
    select_button.pack()
    encryptor_root.mainloop()        
def functions_menu():
    functions_window = ctk.CTk()
    #functions_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture2.ico')
    functions_window.title('Functions')
    def encrypt_file(file_path, key):
     encrypted_text = ""

     with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        for char in text:
            encrypted_char = chr((ord(char) + ord(key)) % 1114112) 
            encrypted_text += encrypted_char

     with open(file_path, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    def decrypt_file(file_path, key):
     decrypted_text = ""
     key_length = len(key)

     with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        for i, char in enumerate(text):
            key_char = key[i % key_length]
            decrypted_char = chr((ord(char) - ord(key_char)) % 1114112)  
            decrypted_text += decrypted_char

     with open(file_path, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    def decrypt_files(file_paths, key):
     txt_files_found = False  

     for file_path in file_paths:
        if file_path.endswith(".txt"):
         txt_files_found = True
         decrypt_file(file_path, key)

     if txt_files_found:
        messagebox.showinfo("Decryption", "Files decrypted successfully!")
     else:
        messagebox.showerror("Error", "No .txt files selected.")

    def select_files():
     file_paths = filedialog.askopenfilenames(filetypes=[("Text Files", "*.txt")])
     if file_paths:
        ask_key(file_paths)

    def ask_key(file_paths):
     key_window = Toplevel()
     key_window.title("Enter Decryption Key")

     key_label = Label(key_window, text="Enter the decryption key:")
     key_label.pack()

     key_entry = Entry(key_window, show="*")
     key_entry.pack()

     decrypt_button = Button(key_window, text="Decrypt", command=lambda: decrypt_files(file_paths, key_entry.get()))
     decrypt_button.pack()

    def run_decryptor_application():
     decryptor_root = Tk()
     decryptor_root.title("File Decryption")

     label = Label(decryptor_root, text="Select text files to decrypt:")
     label.pack()

     select_button = Button(decryptor_root, text="Select", command=select_files)
     select_button.pack()

     decryptor_root.mainloop()
    
    button1 = ctk.CTkButton(functions_window, text="Distributor",command=distributor1_window)
    button2 = ctk.CTkButton(functions_window, text="Encryptor",command=run_encryptor_application)
    button3 = ctk.CTkButton(functions_window, text="Decryptor",command= run_decryptor_application)


    button1.grid(row=0, column=0, padx=10, pady=10)
    button2.grid(row=0, column=1, padx=10, pady=10)
    button3.grid(row=0, column=2, padx=10, pady=10)
    functions_window.mainloop()
functions_button =ctk.CTkButton(window,text = 'Functions',command=functions_menu)
Control_panel_button =ctk.CTkButton(window,text = 'Control panel')    
def file_paths_menu():
    file_paths_window = ctk.CTk()
    #file_paths_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture9.ico')
    file_paths_window.title('File-Path-Viewer')
    file_paths_window.geometry('250x150')
    file_question_label = ctk.CTkLabel(file_paths_window,text = 'Select the file: ',font = ('Roboto',20),justify = 'center')
    file_question_label.pack(anchor = 'n',pady = 12)
    file_path_search_result = ctk.CTkLabel(file_paths_window,text = '',font = ('Roboto',20))
    def path_viewer():
     from tkinter import filedialog
     path = filedialog.askopenfilename()
     if path:
        path1 = os.path.abspath(path)
        messagebox.showinfo("Path-Found!", f"The path is:\n\n{path1}")
        pyperclip.copy(path1)
        show_button = ctk.CTkButton(file_paths_window,text = 'Copy-path')
        show_button.pack(pady=16)  
        def copy_path_to_clipborard():
           window.clipboard_clear()
           window.clipboard_append(path1)
           window.update()
           zero =''
           messagebox.showinfo("Path-Viewer!", f"Path copied to clipboard{zero}")
        show_button.configure(command = copy_path_to_clipborard)
    def open_tkinter_window():
     file_path_window_2 = tk.Tk()
     file_path_window_2.title("File-path-viewer")
     #file_path_window_2.iconbitmap('C:\\Users\\User\\Downloads\\Capture9.ico')
     select_button2 = tk.Button(file_path_window_2, text="Select File/Folder", command=path_viewer)
     select_button2.pack(pady=20)
     file_path_window_2.mainloop()
    select_button =ctk.CTkButton(file_paths_window,text = 'Select',command= open_tkinter_window)
    select_button.pack(pady = 5)
    file_paths_window.mainloop()
file_path_button =ctk.CTkButton(window,text = 'Files Path',command= file_paths_menu)
def compress_file():
     file_path = filedialog.askopenfilename()
     with zipfile.ZipFile(file_path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path, arcname=file_path.split('/')[-1])
     messagebox.showinfo('File Compressor-Decompressor',f'File compressed successfully')
def decompress_file():
    file_path = filedialog.askopenfilename()
    extract_directory = filedialog.askdirectory()
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(extract_directory)
    messagebox.showinfo('File Compressor-Decompressor',f'File decompressed successfully')
def open_compressor_decompressor_window():
    Compressor_Decompresser_window = ctk.CTk()
    Compressor_Decompresser_window.geometry('230x105')
    #Compressor_Decompresser_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture25.ico')
    Compressor_Decompresser_window.title("File Compressor-Decompressor")
    compress_button = ctk.CTkButton(Compressor_Decompresser_window, text="Compress", command=compress_file)
    compress_button.pack(pady=10)
    decompress_button = ctk.CTkButton(Compressor_Decompresser_window, text="Decompress", command=decompress_file)
    decompress_button.pack(pady=10)
    Compressor_Decompresser_window.mainloop()
Compressor_decompressor_button =ctk.CTkButton(window,text = 'Compressor',command =open_compressor_decompressor_window )
def explanation_video_menu():
   explanation_video_window = ctk.CTk()
   #explanation_video_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture11.ico')
   explanation_video_window.title('Explanation-Video')
   explanation_video_window.geometry('300x300')
   explanation_video_window.mainloop()
Explanation_video_button = ctk.CTkButton(window,text = 'Explanation Video',command = explanation_video_menu)
def feedback_menu():
   feedback_window = ctk.CTk()
   #feedback_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture7.ico')
   feedback_window.title('Feedback')
   feedback_window.geometry('300x90')
   feedback_lable = ctk.CTkLabel(feedback_window,text = 'Your feedback is important!', font = ("Roboto",14), justify = 'center')
   feedback_lable.pack(pady = 6)
   #feedback_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture13.ico')
   def save_text(event):
    text = entry.get()
    entry.delete(0,'end')
    with open("Feedbacks.txt", "a") as file:
        file.write(text + "\n")
   entry = ctk.CTkEntry(feedback_window)
   entered_file_name = entry.get()
   entry.pack(pady = 1,padx = 90,anchor = 'n')
   entry.bind("<Return>",save_text)
   def enter_check(event):
    if event.keysym=='Return':
           feedback_lable.configure(text = 'Thanks for your feedback!!!!')
   feedback_window.bind("<Key>", enter_check)
   feedback_window.mainloop()
feedback_button = ctk.CTkButton(window,text = 'Feedback',command=feedback_menu)
def ControlPanel_menu():
    ControlPanel_window = ctk.CTk()
    #ControlPanel_window.iconbitmap('C:\\Users\\User\\Downloads\\Capture3.ico')
    ControlPanel_window.title('Control-Panel')
    ControlPanel_window.geometry('300x150')
    Appearanc_mode_label =ctk.CTkLabel(ControlPanel_window,text = 'Appearance-mode:',font = ('Roboto',14))
    Volume_label = ctk.CTkLabel(ControlPanel_window,text = 'Brightness:',font = ('Roboto',14))
    Volume_label.pack(anchor = 'n',pady = 4)
    def update_variable(value):
     global slider_value
     slider_value = int(value)
     pct.set_brightness(slider_value)
    slider = ctk.CTkSlider(ControlPanel_window, from_=0, to=100, command= update_variable)
    slider.pack()
    Appearanc_mode_label.pack(anchor = 'n',pady = 8)
    optionmenu_var = ctk.StringVar(value="Appearance-Mode")  
    def optionmenu_callback(choice):
     if choice == 'Dark':
        ctk.set_appearance_mode('dark')
     elif choice == 'Light':
        ctk.set_appearance_mode('light')
     elif choice == 'System':
        ctk.set_appearance_mode('system')
    combobox = ctk.CTkOptionMenu(master=    ControlPanel_window,
                                       values=["Dark", "Light",'System'],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
    combobox.pack(padx=20,pady = 0)
    ControlPanel_window.mainloop()
Control_panel_button =ctk.CTkButton(window,text = 'Control panel',command=ControlPanel_menu)  
title_label.pack(pady = 10,anchor = 'n')
functions_button.pack(pady = 10,anchor = 'n')
Control_panel_button.pack(pady = 10,anchor = 'n')
file_path_button.pack(pady = 10,anchor = 'n')
Compressor_decompressor_button.pack(pady = 10,anchor = 'n')
window.mainloop()