from tkinter import *
from PIL import Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#DCC7AA"
FONT_NAME = "Boulder"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
lap = 0
GAME_ON = True

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global lap
    global GAME_ON
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    while lap < 8 :
        if lap == 0 or lap % 2 == 1 :
            count_down(work_sec)
        elif lap % 2 == 0 :
            count_down(short_break)
        elif lap == 8 :
            count_down(long_break)
        lap = lap + 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_min)) == 1 :
        count_min = f"0{count_min}"

    if len(str(count_sec)) == 1 :
        count_sec = f"0{count_sec}"

    tomato_canvas.itemconfig(timer_window, text=f"{count_min}:{count_sec}")

    print(count)
    if count > 0:
        window.after(10, count_down, count - 1)

    tomato_emoji = Label(
        text=f"Laps = {lap}/5 ",
        font=("Segoe UI Emoji", 20),  # larger size for clarity
        bg=YELLOW,
    )
    tomato_emoji.place(x=700, y=525)

# ---------------------------- UI SETUP ------------------------------- #
# Set window size (width x height)
window_width = 850
window_height = 600

window = Tk()

window.title("Pomodoro Tracker by satyajit")
window.minsize(width=window_width,height=window_height)
window.config(bg="#DCC7AA")

# windo open to center

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position x and y coordinates
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Optional: Make window not resizable
window.resizable(False, False)


# fetching images
tomato_stage_0 = PhotoImage(file="Tomato_stage_0.png")
tomato_stage_1 = PhotoImage(file="Tomato_stage_1.png")
tomato_stage_2 = PhotoImage(file="Tomato_stage_2.png")
tomato_stage_3 = PhotoImage(file="Tomato_stage_3.png")
tomato_stage_4 = PhotoImage(file="Tomato_stage_4.png")
tomato_stage_5 = PhotoImage(file="Tomato_stage_5.png")

Trophy_image = PhotoImage(file="Trophy.png")
original = Image.open("tomato.png").convert("RGBA")

# Image rendering
tomato_canvas = Canvas(width=700, height=600, highlightthickness=0, bg=YELLOW)
tomato_canvas.create_image(350, 300, image=tomato_stage_0)
tomato_canvas.grid(row=0, column=0)

# Text on the image
timer_window = tomato_canvas.create_text(360,100, text="00:00",font=(FONT_NAME,50,"bold"), fill="white")

# buttons showing
button_start = Button(text="start",width=10, font=(FONT_NAME,15), highlightthickness=0,command=start_timer)
button_start.place(x=50,y=550)

button_stop = Button(text="pause",width=10, font=(FONT_NAME,15), highlightthickness=0)
button_stop.place(x=300,y=550)

button_reset = Button(text="reset",width=10, font=(FONT_NAME,15), highlightthickness=0)
button_reset.place(x=550,y=550)

# trees showing
trophy_canvas1 = Canvas(width=160, height=160, highlightthickness=0, bg=YELLOW)
trophy_canvas1.create_image(70, 80, image=Trophy_image)
trophy_canvas1.place(x=700, y=0)

trophy_canvas2 = Canvas(width=160, height=160, highlightthickness=0, bg=YELLOW)
trophy_canvas2.create_image(70, 80, image=Trophy_image)
trophy_canvas2.place(x=700, y=162)

trophy_canvas3 = Canvas(width=160, height=160, highlightthickness=0, bg=YELLOW)
trophy_canvas3.create_image(70, 80, image=Trophy_image)
trophy_canvas3.place(x=700, y=324)




window.mainloop()