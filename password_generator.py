import customtkinter as ctk
import random
import string

# Set appearance and theme
ctk.set_appearance_mode("dark")  # Modes: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern PassGen")
        self.geometry("400x300")

        # UI Layout
        self.label = ctk.CTkLabel(self, text="Password Length:", font=("Arial", 16))
        self.label.pack(pady=(20, 5))

        self.length_entry = ctk.CTkEntry(
            self, placeholder_text="Enter length (e.g. 12)"
        )
        self.length_entry.pack(pady=10)

        self.generate_button = ctk.CTkButton(
            self, text="Generate Password", command=self.generate_pass
        )
        self.generate_button.pack(pady=20)

        # Result field (ReadOnly so users can't type in it, but can copy from it)
        self.result_entry = ctk.CTkEntry(
            self, width=300, font=("Consolas", 14), justify="center"
        )
        self.result_entry.pack(pady=10)

    def generate_pass(self):
        char_set = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=`~;:<>?,."'

        try:
            length = int(self.length_entry.get())
            password = "".join(random.choice(char_set) for _ in range(length))

            # Update the result entry
            self.result_entry.delete(0, "end")
            self.result_entry.insert(0, password)
        except ValueError:
            self.result_entry.delete(0, "end")
            self.result_entry.insert(0, "Please enter a valid number!")


if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
