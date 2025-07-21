import customtkinter as ctk

class CaesarCipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CAESER CIPHER ENCRYPTION/DECRYTION TOOL")
        self.geometry("600x550")
        ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light", "System"
        ctk.set_default_color_theme("D:/Python materials/python practice/cc/nordic_theme.json")  # Options: "blue", "dark-blue", "green"

        # Title Label
        self.label_title = ctk.CTkLabel(self, text="CAESER CIPHER ENCRYPTION/DECRYPTION", font=("Bitcount Grid Single Light Open", 24,"bold"))
        self.label_title.pack(pady=15)

        # Input Text Box
        self.label_original_text = ctk.CTkLabel(self, text="Input text:", font=("courier new", 16))
        self.label_original_text.pack(pady=(20,5))
        self.entry_text = ctk.CTkTextbox(self, width=500, height=100)
        self.entry_text.pack(pady=10)

        # Key Entry
        self.label_key = ctk.CTkLabel(self, text="Key (Shift 1-25):", font=("courier new", 16))
        self.label_key.pack(pady=(10, 0))
        self.spin_key = ctk.CTkTextbox(self, width=100, height=20)
        self.spin_key.pack(pady=10)
        # Buttons
        self.frame_buttons = ctk.CTkFrame(self)
        self.frame_buttons.pack(pady=10)
        self.btn_encrypt = ctk.CTkButton(self.frame_buttons, text="Encrypt",font=("Consolas",14) ,command=self.encrypt_text)
        self.btn_encrypt.grid(row=0, column=0, padx=20)
        self.btn_decrypt = ctk.CTkButton(self.frame_buttons, text="Decrypt",font=("Consolas",14), command=self.decrypt_text)
        self.btn_decrypt.grid(row=0, column=1, padx=20)

        # Result Label and Box
        self.label_result = ctk.CTkLabel(self, text="Result:", font=("courier new", 16))
        self.label_result.pack(pady=(20,5))
        self.text_result = ctk.CTkTextbox(self, width=500, height=100, state="disabled")
        self.text_result.pack(pady=10)

    def caesar_cipher(self, text, key, mode):
        result = ""
        key = int(key) % 26
        if mode == 'decrypt':
            key = -key
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + key) % 26 + base)
            else:
                result += char
        return result

    def encrypt_text(self):
        text = self.entry_text.get("1.0","end").strip()
        key = self.spin_key.get("1.0","end")
        encrypted = self.caesar_cipher(text, key, 'encrypt')
        self.text_result.configure(state="normal")
        self.text_result.delete("1.0","end")
        self.text_result.insert("1.0", encrypted)
        self.text_result.configure(state="disabled")

    def decrypt_text(self):
        text = self.entry_text.get("1.0","end").strip()
        key = self.spin_key.get("1.0","end")
        decrypted = self.caesar_cipher(text, key, 'decrypt')
        self.text_result.configure(state="normal")
        self.text_result.delete("1.0","end")
        self.text_result.insert("1.0", decrypted)
        self.text_result.configure(state="disabled")

if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()
