from PIL import Image, ImageFile, ImageTk
import matplotlib.pyplot as plt
import tkinter as tk

from _nearest_neighbour import nearest_neighbor_interpolation
from _bilinear import bilinear_interpolation
from _bicubic import bicubic_interpolation
from _lanczos import lanczos_interpolation

# Setting Attribute
ImageFile.LOAD_TRUNCATED_IMAGES = True

def display_image_with_title(img, title, kill=0,duration=5000):

    root = tk.Tk()
    root.title(title)
    root.configure(bg="#282c34")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width // 2
    window_height = screen_height // 2 + 50

    x_position = screen_width - window_width
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}")
    root.geometry(f"+{x_position}+{y_position}")

    img = img.resize((window_width, window_height - 50), Image.ADAPTIVE)

    tk_img = ImageTk.PhotoImage(img)

    title_label = tk.Label(root, text=title, font=("Courier", 14, 'bold'), bg="#282c34", fg="white")
    title_label.pack(side="top", pady=10)
    
    img_label = tk.Label(root, image=tk_img)
    img_label.pack(side="top", padx=10, pady=10)

    if kill : root.after(duration, root.destroy)
    root.mainloop()


def display_demo_with_titles(image_matrix, titles) :

    fig = plt.figure(figsize=(8, 8))
    columns = 2
    rows = 3
    for i in range(1, columns*rows):
        fig.add_subplot(rows, columns, i)
        plt.imshow(image_matrix[i-1], cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.title(titles[i-1])
    plt.tight_layout()
    plt.show()