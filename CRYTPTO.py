#crypto code
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def encrypt(message, shift=3):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift=3):
    return encrypt(message, -shift)

def perform_encryption():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END)
        encrypted_message = encrypt(message)
        text2.delete(1.0, END)
        text2.insert(END, encrypted_message)
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

def perform_decryption():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END)
        decrypted_message = decrypt(message)
        text2.delete(1.0, END)
        text2.insert(END, decrypted_message)
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")

def main_screen():
    global code
    global text1
    global text2

    screen = Tk()
    screen.geometry("590x380")
    screen.title("CryptiX")
    screen.configure(bg="lightgrey")

    tab_control = ttk.Notebook(screen)

    main_tab = Frame(tab_control, bg="whitesmoke")
    info_tab = Frame(tab_control, bg="whitesmoke")

    tab_control.add(main_tab, text="Main")
    tab_control.add(info_tab, text="Info")
    tab_control.pack(expand=1, fill="both")

    Label(main_tab, text="Entrer votre message", font=("Helvetica", 12, "bold"), bg="whitesmoke").pack(pady=5)
    text1 = Text(main_tab, font=("Helvetica", 11), wrap=WORD, height=4, width=40, bd=2)
    text1.pack(pady=5)

    Label(main_tab, text="Entrer votre mot de pass", font=("Helvetica", 10, "bold"), bg="whitesmoke").pack(pady=5)
    code = StringVar()
    Entry(main_tab, textvariable=code, width=20, bd=2, font=("Helvetica", 12), show="*").pack(pady=5)

    button_frame = Frame(main_tab, bg="whitesmoke")
    button_frame.pack(pady=5)

    Button(button_frame, text="Crypter",bg="navajowhite",fg="black",font=("Times New Roman", 10, "bold"), compound=LEFT, width=20, command=perform_encryption).pack(side=LEFT, padx=10)
    Button(button_frame, text="Décrypter",bg="navy",fg="white",font=("Times New Roman", 10, "bold"), compound=LEFT, width=20, command=perform_decryption).pack(side=LEFT, padx=10)

    Label(main_tab, text="Resultat Final", font=("Helvetica", 12, "bold"), bg="whitesmoke").pack(pady=5)
    text2 = Text(main_tab, font=("Helvetica", 10), wrap=WORD, height=4, width=40, bd=2)
    text2.pack(pady=5)


    Label(info_tab, text="CryptiX", font=("Helvetica", 16, "bold"), bg="whitesmoke").pack(pady=10)
    Label(info_tab, text="2024/2025  |  v1.0 ", font=("Helvetica", 10), bg="whitesmoke").pack(pady=5)
    Label(info_tab, text="Created by HAITAM BEN DAHMANE IDRISSI\n (Stagiaire ID101)", font=("Helvetica", 10, "bold"), bg="whitesmoke").pack(pady=5)
    Label(info_tab, text="Chiffré et Déchiffré votre message simplement\nPLEASE USE THIS FEATURE DURING THE COMMUNICATION OF TCP SERVER (AS A CLIENT)", font=("Helvetica", 10), bg="whitesmoke").pack(pady=5)

    screen.mainloop()

main_screen()
