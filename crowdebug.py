import logging as log
import tkinter as tk
import os

# import sys
# sys.path.append(r'C:\Users\micha\OneDrive\Pictures\Documents\VSCode Files')
# import crowdebug as cdb


# region Screen Size Stuff
def calculate_screensize():
    sizeroot = tk.Tk()
    screen_width, screen_height = (
        sizeroot.winfo_screenwidth(),
        sizeroot.winfo_screenheight())
    sizeroot.destroy()
    window_width = screen_width // 2
    window_height = screen_height // 2
    pos_x = window_width // 2
    pos_y = window_height // 2

    return screen_width, screen_height, window_width, window_height, pos_x, pos_y


def centered_screen():
    screen_width, screen_height, window_width, window_height, pos_x, pos_y = calculate_screensize()
    return f"{window_width}x{window_height}+{pos_x}+{pos_y}"

def print_screensize():
    screen_width, screen_height, window_width, window_height, pos_x, pos_y = calculate_screensize()
    print(f"Screen Size: {screen_width}x{screen_height}")
    print(f"Window Size: {window_width}x{window_height}")
    print(f"Position: {pos_x}, {pos_y}")
    
#endregion

def clear_terminal(any=None):
    if any is None:
        os.system('cls')
        print('CDB - Program Cleared')


def button_test(name): # command=lambda: DBG.button_test(name)
    if name:
        print(f"CDB - {name.capitalize()} Button Pressed")
    else:
        print("CDB - Button Pressed")


def button_toggle_test(label_text):
    print(f"CDB - {label_text} toggled")

def log_test():
    log.debug('debug test 1/5') # Detailed information, typically of interest only when diagnosing problems.
    log.info('info test 2/5') # Confirmation that things are working as expected.
    log.warning('warning test 3/5')# Potential problem that doesn't prevent the program from running
    log.error('error test 4/5')# Serious problem that prevents a specific operation from completing successfully.
    log.critical('critical test 5/5')# Very serious error that may prevent the application from continuing to run.
    log.info('Logging Tests complete! Program starts now! \n \n')

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(filename)s %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        log.FileHandler('Debug.log', mode='w'),  # 'w' mode overwrites the log file each time
    ]
)

print_screensize()