""" Project: Pomodor Timer """

import tkinter as tk

# initialize variables
session_count = 0
timer_running = False
timer_id = None
remaining_time = 25 * 60  # default session length in seconds

# timer logic
def countdown():
    global timer_running, timer_id, remaining_time
    if timer_running and remaining_time > 0:
        mins, secs = divmod(remaining_time, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        remaining_time -= 1
        timer_id = window.after(1000, countdown)
    elif remaining_time == 0:
        timer_running = False
        status_label.config(text="Session Done", fg='purple')

# start or resume timer
def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        countdown()
    status_label.config(text="Work", fg='green')

# stop/pause timer
def pause_timer():
    global timer_running, timer_id
    if timer_running:
        window.after_cancel(timer_id)
        timer_running = False
        status_label.config(text="Paused", fg='red')

# reset timer
def reset_timer():
    global session_count, timer_running, timer_id, remaining_time
    if timer_id:
        window.after_cancel(timer_id)
    session_count = 0
    timer_running = False
    remaining_time = 25 * 60
    timer_label.config(text="25:00")
    status_label.config(text="Ready", fg='black')

# create main window
window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("300x300")

# timer label
timer_label = tk.Label(window, text="25:00", font=("Arial", 40))
timer_label.pack(pady=30)

# status label
status_label = tk.Label(window, text="Ready", font=("Arial", 20))
status_label.pack()

# button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# start button
start_button = tk.Button(button_frame, text="Start", command=start_timer, font=("Arial", 14))
start_button.pack(side="left", padx=10)

# stop button
stop_button = tk.Button(button_frame, text="Pause", command=pause_timer, font=("Arial", 14))
stop_button.pack(side="left", padx=10)

# reset button
reset_button = tk.Button(button_frame, text="Reset", command=reset_timer, font=("Arial", 14))
reset_button.pack(side="left", padx=10)

# run the app
window.mainloop()