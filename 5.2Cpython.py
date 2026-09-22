import tkinter as tk
from gpiozero import PWMLED

# Living room LED connected to GPIO18
led = PWMLED(18)


# Change LED intensity
def change_intensity(value):
    intensity = float(value) / 100
    led.value = intensity
    intensity_label.config(
        text=f"Intensity: {int(value)}%"
    )


# Turn LED off and close program
def exit_program():
    led.off()
    root.destroy()


# Create GUI window
root = tk.Tk()

root.title("Living Room Light Control")
root.geometry("500x300")


# Title
title_label = tk.Label(
    root,
    text="Living Room Light",
    font=("Arial", 20)
)

title_label.pack(pady=20)


# Intensity label
intensity_label = tk.Label(
    root,
    text="Intensity: 0%",
    font=("Arial", 14)
)

intensity_label.pack()


# Slider
slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=350,
    command=change_intensity
)

slider.pack(pady=20)


# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    command=exit_program
)

exit_button.pack(pady=10)


# Start GUI
root.mainloop()