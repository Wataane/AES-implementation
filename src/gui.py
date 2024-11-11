import tkinter as tk
from tkinter import messagebox
from encryption import aes_encrypt, des_encrypt
from decryption import aes_decrypt, des_decrypt
from Crypto.Random import get_random_bytes

def perform_encryption():
    text = entry.get("1.0", tk.END).strip()
    algorithm = algo_var.get()
    key = get_random_bytes(16) if algorithm == 'AES' else get_random_bytes(8)
    
    try:
        if algorithm == 'AES':
            encrypted_text = aes_encrypt(text, key)
        else:
            encrypted_text = des_encrypt(text, key)
        
        result_text_box.config(state=tk.NORMAL)  
        result_text_box.delete("1.0", tk.END)   
        result_text_box.insert(tk.END, f"Encrypted: {encrypted_text.hex()}\n Key (save for decryption): {key.hex()}")
        result_text_box.config(state=tk.DISABLED)  
        
    
        key_entry.delete(0, tk.END)  
        key_entry.insert(0, key.hex())  
    except Exception as e:
        messagebox.showerror("Error", str(e))

def perform_decryption():
    encrypted_text = entry.get("1.0", tk.END).strip()
    algorithm = algo_var.get()
    key = bytes.fromhex(key_entry.get())  

    try:
        encrypted_bytes = bytes.fromhex(encrypted_text)
        
        if algorithm == 'AES':
            decrypted_text = aes_decrypt(encrypted_bytes, key)
        else:
            decrypted_text = des_decrypt(encrypted_bytes, key)
        
        result_text_box.config(state=tk.NORMAL) 
        result_text_box.delete("1.0", tk.END)   
        result_text_box.insert(tk.END, f"Decrypted: {decrypted_text}")
        result_text_box.config(state=tk.DISABLED)  
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Encryption/Decryption Tool")

entry = tk.Text(app, height=5, width=40)
entry.pack()

algo_var = tk.StringVar(value="AES")
tk.Radiobutton(app, text="AES", variable=algo_var, value="AES").pack()
tk.Radiobutton(app, text="DES", variable=algo_var, value="DES").pack()

encrypt_button = tk.Button(app, text="Encrypt", command=perform_encryption)
encrypt_button.pack()

key_label = tk.Label(app, text="Enter key for decryption:")
key_label.pack()
key_entry = tk.Entry(app, width=40)
key_entry.pack()

decrypt_button = tk.Button(app, text="Decrypt", command=perform_decryption)
decrypt_button.pack()

result_text_box = tk.Text(app, height=5, width=50, wrap="word")
result_text_box.pack()
result_text_box.config(state=tk.DISABLED)  # Make text box read-only

app.mainloop()
