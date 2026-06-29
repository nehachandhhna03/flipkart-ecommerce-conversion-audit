import tkinter as tk
from tkinter import messagebox

def homepage():
    messagebox.showinfo(
        "Homepage Audit",
        "✓ Clean homepage\n"
        "✓ Strong search bar\n"
        "✗ Too many promotional banners\n"
        "Suggestion: Reduce clutter."
    )

def product():
    messagebox.showinfo(
        "Product Page Audit",
        "✓ Good product images\n"
        "✓ Ratings available\n"
        "✗ Product description can be improved."
    )

def checkout():
    messagebox.showinfo(
        "Checkout Audit",
        "✓ Multiple payment options\n"
        "✓ Fast checkout\n"
        "✗ Too many checkout steps."
    )

def recommendations():
    messagebox.showinfo(
        "Recommendations",
        "- Simplify navigation\n"
        "- Reduce banner overload\n"
        "- Improve product filters\n"
        "- Faster checkout process"
    )

root = tk.Tk()
root.title("Flipkart E-Commerce Conversion Audit")
root.geometry("600x500")
root.configure(bg="#EAF4FF")

title = tk.Label(
    root,
    text="Flipkart Conversion Audit",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF",
    fg="navy"
)
title.pack(pady=20)

buttons = [
    ("Homepage Audit", homepage),
    ("Product Page Audit", product),
    ("Checkout Audit", checkout),
    ("Recommendations", recommendations),
]

for text, cmd in buttons:
    tk.Button(
        root,
        text=text,
        width=28,
        height=2,
        font=("Arial", 13),
        command=cmd
    ).pack(pady=10)

tk.Button(
    root,
    text="Exit",
    width=28,
    height=2,
    bg="red",
    fg="white",
    font=("Arial", 13),
    command=root.destroy
).pack(pady=20)

root.mainloop()