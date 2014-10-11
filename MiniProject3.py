# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0  # basic time counter
is_running = False  # indicator of stopwatch status
total_stops = 0  # counter of total stops
good_stops = 0  # counter of good stops


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """format the time. return a string of format m:ss.ms"""
    if t < 10:  # less than 1 sec
        t_in_min = 0
        t_in_sec = 0
        t_in_tenth_sec = t
    elif t < 600:  # less than 1 min
        t_in_min = 0
        t_in_sec = t / 10
        t_in_tenth_sec = t % 10
    else:  # larger than 1 min
        t_in_min = t / 600
        t_in_sec = (t - t_in_min * 600) / 10
        t_in_tenth_sec = (t - t_in_min * 600) % 10

    return str(t_in_min) + ":" + format_t_in_sec(t_in_sec) + "." + str(t_in_tenth_sec)


def format_t_in_sec(t_in_sec):
    """format the time in sec. return a string of format ss"""
    if t_in_sec < 10:
        return "0" + str(t_in_sec)
    else:
        return str(t_in_sec)


def format_stops():
    """return a string of format x/y"""
    return str(good_stops) + "/" + str(total_stops)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_watch():
    global is_running
    timer.start()
    is_running = True


def stop_watch():
    global is_running
    global total_stops
    global good_stops

    timer.stop()
    if is_running:
        is_running = False

        # count stops
        total_stops += 1

        # count good stops
        if time % 10 == 0:
            good_stops += 1


def reset_watch():
    global time
    global total_stops
    global good_stops
    global is_running

    # stop timer and change status
    timer.stop()
    is_running = False

    # reset counters
    total_stops = 0
    good_stops = 0
    time = 0


# define event handler for timer with 0.1 sec interval
def increment_time():
    global time
    time += 1

    # works up to 10 mins. after that timer will stop
    if time == 6000:
        timer.stop()


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (80, 95), 48, 'White')
    canvas.draw_text(format_stops(), (10, 25), 24, 'Red')

# create frame
frame = simplegui.create_frame('Stopwatch', 300, 150)

# create timer
timer = simplegui.create_timer(100, increment_time)

# register event handlers
frame.set_draw_handler(draw_handler)

start_button = frame.add_button('Start', start_watch, 200)
stop_button = frame.add_button('Stop', stop_watch, 200)
reset_button = frame.add_button('Reset', reset_watch, 200)

# start frame
frame.start()

# Please remember to review the grading rubric
