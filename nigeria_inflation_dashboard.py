import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "/storage/emulated/0/Download/nigeria_inflation.csv"  # Change if needed

try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# Initialize the Tkinter app
root = tk.Tk()
root.title("Nigeria Inflation Dashboard")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# --- Functions for GUI actions ---
def show_average():
    avg = data["Inflation Rate"].mean()
    messagebox.showinfo("Average Inflation", f"Average: {avg:.2f}%")

def show_highest():
    max_row = data.loc[data["Inflation Rate"].idxmax()]
    messagebox.showinfo("Highest Inflation", f"{int(max_row['Year'])}: {max_row['Inflation Rate']}%")

def show_lowest():
    min_row = data.loc[data["Inflation Rate"].idxmin()]
    messagebox.showinfo("Lowest Inflation", f"{int(min_row['Year'])}: {min_row['Inflation Rate']}%")

def plot_graph():
    plt.figure(figsize=(8, 5))
    plt.plot(data["Year"], data["Inflation Rate"], marker="o", color="green")
    plt.title("Nigeria Inflation Trend")
    plt.xlabel("Year")
    plt.ylabel("Inflation Rate (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --- GUI Buttons ---
tk.Label(root, text="🇳🇬 Nigeria Inflation Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Button(root, text="📈 Show Line Graph", command=plot_graph, width=25, bg="#90ee90").pack(pady=5)
tk.Button(root, text="📊 Average Inflation", command=show_average, width=25, bg="#add8e6").pack(pady=5)
tk.Button(root, text="🔺 Highest Year", command=show_highest, width=25, bg="#ffcccb").pack(pady=5)
tk.Button(root, text="🔻 Lowest Year", command=show_lowest, width=25, bg="#ffe4b5").pack(pady=5)

# Start the app
root.mainloop()