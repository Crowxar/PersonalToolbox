import gui as gui
import crowdebug as cdb


def main():
    cdb.log.info("Starting Log Test")
    cdb.log_test()
    cdb.log.info("Starting GUI")
    gui.show_frame(gui.home)


if __name__ == "__main__":
    main()
    cdb.log.info("End Program - Clearing Terminal")
    cdb.clear_terminal()

