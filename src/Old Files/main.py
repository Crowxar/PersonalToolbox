# pilot_list = ["Botzer","Hempen","Landry","O'Neil","Turner","Griffin","Segreti"]  
import gui
import configparser as cp

config_file = 'config.ini'
config = cp.ConfigParser()

home = "home"
schedule = "schedule"

def main():
    gui.show_frame(home)
    
    
    
if __name__ == "__main__":
    main()