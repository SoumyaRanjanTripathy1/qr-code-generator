import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    """Generate a QR code based on the input text."""
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some text or a URL!")
        return

    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.thumbnail((200, 200)) 

    # Display QR Code in the preview label
    qr_img = ImageTk.PhotoImage(img)
    qr_label.configure(image=qr_img)
    qr_label.image = qr_img  

def save_qr():
    """Save the generated QR code to a file."""
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please generate a QR Code first!")
        return

    # Open file dialog for saving the QR Code
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
    )
    if file_path:
        # Generate and save QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved to {file_path}")

# Create the GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

# Title Label
title = tk.Label(root, text="QR Code Generator", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Input Field
frame = tk.Frame(root)
frame.pack(pady=10)
entry = tk.Entry(frame, width=35, font=("Helvetica", 14))
entry.pack(side=tk.LEFT, padx=5)
generate_btn = tk.Button(frame, text="Generate", command=generate_qr)
generate_btn.pack(side=tk.RIGHT, padx=5)

# QR Code Display
qr_label = tk.Label(root, text="Your QR Code will appear here", font=("Helvetica", 12), fg="gray")
qr_label.pack(pady=20)

# Save Button
save_btn = tk.Button(root, text="Save QR Code", command=save_qr, font=("Helvetica", 12))
save_btn.pack(pady=10)

# Run the GUI application
root.mainloop()
