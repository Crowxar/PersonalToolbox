import logging as log
import os

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