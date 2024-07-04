import gui as gui
import crowdebug as cdb


def main():

    cdb.log.info("Starting Log Test")
    cdb.log_test()
    cdb.log.info("Measuring Screen Size")
    gui.default_config_check()
    cdb.log.info("Starting GUI")
    gui.start_gui()






if __name__ == "__main__":
    main()
    cdb.log.info("End Program - Clearing Terminal")
    cdb.clear_terminal()

