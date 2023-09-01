import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def roll_dice(num_dice, num_sides):
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

def calculate_variance_and_stddev(num_dice, num_sides, num_trials):
    rolls = [roll_dice(num_dice, num_sides) for _ in range(num_trials)]
    mean = np.mean(rolls)
    squared_deviations = [(roll - mean) ** 2 for roll in rolls]
    variance = np.mean(squared_deviations)
    stddev = np.sqrt(variance)
    return variance, stddev, rolls

def plot_distribution(rolls, num_dice, num_sides, canvas_frame):
    fig, ax = plt.subplots()
    ax.hist(rolls, bins=range(num_dice, num_dice * num_sides + 2), align='left', density=True, alpha=0.7)
    ax.set_xlabel('Total Roll Value')
    ax.set_ylabel('Probability')
    ax.set_title(f'Distribution of {num_dice}d{num_sides} Dice Rolls')
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def calculate_and_display():
    num_dice = int(num_dice_entry.get())
    num_sides = int(num_sides_entry.get())
    num_trials = int(num_trials_entry.get())

    variance, stddev, rolls = calculate_variance_and_stddev(num_dice, num_sides, num_trials)
    variance_label.config(text=f"Variance: {variance:.2f}")
    stddev_label.config(text=f"Standard Deviation: {stddev:.2f}")
    
    plot_distribution(rolls, num_dice, num_sides, canvas_frame)

# Create main window
root = tk.Tk()
root.title("Dice Roll Variance and Standard Deviation Calculator")

# Create and place widgets
num_dice_label = tk.Label(root, text="Number of Dice:")
num_dice_label.pack()

num_dice_entry = ttk.Entry(root)
num_dice_entry.pack()

num_sides_label = tk.Label(root, text="Number of Sides:")
num_sides_label.pack()

num_sides_entry = ttk.Entry(root)
num_sides_entry.pack()

num_trials_label = tk.Label(root, text="Number of Trials:")
num_trials_label.pack()

num_trials_entry = ttk.Entry(root)
num_trials_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.pack()

variance_label = tk.Label(root, text="")
variance_label.pack()

stddev_label = tk.Label(root, text="")
stddev_label.pack()

canvas_frame = tk.Frame(root)
canvas_frame.pack()

root.mainloop()