import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(count_text,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_sec)
    elif reps % 2 != 0:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sek = count % 60
    if count_sek < 10:
        count_sek = f"0{count_sek}"
    canvas.itemconfig(count_text, text=f"{count_min}:{count_sek}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_label.config(text=(reps//2)*"✔")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=70, pady=40, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", font=("Calibri", 45, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_label = tk.Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

start_button = tk.Button(text="Start", width=8, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", width=8, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
