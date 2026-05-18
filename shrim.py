from datetime import datetime
import tkinter as tk
import time
import threading
import math
import random

# ===== CONFIG =====
EMOJI = "🦐"
RARE_EMOIJ = "🍤"
INTERVAL_MINUTES = 10
SPEED_IN_PIXELS = 4
FONT_SIZE = 600
COLOR = "pink"
RARE_COLOR = "orange"
BOB_AMPLITUDE = 50
BOB_SPEED = 0.05

# ==================

def show_emoji(emoji, color):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    transparent_color = "white"
    root.configure(bg=transparent_color)

    try:
        root.attributes("-transparentcolor", transparent_color)
    except:
        print("Transparent color not supported on this system.")

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0, bg=transparent_color)
    canvas.pack()

    x = -1000
    base_y = screen_height // 2

    text = canvas.create_text(
        x, base_y,
        text=emoji,
        font=("Segoe UI Emoji", FONT_SIZE),
        anchor="w",
        fill=color
    )

    root.update()

    angle = 0.0

    def animate():
        nonlocal x, angle
        x += SPEED_IN_PIXELS
        current_y = base_y + int(BOB_AMPLITUDE * math.sin(angle))
        angle += BOB_SPEED
        canvas.coords(text, x, current_y)

        if x < screen_width + 200:
            root.after(16, animate)
        else:
            root.destroy()

    animate()
    root.mainloop()

def loop():
    while True:
        emoji = EMOJI
        color = COLOR
        if random.randint(1, 100) == 1:
            emoji = RARE_EMOIJ
            color = RARE_COLOR
        print(f"[{datetime.now().strftime('%H:%M')}] " + emoji)
        show_emoji(emoji, color)
        print(f"[{datetime.now().strftime('%H:%M')}] Zzz.z...")
        time.sleep(INTERVAL_MINUTES * 60)

# Run in background thread so it doesn't block
threading.Thread(target=loop, daemon=True).start()

# Keep app alive (invisible root)
while True:
    time.sleep(1)