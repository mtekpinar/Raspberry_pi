# This script creates a GUI using Tkinter to control four LEDs on a Raspberry Pi.
# Each LED will turn on as long as its corresponding button is pressed and turn off when released.

import tkinter as tk
from gpiozero import LED

# --- Hardware Connections ---
# Connect LEDs to GPIO 17, GPIO 18, GPIO 22, and GPIO 27, with current-limiting resistors, then to GND.

# Define the GPIO pins to be used.
gpio_pins = [17, 18, 22, 27]
leds = {} # A dictionary to hold the LED objects.

try:
    # Create an LED object for each specified GPIO pin.
    for pin in gpio_pins:
        leds[pin] = LED(pin)
    print("GPIO Zero LED objects created. Ready to control the LEDs.")
except Exception as e:
    print(f"Warning: Could not initialize GPIO Zero. LED control will be non-functional. Error: {e}")
    # Create a dummy LED class for testing on non-Pi systems.
    class DummyLED:
        def __init__(self, pin):
            self.pin = pin
        def on(self):
            print(f"Dummy LED on GPIO {self.pin}: ON")
        def off(self):
            print(f"Dummy LED on GPIO {self.pin}: OFF")
    for pin in gpio_pins:
        leds[pin] = DummyLED(pin)

# --- Tkinter GUI Functions ---

def turn_led_on(pin, event=None):
    """Turns the LED on when the button is pressed."""
    print(f"Button Pressed: LED on GPIO {pin} ON")
    leds[pin].on()
    
def turn_led_off(pin, event=None):
    """Turns the LED off when the button is released."""
    print(f"Button Released: LED on GPIO {pin} OFF")
    leds[pin].off()
    
# --- Tkinter GUI Setup ---

# Create the main window.
root = tk.Tk()
root.title("Multi-LED Control")
root.geometry("650x650")
root.configure(bg="#2c3e50")

# Manually create and position each button using grid.
# You can now change the text and grid position for each button individually.

# GPIO 17 Button
button_17 = tk.Button(
    root,
    text="SOL",
    bg="#3498db",
    fg="white",
    font=("Helvetica", 12, "bold"),
    width=15,
    height=3,
    relief="raised",
    bd=3,
)
button_17.grid(row=1, column=0, padx=20, pady=50)
button_17.bind("<Button-1>", lambda event: turn_led_on(17, event))
button_17.bind("<ButtonRelease-1>", lambda event: turn_led_off(17, event))

# GPIO 18 Button
button_18 = tk.Button(
    root,
    text="Ileri",
    bg="#3498db",
    fg="white",
    font=("Helvetica", 12, "bold"),
    width=15,
    height=3,
    relief="raised",
    bd=3,
)
button_18.grid(row=0, column=1, padx=20, pady=50)
button_18.bind("<Button-1>", lambda event: turn_led_on(18, event))
button_18.bind("<ButtonRelease-1>", lambda event: turn_led_off(18, event))

# GPIO 22 Button
button_22 = tk.Button(
    root,
    text="Geri",
    bg="#3498db",
    fg="white",
    font=("Helvetica", 12, "bold"),
    width=15,
    height=3,
    relief="raised",
    bd=3,
)
button_22.grid(row=2, column=1, padx=20, pady=50)
button_22.bind("<Button-1>", lambda event: turn_led_on(22, event))
button_22.bind("<ButtonRelease-1>", lambda event: turn_led_off(22, event))

# GPIO 27 Button
button_27 = tk.Button(
    root,
    text="Sağ",
    bg="#3498db",
    fg="white",
    font=("Helvetica", 12, "bold"),
    width=15,
    height=3,
    relief="raised",
    bd=3,
)
button_27.grid(row=1, column=2, padx=20, pady=50)
button_27.bind("<Button-1>", lambda event: turn_led_on(27, event))
button_27.bind("<ButtonRelease-1>", lambda event: turn_led_off(27, event))


# Start the Tkinter event loop.
root.mainloop()

# Cleanup on close.
for led in leds.values():
    try:
        led.close()
        print(f"GPIO Zero LED object for pin {led.pin} closed.")
    except AttributeError:
        pass # Dummy LED has no close() method.
