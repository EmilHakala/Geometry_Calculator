import math
import tkinter as tk
from tkinter import font


def calculate_circle_area(radius):
  return math.pi * radius**2


def calculate_circle_circumference(radius):
  return 2 * math.pi * radius


def calculate_rectangle_area(length, width):
  return length * width


def calculate_rectangle_circumference(length, width):
  return 2 * (length + width)


def calculate_triangle_area(base, height):
  return 0.5 * base * height


def calculate_triangle_circumference(base, height, hypotenuse=None):
  if hypotenuse is None:
    return base + height + math.sqrt(base**2 + height**2)
  else:
    return base + height + hypotenuse


def update_input_fields(*args):
  shape = shape_var.get()

  if shape == "Circle":
    radius_label.pack()
    radius_entry.pack()
    length_label.pack_forget()
    length_entry.pack_forget()
    width_label.pack_forget()
    width_entry.pack_forget()
    base_label.pack_forget()
    base_entry.pack_forget()
    height_label.pack_forget()
    height_entry.pack_forget()
    hypotenuse_label.pack_forget()
    hypotenuse_entry.pack_forget()
  elif shape == "Rectangle":
    radius_label.pack_forget()
    radius_entry.pack_forget()
    length_label.pack()
    length_entry.pack()
    width_label.pack()
    width_entry.pack()
    base_label.pack_forget()
    base_entry.pack_forget()
    height_label.pack_forget()
    height_entry.pack_forget()
    hypotenuse_label.pack_forget()
    hypotenuse_entry.pack_forget()
  elif shape == "Triangle":
    radius_label.pack_forget()
    radius_entry.pack_forget()
    length_label.pack_forget()
    length_entry.pack_forget()
    width_label.pack_forget()
    width_entry.pack_forget()
    base_label.pack()
    base_entry.pack()
    height_label.pack()
    height_entry.pack()
    hypotenuse_label.pack()
    hypotenuse_entry.pack()


def calculate_button_clicked():
  shape = shape_var.get()

  if shape == "Circle":
    radius = float(radius_entry.get())
    area = calculate_circle_area(radius)
    circumference = calculate_circle_circumference(radius)
  elif shape == "Rectangle":
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = calculate_rectangle_area(length, width)
    circumference = calculate_rectangle_circumference(length, width)
  elif shape == "Triangle":
    base = float(base_entry.get())
    height = float(height_entry.get())
    hypotenuse = hypotenuse_entry.get()
    if hypotenuse:
      hypotenuse = float(hypotenuse)
      circumference = calculate_triangle_circumference(base, height,
                                                       hypotenuse)
    else:
      circumference = calculate_triangle_circumference(base, height)
    area = calculate_triangle_area(base, height)

  result_label.config(text=f"Area: {area}\nCircumference: {circumference}")


# GUI setup
window = tk.Tk()
window.title("Geometric Shape Calculator")
window.geometry("400x400")  # Set the window size

# Font size
font_size = font.Font(size=12)

# Add padding to the window and all widgets
window.configure(padx=20, pady=20)

shape_var = tk.StringVar()
shape_var.set("Circle")
shape_var.trace("w", update_input_fields)

shape_label = tk.Label(window, text="Select Shape:", font=font_size)
shape_label.pack()

shape_option_menu = tk.OptionMenu(window, shape_var, "Circle", "Rectangle",
                                  "Triangle")
shape_option_menu.config(font=font_size)
shape_option_menu.pack()

radius_label = tk.Label(window, text="Radius:", font=font_size)
radius_entry = tk.Entry(window, font=font_size)

length_label = tk.Label(window, text="Length:", font=font_size)
length_entry = tk.Entry(window, font=font_size)

width_label = tk.Label(window, text="Width:", font=font_size)
width_entry = tk.Entry(window, font=font_size)

base_label = tk.Label(window, text="Base:", font=font_size)
base_entry = tk.Entry(window, font=font_size)

height_label = tk.Label(window, text="Height:", font=font_size)
height_entry = tk.Entry(window, font=font_size)

hypotenuse_label = tk.Label(window, text="Hypotenuse:", font=font_size)
hypotenuse_entry = tk.Entry(window, font=font_size)

calculate_button = tk.Button(window,
                             text="Calculate",
                             command=calculate_button_clicked,
                             font=font_size)
calculate_button.pack()

result_label = tk.Label(window, text="Area: ", font=font_size)
result_label.pack()

update_input_fields(
)

window.mainloop()
