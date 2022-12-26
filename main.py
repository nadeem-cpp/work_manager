from tkinter import *
from tkinter import messagebox
import datetime


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# trip to keep track for long and short brakes
trip = 0
timer = None
# to avoid double click
double_clicked = False


def main():

    def time_counter(total):
        if total > 0:
            countdown = datetime.timedelta(seconds=total)
            canvas.itemconfig(timer_text, text=f"{countdown}")
            global timer
            timer = window.after(1000, time_counter, total - 1)
        else:
            global double_clicked
            double_clicked = False
            time_starter()

    def restart():
        try:
            # cancel after function called on timer
            window.after_cancel(timer)
        # if timer is None(at start of programme)
        except ValueError:
            pass
        else:
            canvas.itemconfig(timer_text, text="00:00:00")
            title.config(text="Timer", fg=GREEN)
            global trip
            global double_clicked
            trip = 0
            double_clicked = False

    def time_starter():
        global trip
        global double_clicked
        if not double_clicked:
            double_clicked = True
            trip += 1
            if trip % 8 == 0:
                messagebox.showinfo(title="Take Break!", message=f"Congrats! You have completed 100 minutes\nPlease "
                                                                 f"take a break of {LONG_BREAK_MIN} minutes")
                title.config(text="Break", fg=RED)
                time_counter(LONG_BREAK_MIN * 60)
            elif trip % 2 == 0:
                messagebox.showinfo(title="Take Break!", message=f"Congrats! You have completed 20 minutes of work"
                                                                 f"\nPlease take a break of {SHORT_BREAK_MIN} minutes")
                title.config(text="Break", fg=PINK)
                time_counter(SHORT_BREAK_MIN * 60)
            else:
                # after 1st work
                if trip != 1:
                    messagebox.showinfo(title="Back to Work!", message=f"Hope you enjoyed your break\nProceed "
                                                                       f"with work")
                    title.config(text="Work", fg=GREEN)
                time_counter(WORK_MIN * 60)

    # ##################### UI ############################
    window = Tk()
    # window.geometry("500x400")
    window.minsize(width=505, height=450)
    window.maxsize(width=505, height=450)
    window.title("Pomodoro")
    window.config(padx=100, pady=80, bg=YELLOW)
    # label
    title = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
    title.grid(row=0, column=1)
    # canvas to draw
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    # img path for create_image
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 120, text="00:00:00", font=(FONT_NAME, 30, "bold"), fill="white")
    canvas.grid(row=1, column=1)

    # buttons
    start = Button(text="Start", command=time_starter)
    start.grid(row=2, column=0)
    reset = Button(text="Reset", command=restart)
    reset.grid(row=2, column=2)

    window.mainloop()


if __name__ == '__main__':
    main()
