from datetime import datetime
import tkinter as tk
import time
import threading
import random

# ===== CONFIG =====
EMOJI = "🦐"
RARE_EMOIJ = "🍤"
INTERVAL_MINUTES = 10
SPEED_IN_PIXELS = 5
FONT_SIZE = 600
COLOR = "pink"
RARE_COLOR = "orange"

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
    y = screen_height // 2

    text = canvas.create_text(
        x, y,
        text=emoji,
        font=("Segoe UI Emoji", FONT_SIZE),
        anchor="w",
        fill=color
    )

    root.update()

    def animate():
        nonlocal x
        x += SPEED_IN_PIXELS
        canvas.coords(text, x, y)

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