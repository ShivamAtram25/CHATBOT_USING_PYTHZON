import tkinter as tk
from tkinter import scrolledtext
import cohere

# === Cohere API CONFIGURATION ===
co = cohere.Client("SderZMSzs5pN6rcYptXBGOZ1llgZbqjZz3KIR8Fe")  # 🔑 Replace with your actual API key

def call_chatbot_api(message):
    try:
        response = co.chat(message=message)
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"

# === Chat Function ===
def send_message():
    user_message = entry_box.get().strip()
    if not user_message:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_message}\n", "user")

    bot_response = call_chatbot_api(user_message)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n", "bot")

    chat_window.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)
    chat_window.yview(tk.END)

# === GUI SETUP ===
root = tk.Tk()
root.title("Cohere ChatBot")
root.geometry("600x650")
root.resizable(False, False)
root.config(bg="#f0f0f0")

chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 13), bg="#ffffff", fg="#000000", padx=10, pady=10)
chat_window.place(x=10, y=10, width=580, height=540)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.place(x=10, y=570, width=470, height=40)
entry_box.focus()

send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#007ACC", fg="white", command=send_message)
send_button.place(x=490, y=570, width=90, height=40)

root.bind('<Return>', lambda event: send_message())
root.mainloop()
