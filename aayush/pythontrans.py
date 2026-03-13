import threading
import customtkinter as ctk
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Initialize the UI
class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("English-Hindi Translator")
        self.geometry("800x500")
        self.resizable(False, False)
        
        # Configure layout weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Premium UI appearance
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Logical State Variables
        self.source_lang = "en"
        self.target_lang = "hi"
        self.source_lang_name = "English"
        self.target_lang_name = "Hindi"

        self.create_widgets()

    def create_widgets(self):
        # --- Top Bar layout ---
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="ew")
        
        # Center the widgets in top_frame
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=0)
        self.top_frame.grid_columnconfigure(2, weight=1)

        self.lbl_source = ctk.CTkLabel(self.top_frame, text=self.source_lang_name, font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_source.grid(row=0, column=0, sticky="e", padx=30)

        # Swap Languages Button
        self.btn_swap = ctk.CTkButton(self.top_frame, text="⇄", width=50, height=40,
                                      font=ctk.CTkFont(size=24, weight="bold"), 
                                      command=self.swap_languages, corner_radius=10)
        self.btn_swap.grid(row=0, column=1)

        self.lbl_target = ctk.CTkLabel(self.top_frame, text=self.target_lang_name, font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_target.grid(row=0, column=2, sticky="w", padx=30)

        # --- Text Areas ---
        # Left side: Source Textbox
        self.textbox_source = ctk.CTkTextbox(self, font=ctk.CTkFont(size=18), wrap="word", corner_radius=15, border_width=1)
        self.textbox_source.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")

        # Right side: Target Textbox (Disabled for reading only)
        self.textbox_target = ctk.CTkTextbox(self, font=ctk.CTkFont(size=18), wrap="word", corner_radius=15, border_width=1, state="disabled")
        self.textbox_target.grid(row=1, column=2, padx=(10, 20), pady=(10, 20), sticky="nsew")

        # --- Bottom Bar ---
        self.btn_translate = ctk.CTkButton(self, text="Translate", height=50, width=200,
                                           font=ctk.CTkFont(size=18, weight="bold"),
                                           command=self.start_translation, corner_radius=10)
        self.btn_translate.grid(row=2, column=0, columnspan=3, pady=(0, 20))

    def swap_languages(self):
        # Swap logical language codes for google translate
        self.source_lang, self.target_lang = self.target_lang, self.source_lang
        # Swap UI names completely 
        self.source_lang_name, self.target_lang_name = self.target_lang_name, self.source_lang_name
        
        # Update Top Labels visually
        self.lbl_source.configure(text=self.source_lang_name)
        self.lbl_target.configure(text=self.target_lang_name)

        # Transfer the typed and translated text
        source_text = self.textbox_source.get("1.0", "end-1c").strip()
        
        self.textbox_target.configure(state="normal")
        target_text = self.textbox_target.get("1.0", "end-1c").strip()

        # Place target text in the source box securely
        self.textbox_source.delete("1.0", "end")
        self.textbox_source.insert("1.0", target_text)

        # Place the old source text block in the new target box securely
        self.textbox_target.delete("1.0", "end")
        self.textbox_target.insert("1.0", source_text)
        self.textbox_target.configure(state="disabled")

    def start_translation(self):
        source_text = self.textbox_source.get("1.0", "end-1c").strip()
        if not source_text:
            messagebox.showwarning("Empty Text", "Please enter some text to translate.")
            return

        # Disable UI to tell user an async operation is running
        self.btn_translate.configure(state="disabled", text="Translating...")
        
        # Do not block main thread (UI freeze otherwise) - use simple threading!
        thread = threading.Thread(target=self.translate_text, args=(source_text,))
        thread.daemon = True
        thread.start()

    def translate_text(self, text):
        try:
            translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)
            result = translator.translate(text)
            
            # Switch back safely into the Tkinter mainloop context!
            self.after(0, self.update_target_text, result)
        except Exception as e:
            self.after(0, self.show_error, str(e))

    def update_target_text(self, translated_text):
        # Ensure we write safely
        self.textbox_target.configure(state="normal")
        self.textbox_target.delete("1.0", "end")
        self.textbox_target.insert("1.0", translated_text)
        self.textbox_target.configure(state="disabled")
        
        self.btn_translate.configure(state="normal", text="Translate")

    def show_error(self, error_msg):
        messagebox.showerror("Translation Error", f"An internet or service error occurred:\n{error_msg}")
        self.btn_translate.configure(state="normal", text="Translate")

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
